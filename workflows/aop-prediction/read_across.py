from __future__ import annotations

import json
import os
import re
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Optional, Sequence

import numpy as np

try:
    from rdkit import Chem, DataStructs
    from rdkit.Chem import AllChem
    from rdkit.Chem import rdFingerprintGenerator
except Exception as e:  # pragma: no cover
    raise RuntimeError("RDKit is required for read_across.py.") from e

try:
    from ctx_api import (
        fetch_chemical_details,
        fetch_chemical_details_by_dtxcid,
        fetch_chemical_details_by_smiles,
        fetch_compound_bundle,
        resolve_chemical,
        resolve_query_chemical,
        search_chemical,
    )
except Exception:  # pragma: no cover
    fetch_chemical_details = None  # type: ignore
    fetch_chemical_details_by_dtxcid = None  # type: ignore
    fetch_chemical_details_by_smiles = None  # type: ignore
    fetch_compound_bundle = None  # type: ignore
    resolve_chemical = None  # type: ignore
    resolve_query_chemical = None  # type: ignore
    search_chemical = None  # type: ignore

READ_ACROSS_TOP_K = int(os.environ.get("READ_ACROSS_TOP_K", "5"))
READ_ACROSS_MIN_SIMILARITY = float(os.environ.get("READ_ACROSS_MIN_SIMILARITY", "0.25"))
READ_ACROSS_ALLOW_REMOTE_RESOLUTION = os.environ.get("READ_ACROSS_ALLOW_REMOTE_RESOLUTION", "true").lower() == "true"
READ_ACROSS_METHOD = os.environ.get("READ_ACROSS_METHOD", "auto").strip().lower()
READ_ACROSS_CTX_ONLY = os.environ.get("READ_ACROSS_CTX_ONLY", "true").lower() == "true"
FP_RADIUS = int(os.environ.get("READ_ACROSS_FP_RADIUS", "2"))
FP_NBITS = int(os.environ.get("READ_ACROSS_FP_NBITS", "2048"))

STOPWORDS = {
    "a", "an", "and", "of", "the", "to", "in", "for", "with", "via", "by", "from",
    "is", "are", "be", "as", "at", "or", "this", "that", "these", "those", "on",
    "chemical", "compound", "target", "profile", "assay", "endpoint", "effect", "data",
    "study", "result", "results", "source", "evidence", "summary", "reference",
}


def _normalize_text(value: Any) -> str:
    text = str(value or "").lower().strip()
    text = re.sub(os.environ.get("READ_ACROSS_REMOVE_PATTERN", r"[^a-z0-9]+"), " ", text)
    return re.sub(os.environ.get("READ_ACROSS_WHITESPACE_PATTERN", r"\s+"), " ", text).strip()


def _tokens(value: Any) -> set[str]:
    return {t for t in _normalize_text(value).split() if t and t not in STOPWORDS}


def _as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return []
        if s.startswith("[") and s.endswith("]"):
            try:
                parsed = json.loads(s)
                if isinstance(parsed, list):
                    return [str(v).strip() for v in parsed if str(v).strip()]
            except Exception:
                pass
        return [p.strip() for p in re.split(r"[|;,]\s*", s) if p.strip()]
    return [str(value).strip()] if str(value).strip() else []


def _canonicalize_smiles(smiles: str) -> Optional[str]:
    if not smiles:
        return None
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol, canonical=True) if mol else None


_MORGAN_GENERATOR = rdFingerprintGenerator.GetMorganGenerator(
    radius=FP_RADIUS,
    fpSize=FP_NBITS,
)

def fingerprint_from_smiles(smiles: str):
    mol = Chem.MolFromSmiles(smiles or "")
    return None if mol is None else _MORGAN_GENERATOR.GetFingerprint(mol)


def tanimoto_from_smiles(smiles_a: str, smiles_b: str) -> float:
    fp_a = fingerprint_from_smiles(smiles_a)
    fp_b = fingerprint_from_smiles(smiles_b)
    if fp_a is None or fp_b is None:
        return 0.0
    return float(DataStructs.TanimotoSimilarity(fp_a, fp_b))


