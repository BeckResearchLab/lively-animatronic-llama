from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

try:
    import ctxpy as ctx  # type: ignore
except Exception:  # pragma: no cover
    ctx = None  # type: ignore

load_dotenv()

CTX_API_HOST = os.environ.get("ctx_api_host", os.environ.get("CTX_BASE_URL", "https://api.epa.gov/comptox-ptc")).rstrip("/")
CTX_API_ACCEPT = os.environ.get("ctx_api_accept", os.environ.get("CTX_ACCEPT", "application/json"))
CTX_X_API_KEY = os.environ.get("ctx_x_api_key", os.environ.get("CTX_API_KEY", "")).strip()


# -------------------------
# client helpers
# -------------------------

def _chemical_client() -> Any:
    if ctx is None:
        raise RuntimeError("ctxpy is not available.")
    try:
        if CTX_X_API_KEY:
            return ctx.Chemical(x_api_key=CTX_X_API_KEY)
        return ctx.Chemical()
    except Exception as e:  # pragma: no cover
        raise RuntimeError(f"Unable to initialize CTX Chemical client: {e}") from e


def _search_hits(result: Any) -> List[Dict[str, Any]]:
    if isinstance(result, dict):
        for key in ("results", "data", "items", "records", "chemicals", "compounds", "hits"):
            value = result.get(key)
            if isinstance(value, list):
                return [x for x in value if isinstance(x, dict)]
        return [result]
    if isinstance(result, list):
        return [x for x in result if isinstance(x, dict)]
    return []


def _first_hit(result: Any) -> Dict[str, Any]:
    hits = _search_hits(result)
    return hits[0] if hits else {}


def _extract_smiles(record: Dict[str, Any]) -> str:
    for key in (
        "smiles",
        "SMILES",
        "canonical_smiles",
        "CanonicalSMILES",
        "isomeric_smiles",
        "IsomericSMILES",
        "smiles_string",
        "structural_formula",
    ):
        value = str(record.get(key, "")).strip()
        if value:
            return value
    return ""


def _extract_name(record: Dict[str, Any], fallback: str = "") -> str:
    for key in ("name", "chemical_name", "preferred_name", "title", "substance_name", "common_name"):
        value = str(record.get(key, "")).strip()
        if value:
            return value
    return fallback


def _normalize_chemical_record(query: str, record: Dict[str, Any], source: str = "ctx") -> Dict[str, Any]:
    record = dict(record or {})
    dtxsid = str(record.get("dtxsid") or record.get("DTXSID") or record.get("substance_id") or record.get("substanceId") or "").strip()
    dtxcid = str(record.get("dtxcid") or record.get("DTXCID") or record.get("cid") or record.get("CID") or "").strip()
    name = _extract_name(record, fallback=query)
    smiles = _extract_smiles(record)
    inchikey = str(record.get("inchikey") or record.get("InChIKey") or record.get("inchi_key") or "").strip()
    formula = str(record.get("formula") or record.get("molecular_formula") or record.get("MolecularFormula") or "").strip()
    return {
        "query": query,
        "status": "ok" if (name or dtxsid or dtxcid or smiles) else "not_found",
        "name": name or query,
        "dtxsid": dtxsid,
        "dtxcid": dtxcid,
        "smiles": smiles,
        "inchikey": inchikey,
        "formula": formula,
        "source": source,
        "raw": record,
    }


# -------------------------
# public API
# -------------------------

def search_chemical(query: str, by: str = "equals") -> List[Dict[str, Any]]:
    chem = _chemical_client()
    result = chem.search(by=by, query=query)
    return _search_hits(result)


def fetch_chemical_details(identifier: str) -> Dict[str, Any]:
    chem = _chemical_client()
    result = chem.details(by="dtxsid", query=identifier)
    if isinstance(result, dict):
        return result
    return _first_hit(result)


def fetch_chemical_details_by_dtxcid(identifier: str) -> Dict[str, Any]:
    chem = _chemical_client()
    result = chem.details(by="dtxcid", query=identifier)
    if isinstance(result, dict):
        return result
    return _first_hit(result)


def fetch_chemical_details_by_smiles(smiles: str) -> Dict[str, Any]:
    chem = _chemical_client()
    try:
        result = chem.search(by="equals", query=smiles)
    except Exception:
        result = chem.search(by="contains", query=smiles)
    return _first_hit(result)


def resolve_chemical(query: str) -> Dict[str, Any]:
    chem = _chemical_client()
    try:
        try:
            result = chem.search(by="equals", query=query)
        except Exception:
            result = chem.search(by="contains", query=query)
    except Exception:
        return {"query": query, "status": "not_found", "name": query, "smiles": "", "raw": {}}

    hit = _first_hit(result)
    if not hit:
        return {"query": query, "status": "not_found", "name": query, "smiles": "", "raw": {}}

    normalized = _normalize_chemical_record(query, hit, source="ctx_search")
    if normalized.get("dtxsid"):
        try:
            details = fetch_chemical_details(normalized["dtxsid"])
            if isinstance(details, dict):
                normalized.update(_normalize_chemical_record(query, details, source="ctx_details_dtxsid"))
        except Exception:
            pass
    if not normalized.get("smiles") and normalized.get("dtxcid"):
        try:
            details = fetch_chemical_details_by_dtxcid(normalized["dtxcid"])
            if isinstance(details, dict):
                normalized.update(_normalize_chemical_record(query, details, source="ctx_details_dtxcid"))
        except Exception:
            pass
    return normalized


def resolve_query_chemical(query: str) -> Dict[str, Any]:
    return resolve_chemical(query)


def fetch_compound_bundle(query: str) -> Dict[str, Any]:
    chem = _chemical_client()
    resolved = resolve_chemical(query)
    bundle: Dict[str, Any] = {"query": query, "chemical": resolved, "chemical_details": {}, "bioactivity": {}, "exposure": {}, "hazard": {}, "raw": {}}

    dtxsid = str(resolved.get("dtxsid") or "").strip()
    dtxcid = str(resolved.get("dtxcid") or "").strip()
    if dtxsid:
        try:
            bundle["chemical_details"] = fetch_chemical_details(dtxsid)
        except Exception:
            bundle["chemical_details"] = {}
        for attr, path in (("bioactivity", "bioactivity/data/{dtxsid}"), ("exposure", "exposure/functional-use/{dtxsid}"), ("hazard", "hazard/toxvaldb/{dtxsid}")):
            try:
                getter = getattr(chem, attr, None)
                if callable(getter):
                    bundle[attr] = getter(dtxsid)
            except Exception:
                pass
    elif dtxcid:
        try:
            bundle["chemical_details"] = fetch_chemical_details_by_dtxcid(dtxcid)
        except Exception:
            bundle["chemical_details"] = {}

    bundle["raw"] = {
        "resolved": resolved,
        "chemical_details": bundle.get("chemical_details", {}),
        "bioactivity": bundle.get("bioactivity", {}),
        "exposure": bundle.get("exposure", {}),
        "hazard": bundle.get("hazard", {}),
    }
    return bundle


__all__ = [
    "CTX_API_ACCEPT",
    "CTX_API_HOST",
    "CTX_X_API_KEY",
    "fetch_chemical_details",
    "fetch_chemical_details_by_dtxcid",
    "fetch_chemical_details_by_smiles",
    "fetch_compound_bundle",
    "resolve_chemical",
    "resolve_query_chemical",
    "search_chemical",
]