def is_probable_smiles(value: str) -> bool:
    s = str(value or "").strip()
    return bool(s) and len(s) > 2 and any(ch in s for ch in ("=", "#", "[", "]", "(", ")"))


def _is_valid_chemical_name(name: str) -> bool:
    if not name or not isinstance(name, str):
        return False
    name = name.strip()
    return bool(name) and any(c.isalpha() for c in name) and not any(
        re.match(p, name)
        for p in [r'^\s*$', r'^\d+$', r'^[^a-zA-Z0-9\s\-\.\,\(\)\/]+$']
    )


def _merge_nonempty_dict(base: Dict[str, Any], extra: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    base = dict(base or {})
    if not isinstance(extra, dict):
        return base
    for k, v in extra.items():
        if v not in (None, "", [], {}, ()):
            base[k] = v
    return base


def _first_dict(obj: Any) -> Dict[str, Any]:
    if isinstance(obj, dict):
        for key in ("results", "data", "items", "records", "chemicals", "compounds", "hits"):
            v = obj.get(key)
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        return item
            if isinstance(v, dict):
                return v
        return obj
    if isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                return item
    return {}


def _records(obj: Any) -> List[Dict[str, Any]]:
    if isinstance(obj, dict):
        for key in ("results", "data", "items", "records", "chemicals", "compounds", "hits"):
            v = obj.get(key)
            if isinstance(v, list):
                return [x for x in v if isinstance(x, dict)]
        return [obj] if obj else []
    if isinstance(obj, list):
        return [x for x in obj if isinstance(x, dict)]
    return []

def _is_likely_chemical_seed(name: str) -> bool:
    s = str(name or "").strip()
    if not s:
        return False
    if re.fullmatch(r"[A-Z0-9\-]{3,}", s):  # PTGS1, TP53, etc.
        return False
    return any(c.isalpha() for c in s)


def _normalize_chemical_details(query: str, item: Dict[str, Any], source: str = "ctx") -> Dict[str, Any]:
    dtxsid = str(item.get("dtxsid") or item.get("DTXSID") or item.get("substance_id") or item.get("substanceId") or "").strip()
    dtxcid = str(item.get("dtxcid") or item.get("DTXCID") or item.get("cid") or item.get("CID") or "").strip()
    name = str(item.get("name") or item.get("chemical_name") or item.get("title") or item.get("preferred_name") or query).strip()
    smiles = str(item.get("smiles") or item.get("CanonicalSMILES") or item.get("canonical_smiles") or item.get("IsomericSMILES") or item.get("isomeric_smiles") or "").strip()
    if smiles:
        smiles = _canonicalize_smiles(smiles) or smiles
    inchikey = str(item.get("inchikey") or item.get("InChIKey") or item.get("inchi_key") or "").strip()
    formula = str(item.get("formula") or item.get("MolecularFormula") or item.get("molecular_formula") or "").strip()
    return {"query": query, "status": "ok", "name": name, "dtxsid": dtxsid, "dtxcid": dtxcid, "smiles": smiles, "inchikey": inchikey, "formula": formula, "source": source, "raw": item}


def _ctx_search(query: str, by: str = "equals") -> List[Dict[str, Any]]:
    if search_chemical is None:
        return []
    try:
        return search_chemical(query, by=by) or []
    except Exception:
        return []


def _ctx_lookup_chemical(query: str) -> Dict[str, Any]:
    q = str(query or "").strip()
    if not q:
        return {"query": "", "status": "empty_query", "name": "", "smiles": "", "raw": {}}

    resolved = resolve_query_chemical(q) if resolve_query_chemical is not None else resolve_chemical(q)
    resolved = dict(resolved or {})
    if resolved.get("smiles"):
        pass
    else:
        hits = _ctx_search(q, "equals") or _ctx_search(q, "contains")
        if hits:
            resolved = _merge_nonempty_dict(resolved, _normalize_chemical_details(q, hits[0], "ctx_search"))

    if not resolved.get("smiles") and resolved.get("dtxsid") and fetch_chemical_details is not None:
        try:
            details = fetch_chemical_details(str(resolved["dtxsid"]))
            if details:
                resolved = _merge_nonempty_dict(resolved, _normalize_chemical_details(q, details, "ctx_details_dtxsid"))
        except Exception:
            pass
    if not resolved.get("smiles") and resolved.get("dtxcid") and fetch_chemical_details_by_dtxcid is not None:
        try:
            details = fetch_chemical_details_by_dtxcid(str(resolved["dtxcid"]))
            if details:
                resolved = _merge_nonempty_dict(resolved, _normalize_chemical_details(q, details, "ctx_details_dtxcid"))
        except Exception:
            pass
    if not resolved.get("smiles") and is_probable_smiles(q) and fetch_chemical_details_by_smiles is not None:
        try:
            details = fetch_chemical_details_by_smiles(q)
            if details:
                resolved = _merge_nonempty_dict(resolved, _normalize_chemical_details(q, details, "ctx_details_smiles"))
        except Exception:
            pass
    if not resolved.get("smiles") and is_probable_smiles(q):
        canon = _canonicalize_smiles(q)
        if canon:
            resolved = _merge_nonempty_dict(resolved, {"query": q, "status": "ok", "name": q, "smiles": canon, "source": "direct_smiles"})
    if not resolved.get("name"):
        resolved["name"] = q
    if not resolved.get("status"):
        resolved["status"] = "not_found"
    return resolved


def _ctx_bundle(query: str) -> Dict[str, Any]:
    if fetch_compound_bundle is None:
        return {}
    try:
        return fetch_compound_bundle(query) or {}
    except Exception:
        return {}


# -------------------------
# Read-across source records
# -------------------------

def _profile_text(target_profile: Dict[str, Any], mies: Sequence[Dict[str, Any]] | None = None) -> str:
    if not isinstance(target_profile, dict):
        return ""
    parts: List[str] = []
    props = target_profile.get("properties", {}) if isinstance(target_profile.get("properties", {}), dict) else {}
    for k, v in props.items():
        parts.append(str(k))
        if isinstance(v, (list, tuple, set)):
            parts.extend(map(str, v))
        else:
            parts.append(str(v))
    parts.extend(_as_list(target_profile.get("liabilities", [])))
    if mies:
        for mie in mies:
            if isinstance(mie, dict):
                parts.append(str(mie.get("name", "")))
                parts.append(str(mie.get("reasoning", "")))
    return _normalize_text(" ".join(parts))


def _ctx_seed_names(target_profile: Optional[Dict[str, Any]], mies: Optional[Sequence[Dict[str, Any]]] = None) -> List[str]:
    if not isinstance(target_profile, dict):
        return []
    names: List[str] = []
    props = target_profile.get("properties", {}) if isinstance(target_profile.get("properties", {}), dict) else {}
    for key in ("similar_chemicals", "reference_chemicals", "analog_chemicals", "seed_chemicals"):
        names.extend(_as_list(target_profile.get(key)))
        names.extend(_as_list(props.get(key)))
    if mies:
        for mie in mies:
            if isinstance(mie, dict):
                for key in ("similar_chemicals", "reference_chemicals", "analog_chemicals"):
                    names.extend(_as_list(mie.get(key)))
    return [n for n in dict.fromkeys(str(n).strip() for n in names if str(n).strip())]


def _infer_read_across_method(target_profile: Optional[Dict[str, Any]], mies: Optional[Sequence[Dict[str, Any]]] = None, chemical: str = "") -> str:
    seed_names = _ctx_seed_names(target_profile, mies)
    props = target_profile.get("properties", {}) if isinstance(target_profile, dict) else {}
    target_class = _normalize_text(" ".join([
        str(target_profile.get("target_class", "")) if isinstance(target_profile, dict) else "",
        str(props.get("target_class", "")) if isinstance(props, dict) else "",
        str(props.get("mechanism_of_action", "")) if isinstance(props, dict) else "",
    ]))
    if len(seed_names) <= 3:
        return "analogue"
    if len(seed_names) >= 4:
        return "category"
    if any(k in target_class for k in ("class", "family", "category", "group")):
        return "category"
    return "analogue"


def _ctx_seed_reference_records(target_profile: Optional[Dict[str, Any]], mies: Optional[Sequence[Dict[str, Any]]] = None, *, max_seeds: int = 8, method: str = "analogue") -> List[Dict[str, Any]]:
    seed_names = _ctx_seed_names(target_profile, mies)
    if not seed_names and method == "category":
        props = target_profile.get("properties", {}) if isinstance(target_profile, dict) else {}
        seed_names = [x for x in _as_list(target_profile.get("target_class")) + _as_list(props.get("target_class")) + _as_list(props.get("mechanism_of_action")) if x]

    records: List[Dict[str, Any]] = []
    for seed in seed_names[:max_seeds]:
        if not _is_likely_chemical_seed(seed):
            continue
        chem = _ctx_lookup_chemical(seed)
    for seed in seed_names[:max_seeds]:
        if not _is_likely_chemical_seed(seed):
            continue
        chem = _ctx_lookup_chemical(seed)
        bundle = _ctx_bundle(seed) if READ_ACROSS_CTX_ONLY or fetch_compound_bundle is not None else {}
        merged: Dict[str, Any] = {}
        if isinstance(bundle.get("chemical"), dict):
            merged = _merge_nonempty_dict(merged, bundle["chemical"])
        if isinstance(bundle.get("chemical_details"), dict):
            merged = _merge_nonempty_dict(merged, bundle["chemical_details"])
        merged = _merge_nonempty_dict(merged, chem)
        if not merged.get("smiles"):
            continue

        labels: List[str] = []
        if isinstance(target_profile, dict):
            labels.extend(_as_list(target_profile.get("liabilities")))
            labels.extend(_as_list(target_profile.get("known_targets")))
            props = target_profile.get("properties", {}) if isinstance(target_profile.get("properties", {}), dict) else {}
            labels.extend(_as_list(props.get("known_targets")))
            labels.extend(_as_list(props.get("mechanism_of_action")))
            labels.extend(_as_list(props.get("target_class")))
        labels.append(seed)

        summary = str((bundle.get("chemical_details") or {}).get("title") or (bundle.get("chemical_details") or {}).get("name") or merged.get("name") or seed)
        record = {
            "name": str(merged.get("name") or seed).strip() or seed,
            "chemical_name": str(merged.get("name") or seed).strip() or seed,
            "smiles": str(merged.get("smiles") or "").strip(),
            "dtxsid": str(merged.get("dtxsid") or "").strip(),
            "dtxcid": str(merged.get("dtxcid") or "").strip(),
            "inchikey": str(merged.get("inchikey") or "").strip(),
            "formula": str(merged.get("formula") or "").strip(),
            "endpoint": ", ".join(v for v in [
                "bioactivity" if bundle.get("bioactivity") else "",
                "exposure" if bundle.get("exposure") else "",
                "hazard" if bundle.get("hazard") else "",
            ] if v),
            "labels": list(dict.fromkeys(v for v in labels if v)),
            "source": "ctx_seed",
            "summary": summary,
            "raw": {"ctx_bundle": bundle, "resolved": merged},
        }
        records.append(record)

    return _dedupe_reference_records(records)


# -------------------------
# Normalization / deduplication
# -------------------------

def normalize_reference_record(rec: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(rec, dict):
        return {}
    rec = dict(rec)
    name = str(rec.get("name") or rec.get("chemical_name") or rec.get("compound") or rec.get("preferred_name") or rec.get("title") or rec.get("sample_name") or rec.get("record_id") or "unknown").strip()
    smiles = str(rec.get("smiles") or rec.get("canonical_smiles") or rec.get("isomeric_smiles") or "").strip()
    if smiles:
        canon = _canonicalize_smiles(smiles)
        if canon:
            smiles = canon
    labels = list(dict.fromkeys(_as_list(rec.get("labels")) + _as_list(rec.get("tags")) + _as_list(rec.get("liabilities"))))
    if not name or name == "unknown":
        return {}
    if not smiles and not str(rec.get("dtxsid") or "").strip() and not str(rec.get("dtxcid") or "").strip():
        return {}
    return {
        "record_id": str(rec.get("record_id") or name).strip(),
        "name": name,
        "chemical_name": str(rec.get("chemical_name") or name).strip(),
        "smiles": smiles,
        "dtxsid": str(rec.get("dtxsid") or "").strip(),
        "dtxcid": str(rec.get("dtxcid") or "").strip(),
        "inchikey": str(rec.get("inchikey") or "").strip(),
        "formula": str(rec.get("formula") or "").strip(),
        "endpoint": str(rec.get("endpoint") or "").strip(),
        "labels": labels,
        "source": str(rec.get("source") or "ctx_reference").strip(),
        "summary": rec.get("summary") or "",
        "raw": rec,
    }


def _dedupe_reference_records(rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    deduped: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        candidate = normalize_reference_record(row)
        if not candidate:
            continue
        key = candidate.get("smiles") or candidate.get("dtxsid") or candidate.get("dtxcid") or candidate.get("record_id") or candidate.get("name")
        key = str(key).strip().lower()
        if not key:
            continue
        if key not in deduped:
            deduped[key] = candidate
            continue
        existing = deduped[key]
        for field in ("name", "chemical_name", "dtxsid", "dtxcid", "inchikey", "formula", "endpoint", "source", "summary"):
            if not existing.get(field) and candidate.get(field):
                existing[field] = candidate[field]
        if candidate.get("smiles") and not existing.get("smiles"):
            existing["smiles"] = candidate["smiles"]
        existing["labels"] = list(dict.fromkeys((existing.get("labels") or []) + (candidate.get("labels") or [])))
        if candidate.get("raw"):
            existing["raw"] = {**candidate.get("raw", {}), **(existing.get("raw") or {})}
    return list(deduped.values())


# -------------------------
# Scoring
# -------------------------

def _record_name(record: Dict[str, Any]) -> str:
    for key in ("name", "chemical_name", "compound", "preferred_name", "title", "sample_name", "stressor"):
        value = str(record.get(key, "")).strip()
        if value:
            return value
    return "unknown"


def _record_smiles(record: Dict[str, Any]) -> str:
    for key in ("smiles", "canonical_smiles", "isomeric_smiles", "SMILES"):
        value = str(record.get(key, "")).strip()
        if value:
            return _canonicalize_smiles(value) or value
    return ""


def _record_endpoints(record: Dict[str, Any]) -> List[str]:
    vals: List[str] = []
    for key in ("endpoint", "endpoint_name", "endpoints", "assay", "assay_name", "protocol_name", "effect"):
        vals.extend(_as_list(record.get(key)))
    return [v for v in dict.fromkeys(v.strip() for v in vals if v.strip())]


def _record_labels(record: Dict[str, Any]) -> List[str]:
    vals: List[str] = []
    for key in ("labels", "tags", "liabilities", "target_class", "mechanism_of_action", "stressor", "aop"):
        vals.extend(_as_list(record.get(key)))
    return [v for v in dict.fromkeys(v.strip() for v in vals if v.strip())]


def _reference_annotation_text(record: Dict[str, Any]) -> str:
    parts: List[str] = []
    for key in ("name", "target_class", "mechanism_of_action", "endpoint", "assay_name", "summary", "evidence", "reasoning", "source", "stressor", "aop", "liabilities", "labels", "tags"):
        val = record.get(key)
        if not val:
            continue
        if isinstance(val, (list, tuple, set)):
            parts.extend(map(str, val))
        else:
            parts.append(str(val))
    return _normalize_text(" ".join(parts))


def _score_single_reference(query_smiles: str, query_labels: set[str], record: Dict[str, Any], allow_remote_resolution: bool = True) -> Dict[str, Any]:
    name = _record_name(record)
    record_smiles = _record_smiles(record)

    if not record_smiles and allow_remote_resolution and search_chemical is not None:
        try:
            hits = search_chemical(name, by="equals") or search_chemical(name, by="contains")
            if hits:
                detail = _normalize_chemical_details(name, hits[0], "ctx_search")
                record_smiles = detail.get("smiles") or ""
                if not record_smiles and detail.get("dtxsid") and fetch_chemical_details is not None:
                    d = fetch_chemical_details(str(detail["dtxsid"]))
                    record_smiles = str(d.get("smiles") or d.get("CanonicalSMILES") or d.get("canonical_smiles") or d.get("IsomericSMILES") or "").strip()
                if record_smiles:
                    record["smiles"] = record_smiles
        except Exception:
            record_smiles = ""

    sim = tanimoto_from_smiles(query_smiles, record_smiles) if query_smiles and record_smiles else 0.0
    record_text = _reference_annotation_text(record)
    record_labels = set(_tokens(_record_labels(record)))
    label_overlap = len(query_labels & record_labels)

    structural_weight = float(os.environ.get("READ_ACROSS_STRUCTURAL_WEIGHT", "0.90"))
    max_bonus = float(os.environ.get("READ_ACROSS_MAX_BONUS", "0.10"))
    bonus_per_overlap = float(os.environ.get("READ_ACROSS_BONUS_PER_OVERLAP", "0.05"))
    bonus = min(max_bonus, bonus_per_overlap * label_overlap)
    score = float(np.clip(structural_weight * sim + bonus, 0.0, 1.0))

    reasons: List[str] = []
    if sim:
        reasons.append("fingerprint similarity")
    if label_overlap:
        reasons.append("shared annotation terms")
    if record_text and not reasons:
        reasons.append("structure and annotation overlap")
    if not reasons:
        reasons.append("structure and annotation overlap")

    return {
        "name": name,
        "score": score,
        "similarity": score,
        "raw_similarity": sim,
        "reasoning": "; ".join(reasons),
        "smiles": record_smiles,
        "endpoint": ", ".join(_record_endpoints(record)),
        "source": record.get("source") or record.get("dataset") or "ctx_reference",
        "labels": sorted(record_labels),
        "raw": record,
    }


# -------------------------
# Main read-across API
# -------------------------

def score_against_reference_library(
    query_smiles: str,
    target_profile: Optional[Dict[str, Any]] = None,
    mies: Optional[Sequence[Dict[str, Any]]] = None,
    reference_library: Optional[Sequence[Dict[str, Any]]] = None,
    top_k: Optional[int] = None,
    min_similarity: Optional[float] = None,
    allow_remote_resolution: Optional[bool] = None,
) -> Dict[str, Any]:
    """Score a query structure against CTX-derived analog records using RDKit fingerprints."""
    query_smiles = _canonicalize_smiles(query_smiles or "") or (query_smiles or "")
    target_profile = target_profile or {}
    mies = mies or []

    method = READ_ACROSS_METHOD or "auto"
    method = _infer_read_across_method(target_profile, mies) if method == "auto" else method
    reference_library = []  # CTX-only: ignore any local library input.
    ctx_seed_records = _ctx_seed_reference_records(target_profile, mies, method=method)
    reference_library = _dedupe_reference_records(list(reference_library) + list(ctx_seed_records))

    top_k = int(top_k if top_k is not None else READ_ACROSS_TOP_K)
    min_similarity = float(min_similarity if min_similarity is not None else READ_ACROSS_MIN_SIMILARITY)
    allow_remote_resolution = bool(READ_ACROSS_ALLOW_REMOTE_RESOLUTION if allow_remote_resolution is None else allow_remote_resolution)

    query_text = _profile_text(target_profile, mies)
    query_labels = _tokens(query_text)

    scored = [
        _score_single_reference(query_smiles=query_smiles, query_labels=query_labels, record=record, allow_remote_resolution=allow_remote_resolution)
        for record in reference_library
        if isinstance(record, dict)
    ]
    scored.sort(key=lambda x: float(x.get("score") or 0.0), reverse=True)
    top = [x for x in scored if float(x.get("score") or 0.0) >= min_similarity][:top_k]

    analogs: List[Dict[str, Any]] = []
    supporting_evidence: List[str] = []
    matched_endpoints: List[str] = []
    for item in top:
        analogs.append({
            "name": item.get("name"),
            "score": float(item.get("score") or 0.0),
            "similarity": float(item.get("similarity") or 0.0),
            "raw_similarity": float(item.get("raw_similarity") or 0.0),
            "endpoint": item.get("endpoint", ""),
            "source": item.get("source", ""),
            "labels": item.get("labels", []),
            "reasoning": item.get("reasoning", ""),
        })
        if item.get("endpoint"):
            matched_endpoints.extend([e.strip() for e in str(item.get("endpoint")).split(",") if e.strip()])
        if item.get("reasoning"):
            supporting_evidence.append(f"{item.get('name')}: {item.get('reasoning')}")

    avg_score = float(mean([a["score"] for a in analogs])) if analogs else 0.0
    confidence = float(np.clip(avg_score, 0.0, 1.0))
    summary = summarize_read_across({
        "status": "ok" if analogs else "no_analogs",
        "query": query_smiles,
        "analogs": analogs,
        "matched_endpoints": sorted(dict.fromkeys(matched_endpoints)),
        "supporting_evidence": supporting_evidence,
        "confidence": confidence,
    })

    return {
        "status": "ok" if analogs else "no_analogs",
        "query": query_smiles,
        "analogs": analogs,
        "matched_endpoints": sorted(dict.fromkeys(matched_endpoints)),
        "supporting_evidence": supporting_evidence,
        "confidence": confidence,
        "summary": summary,
        "method": method,
        "library_size": len(reference_library),
        "scored_count": len(scored),
        "top_k": top_k,
        "min_similarity": min_similarity,
        "ctx_seed_records": ctx_seed_records,
        "ctx_seed_count": len(ctx_seed_records),
    }

def enrich_read_across(
    chemical: str,
    target_profile: Optional[Dict[str, Any]] = None,
    mies: Optional[Sequence[Dict[str, Any]]] = None,
    top_k: Optional[int] = None,
    min_similarity: Optional[float] = None,
    allow_remote_resolution: Optional[bool] = None,
    use_ctx: bool = False,
    method: Optional[str] = None,
) -> Dict[str, Any]:
    chemical = str(chemical or "").strip()
    if not chemical:
        return {"status": "empty_query", "query": "", "analogs": [], "matched_endpoints": [], "supporting_evidence": [], "confidence": 0.0, "summary": "No query chemical provided."}
    if not _is_valid_chemical_name(chemical):
        return {"status": "invalid_name_format", "query": chemical, "analogs": [], "matched_endpoints": [], "supporting_evidence": [], "confidence": 0.0, "summary": f"Invalid chemical name format: {chemical}", "error": "Chemical name does not meet validation criteria"}

    query = _ctx_lookup_chemical(chemical)
    selected_method = (method or READ_ACROSS_METHOD or "auto").strip().lower()
    if selected_method == "auto":
        selected_method = _infer_read_across_method(target_profile, mies, chemical)

    if selected_method == "analogue":
        top_k = int(top_k if top_k is not None else min(3, READ_ACROSS_TOP_K))
        min_similarity = float(min_similarity if min_similarity is not None else max(0.35, READ_ACROSS_MIN_SIMILARITY))
    else:
        top_k = int(top_k if top_k is not None else max(READ_ACROSS_TOP_K, 8))
        min_similarity = float(min_similarity if min_similarity is not None else max(0.20, READ_ACROSS_MIN_SIMILARITY * 0.8))

    query_smiles = str(query.get("smiles") or "")
    result: Dict[str, Any]
    if not query_smiles:
        result = {"status": query.get("status", "not_found"), "query": chemical, "chemical": query, "analogs": [], "matched_endpoints": [], "supporting_evidence": [], "confidence": 0.0, "summary": f"Unable to resolve {chemical} to a structure."}
    else:
        result = score_against_reference_library(
            query_smiles=query_smiles,
            target_profile=target_profile,
            mies=mies,
            reference_library=None,
            top_k=top_k,
            min_similarity=min_similarity,
            allow_remote_resolution=allow_remote_resolution,
        )
        result["query_name"] = chemical
        result["chemical"] = query

    result["method"] = selected_method
    result["method_reason"] = (
        "Analogue approach: one/few close source chemicals"
        if selected_method == "analogue"
        else "Category approach: broader source set for class-level patterns"
    )

    if use_ctx and fetch_compound_bundle is not None:
        try:
            result["ctx_bundle"] = fetch_compound_bundle(chemical)
        except Exception:
            result["ctx_bundle"] = {}
    return result


def enrich_read_across_state(state: Dict[str, Any], use_ctx: bool = False, method: Optional[str] = None) -> Dict[str, Any]:
    data = state.setdefault("data", {})
    if not isinstance(data, dict):
        data = {}
        state["data"] = data

    if data.get("read_across_attempted", False):
        return state

    chemical = str(state.get("chemical", "")).strip()
    if not chemical:
        return state
    if not _is_valid_chemical_name(chemical):
        data["read_across"] = {"status": "invalid_name_format", "query": chemical, "analogs": [], "matched_endpoints": [], "supporting_evidence": [], "confidence": 0.0, "summary": f"Invalid chemical name format: {chemical}", "error": "Chemical name does not meet validation criteria"}
        data["read_across_attempted"] = True
        return state

    target_profile = data.get("target_profile", {}) if isinstance(data.get("target_profile", {}), dict) else {}
    if not target_profile:
        return state


    data["read_across_attempted"] = True
    result = enrich_read_across(chemical=chemical, target_profile=target_profile, mies=state.get("MIEs", []), use_ctx=use_ctx, method=method)
    data["read_across"] = result
    return state


def _profile_text(target_profile: Dict[str, Any], mies: Sequence[Dict[str, Any]] | None = None) -> str:
    if not isinstance(target_profile, dict):
        return ""
    parts: List[str] = []
    props = target_profile.get("properties", {}) if isinstance(target_profile.get("properties", {}), dict) else {}
    for k, v in props.items():
        parts.append(str(k))
        if isinstance(v, (list, tuple, set)):
            parts.extend(map(str, v))
        else:
            parts.append(str(v))
    parts.extend(_as_list(target_profile.get("liabilities", [])))
    if mies:
        for mie in mies:
            if isinstance(mie, dict):
                parts.append(str(mie.get("name", "")))
                parts.append(str(mie.get("reasoning", "")))
    return _normalize_text(" ".join(parts))

def summarize_read_across(result: Dict[str, Any]) -> str:
    if not isinstance(result, dict):
        return ""
    if result.get("status") in {"empty_query", "not_found"}:
        return str(result.get("summary", ""))
    analogs = result.get("analogs", []) if isinstance(result.get("analogs", []), list) else []
    if not analogs:
        return str(result.get("summary", "No CTX analogs found."))
    parts = [f"{a.get('name', 'unknown')} (sim {float(a.get('score') or 0.0):.2f})" for a in analogs[:3]]
    endpoints = result.get("matched_endpoints", [])
    endpoint_text = f"; endpoints: {', '.join(endpoints[:5])}" if endpoints else ""
    return f"Top CTX-derived analogs: {', '.join(parts)}{endpoint_text}."


def evaluate_candidates_read_across(*args, **kwargs):
    return score_against_reference_library(*args, **kwargs)


__all__ = [
    "enrich_read_across",
    "enrich_read_across_state",
    "evaluate_candidates_read_across",
    "fingerprint_from_smiles",
    "is_probable_smiles",
    "normalize_reference_record",
    "score_against_reference_library",
    "summarize_read_across",
    "tanimoto_from_smiles",
]
