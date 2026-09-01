import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', 'a0e'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '949'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '926'),
            routes: [
              {
                path: '/docs/',
                component: ComponentCreator('/docs/', 'c47'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/agent-task-template',
                component: ComponentCreator('/docs/agent-operations/agent-task-template', 'ca6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/aop-2018-ingestion-audit',
                component: ComponentCreator('/docs/agent-operations/aop-2018-ingestion-audit', '22d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/omics-ingestion-operation-summary',
                component: ComponentCreator('/docs/agent-operations/omics-ingestion-operation-summary', '5a2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/verification-audit-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/verification-audit-2026-08-08', '8a2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/verification-report-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/verification-report-2026-08-08', 'bb1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/verification-summary-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/verification-summary-2026-08-08', '116'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/wiki-ingestion-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/wiki-ingestion-2026-08-08', '324'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/wiki-ingestion-2026-08-08-summary',
                component: ComponentCreator('/docs/agent-operations/wiki-ingestion-2026-08-08-summary', '660'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/wiki-verification-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/wiki-verification-2026-08-08', 'd35'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/wiki-write-operation-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/wiki-write-operation-2026-08-08', 'be6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/agent-operations/wiki-write-summary-2026-08-08',
                component: ComponentCreator('/docs/agent-operations/wiki-write-summary-2026-08-08', 'e32'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/ahr-activation-assay',
                component: ComponentCreator('/docs/assays/ahr-activation-assay', 'f43'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/ames-test',
                component: ComponentCreator('/docs/assays/ames-test', '216'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/carcinogenicity-profilers',
                component: ComponentCreator('/docs/assays/carcinogenicity-profilers', 'be4'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/comet-assay',
                component: ComponentCreator('/docs/assays/comet-assay', '077'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/estrogen-receptor-transactivation-assay',
                component: ComponentCreator('/docs/assays/estrogen-receptor-transactivation-assay', 'bb2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/herg-inhibition-assay',
                component: ComponentCreator('/docs/assays/herg-inhibition-assay', '33c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/hts',
                component: ComponentCreator('/docs/assays/hts', '2ab'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/in-vitro-systems',
                component: ComponentCreator('/docs/assays/in-vitro-systems', '502'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/micronucleus-assay',
                component: ComponentCreator('/docs/assays/micronucleus-assay', '188'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/mitochondrial-membrane-potential-assay',
                component: ComponentCreator('/docs/assays/mitochondrial-membrane-potential-assay', '074'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/molecular-docking',
                component: ComponentCreator('/docs/assays/molecular-docking', '752'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/mutagenicity-profilers',
                component: ComponentCreator('/docs/assays/mutagenicity-profilers', 'd47'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/nrf2-reporter-assay',
                component: ComponentCreator('/docs/assays/nrf2-reporter-assay', 'c02'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/qsar-prediction',
                component: ComponentCreator('/docs/assays/qsar-prediction', 'e63'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/assays/skin-sensitisation-profilers',
                component: ComponentCreator('/docs/assays/skin-sensitisation-profilers', '9be'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-aop-ingestion-summary',
                component: ComponentCreator('/docs/audit_records/2026-08-08-aop-ingestion-summary', '32b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-nam-framework-verification',
                component: ComponentCreator('/docs/audit_records/2026-08-08-nam-framework-verification', '155'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-nam-verification-audit',
                component: ComponentCreator('/docs/audit_records/2026-08-08-nam-verification-audit', 'e32'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-pbpk-nam-verification',
                component: ComponentCreator('/docs/audit_records/2026-08-08-pbpk-nam-verification', '2d6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-pbpk-nam-verification-report',
                component: ComponentCreator('/docs/audit_records/2026-08-08-pbpk-nam-verification-report', '223'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-verification-completion-summary',
                component: ComponentCreator('/docs/audit_records/2026-08-08-verification-completion-summary', '947'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-verification-operation',
                component: ComponentCreator('/docs/audit_records/2026-08-08-verification-operation', '371'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-verification-report',
                component: ComponentCreator('/docs/audit_records/2026-08-08-verification-report', '16e'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/2026-08-08-verification-summary',
                component: ComponentCreator('/docs/audit_records/2026-08-08-verification-summary', 'dd6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/audit-2026-08-08-aop-dev',
                component: ComponentCreator('/docs/audit_records/audit-2026-08-08-aop-dev', 'b0e'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit_records/audit-2026-08-08-nam-framework',
                component: ComponentCreator('/docs/audit_records/audit-2026-08-08-nam-framework', '19b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit-records/2026-08-08-omics-ingestion-audit',
                component: ComponentCreator('/docs/audit-records/2026-08-08-omics-ingestion-audit', 'f6d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit-records/2026-08-08-pbpk-nam-ingestion',
                component: ComponentCreator('/docs/audit-records/2026-08-08-pbpk-nam-ingestion', '9b0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit-records/audit-deeptox-ingestion-2026-08-08',
                component: ComponentCreator('/docs/audit-records/audit-deeptox-ingestion-2026-08-08', '95c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit/audit-chemical-databases-2024',
                component: ComponentCreator('/docs/audit/audit-chemical-databases-2024', 'c8e'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit/audit-literature-ml-chemoinformatics-2024',
                component: ComponentCreator('/docs/audit/audit-literature-ml-chemoinformatics-2024', '47a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit/audit-ml-algorithms-2024',
                component: ComponentCreator('/docs/audit/audit-ml-algorithms-2024', 'cdf'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/audit/audit-molecular-descriptors-2024',
                component: ComponentCreator('/docs/audit/audit-molecular-descriptors-2024', '7b5'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/biology/estrogen-receptors',
                component: ComponentCreator('/docs/biology/estrogen-receptors', 'fde'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/biology/gpcrs-kinases',
                component: ComponentCreator('/docs/biology/gpcrs-kinases', '662'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/agent-operations',
                component: ComponentCreator('/docs/category/agent-operations', 'ecc'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/assays',
                component: ComponentCreator('/docs/category/assays', 'a56'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/biology',
                component: ComponentCreator('/docs/category/biology', '806'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/chemicals',
                component: ComponentCreator('/docs/category/chemicals', '1b8'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/concepts',
                component: ComponentCreator('/docs/category/concepts', 'bc8'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/datasets',
                component: ComponentCreator('/docs/category/datasets', '304'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/evidence',
                component: ComponentCreator('/docs/category/evidence', 'fb0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/glossary',
                component: ComponentCreator('/docs/category/glossary', '281'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/indices',
                component: ComponentCreator('/docs/category/indices', '12f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/literature',
                component: ComponentCreator('/docs/category/literature', '701'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/models-and-methods',
                component: ComponentCreator('/docs/category/models-and-methods', '912'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/quality-and-governance',
                component: ComponentCreator('/docs/category/quality-and-governance', '6f0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/system',
                component: ComponentCreator('/docs/category/system', '8f9'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/toxicological-endpoints',
                component: ComponentCreator('/docs/category/toxicological-endpoints', '256'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/category/workflows',
                component: ComponentCreator('/docs/category/workflows', '112'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/acetaminophen',
                component: ComponentCreator('/docs/chemicals/acetaminophen', '34c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/aflatoxin-b1',
                component: ComponentCreator('/docs/chemicals/aflatoxin-b1', '8e1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/arsenic',
                component: ComponentCreator('/docs/chemicals/arsenic', 'ede'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/benzo-a-pyrene',
                component: ComponentCreator('/docs/chemicals/benzo-a-pyrene', '9d7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/bisphenol-a',
                component: ComponentCreator('/docs/chemicals/bisphenol-a', 'fa8'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/bisphenol-a-analogs',
                component: ComponentCreator('/docs/chemicals/bisphenol-a-analogs', '7c2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/bisphenol-af',
                component: ComponentCreator('/docs/chemicals/bisphenol-af', '6b3'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/cadmium',
                component: ComponentCreator('/docs/chemicals/cadmium', '7e7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/cerapp',
                component: ComponentCreator('/docs/chemicals/cerapp', '0ba'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/diethylhexyl-phthalate',
                component: ComponentCreator('/docs/chemicals/diethylhexyl-phthalate', '4ad'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/glyphosate',
                component: ComponentCreator('/docs/chemicals/glyphosate', '11d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/perfluorooctanoic-acid',
                component: ComponentCreator('/docs/chemicals/perfluorooctanoic-acid', 'b24'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/chemicals/tricosan',
                component: ComponentCreator('/docs/chemicals/tricosan', 'ba2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/adverse-outcome-pathway',
                component: ComponentCreator('/docs/concepts/adverse-outcome-pathway', 'cc7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/aop-framework',
                component: ComponentCreator('/docs/concepts/aop-framework', '6e4'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/aop-frameworks',
                component: ComponentCreator('/docs/concepts/aop-frameworks', '7a2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/applicability-domain',
                component: ComponentCreator('/docs/concepts/applicability-domain', '3f9'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/bioactivity',
                component: ComponentCreator('/docs/concepts/bioactivity', 'e14'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/citation-grounding',
                component: ComponentCreator('/docs/concepts/citation-grounding', 'a09'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/dataset-profiling',
                component: ComponentCreator('/docs/concepts/dataset-profiling', '329'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/dose-response-relationship',
                component: ComponentCreator('/docs/concepts/dose-response-relationship', 'a95'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/evidence-claim',
                component: ComponentCreator('/docs/concepts/evidence-claim', 'dc8'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/exposure',
                component: ComponentCreator('/docs/concepts/exposure', '828'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/general-toxicology',
                component: ComponentCreator('/docs/concepts/general-toxicology', 'c62'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/hazard',
                component: ComponentCreator('/docs/concepts/hazard', '416'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/human-review-checkpoint',
                component: ComponentCreator('/docs/concepts/human-review-checkpoint', 'ebd'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/key-event-relationships',
                component: ComponentCreator('/docs/concepts/key-event-relationships', '730'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/mechanism-of-action',
                component: ComponentCreator('/docs/concepts/mechanism-of-action', 'eda'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/mixture-toxicity',
                component: ComponentCreator('/docs/concepts/mixture-toxicity', '9b1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/model-validation',
                component: ComponentCreator('/docs/concepts/model-validation', '4f6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/molecular-descriptors',
                component: ComponentCreator('/docs/concepts/molecular-descriptors', 'ccb'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/nam-standardization',
                component: ComponentCreator('/docs/concepts/nam-standardization', 'edf'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/nam-validation',
                component: ComponentCreator('/docs/concepts/nam-validation', '096'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/nams-integration',
                component: ComponentCreator('/docs/concepts/nams-integration', '5cc'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/new-approach-methodologies',
                component: ComponentCreator('/docs/concepts/new-approach-methodologies', '649'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/ngra',
                component: ComponentCreator('/docs/concepts/ngra', 'f41'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/non-animal-approaches',
                component: ComponentCreator('/docs/concepts/non-animal-approaches', '1b7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/pbpk-modeling',
                component: ComponentCreator('/docs/concepts/pbpk-modeling', '597'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/qivive',
                component: ComponentCreator('/docs/concepts/qivive', '17a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/qsar',
                component: ComponentCreator('/docs/concepts/qsar', '9ab'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/quantitative-adverse-outcome-pathways',
                component: ComponentCreator('/docs/concepts/quantitative-adverse-outcome-pathways', '0f7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/reach-framework',
                component: ComponentCreator('/docs/concepts/reach-framework', '965'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/read-across',
                component: ComponentCreator('/docs/concepts/read-across', '744'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/regulatory-frameworks-nams',
                component: ComponentCreator('/docs/concepts/regulatory-frameworks-nams', '096'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/regulatory-initiatives',
                component: ComponentCreator('/docs/concepts/regulatory-initiatives', '17b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/regulatory-toxicology',
                component: ComponentCreator('/docs/concepts/regulatory-toxicology', '210'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/risk',
                component: ComponentCreator('/docs/concepts/risk', '13b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/tiered-approach-chemical-safety',
                component: ComponentCreator('/docs/concepts/tiered-approach-chemical-safety', '1dc'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/toxicological-endpoint',
                component: ComponentCreator('/docs/concepts/toxicological-endpoint', 'b39'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/uncertainty',
                component: ComponentCreator('/docs/concepts/uncertainty', '2c2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/concepts/weight-of-evidence',
                component: ComponentCreator('/docs/concepts/weight-of-evidence', '7a7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/datasets/comparative-toxicogenomics-database',
                component: ComponentCreator('/docs/datasets/comparative-toxicogenomics-database', '11a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/datasets/comptox-chemicals-dashboard',
                component: ComponentCreator('/docs/datasets/comptox-chemicals-dashboard', 'd16'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/datasets/pubchem-bioassay',
                component: ComponentCreator('/docs/datasets/pubchem-bioassay', 'da1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/datasets/quantitative-adverse-outcome-pathways-data',
                component: ComponentCreator('/docs/datasets/quantitative-adverse-outcome-pathways-data', '14d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/datasets/tox21',
                component: ComponentCreator('/docs/datasets/tox21', '828'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/datasets/toxcast',
                component: ComponentCreator('/docs/datasets/toxcast', 'e0c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/carcinogenicity',
                component: ComponentCreator('/docs/endpoints/carcinogenicity', '51d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/cardiotoxicity',
                component: ComponentCreator('/docs/endpoints/cardiotoxicity', '536'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/developmental-toxicity',
                component: ComponentCreator('/docs/endpoints/developmental-toxicity', '3a6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/endocrine-disruption',
                component: ComponentCreator('/docs/endpoints/endocrine-disruption', '6dd'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/genotoxicity',
                component: ComponentCreator('/docs/endpoints/genotoxicity', '399'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/hepatotoxicity',
                component: ComponentCreator('/docs/endpoints/hepatotoxicity', '6fb'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/mitochondrial-toxicity',
                component: ComponentCreator('/docs/endpoints/mitochondrial-toxicity', '71d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/neurotoxicity',
                component: ComponentCreator('/docs/endpoints/neurotoxicity', '58d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/reproductive-toxicity',
                component: ComponentCreator('/docs/endpoints/reproductive-toxicity', '51f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/endpoints/skin-sensitization',
                component: ComponentCreator('/docs/endpoints/skin-sensitization', '76e'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/evidence/ev-chem-databases-2024',
                component: ComponentCreator('/docs/evidence/ev-chem-databases-2024', 'd96'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/evidence/ev-ml-algorithms-2024',
                component: ComponentCreator('/docs/evidence/ev-ml-algorithms-2024', 'a94'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/evidence/ev-molecular-descriptors-2024',
                component: ComponentCreator('/docs/evidence/ev-molecular-descriptors-2024', '493'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/glossary/acronyms',
                component: ComponentCreator('/docs/glossary/acronyms', '624'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/glossary/glossary',
                component: ComponentCreator('/docs/glossary/glossary', '7e7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/glossary/identifier-systems',
                component: ComponentCreator('/docs/glossary/identifier-systems', 'e3d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/glossary/ontology-crosswalks',
                component: ComponentCreator('/docs/glossary/ontology-crosswalks', 'b7c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/assay-index',
                component: ComponentCreator('/docs/indices/assay-index', '13c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/chemical-index',
                component: ComponentCreator('/docs/indices/chemical-index', '0e9'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/dataset-index',
                component: ComponentCreator('/docs/indices/dataset-index', '8ce'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/endpoint-index',
                component: ComponentCreator('/docs/indices/endpoint-index', 'dcd'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/evidence-claim-index',
                component: ComponentCreator('/docs/indices/evidence-claim-index', '33b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/master-index',
                component: ComponentCreator('/docs/indices/master-index', 'a08'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/model-index',
                component: ComponentCreator('/docs/indices/model-index', 'c6f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/indices/workflow-index',
                component: ComponentCreator('/docs/indices/workflow-index', '754'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/aop-multifaceted-framework-2018',
                component: ComponentCreator('/docs/literature/aop-multifaceted-framework-2018', '5ba'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/assessment_of_performance_of_profilers_oecd_qsar_toolbox',
                component: ComponentCreator('/docs/literature/assessment_of_performance_of_profilers_oecd_qsar_toolbox', '3eb'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/big-data-predictive-toxicology-2026',
                component: ComponentCreator('/docs/literature/big-data-predictive-toxicology-2026', '5fe'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/bpa-mechanisms-2025',
                component: ComponentCreator('/docs/literature/bpa-mechanisms-2025', '321'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/deeptox-2015',
                component: ComponentCreator('/docs/literature/deeptox-2015', '832'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/differential-estrogenic-actions-2012',
                component: ComponentCreator('/docs/literature/differential-estrogenic-actions-2012', '902'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/ecetoc-wr-38-qao-workshop',
                component: ComponentCreator('/docs/literature/ecetoc-wr-38-qao-workshop', '405'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/framework-reach-2022',
                component: ComponentCreator('/docs/literature/framework-reach-2022', '5f4'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/good-read-across-practices-2025',
                component: ComponentCreator('/docs/literature/good-read-across-practices-2025', 'bc1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/guidance-on-the-use-of-read-across-for-chemical-safety-assessment-in-food-and-feed',
                component: ComponentCreator('/docs/literature/guidance-on-the-use-of-read-across-for-chemical-safety-assessment-in-food-and-feed', '9e7'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/ivive-pbpk-interface-2022',
                component: ComponentCreator('/docs/literature/ivive-pbpk-interface-2022', '7c3'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/ivive-review-2024',
                component: ComponentCreator('/docs/literature/ivive-review-2024', '79c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/machine-learning-chemoinformatics-2024',
                component: ComponentCreator('/docs/literature/machine-learning-chemoinformatics-2024', '08a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/nam-regulatory-toxicology-2023',
                component: ComponentCreator('/docs/literature/nam-regulatory-toxicology-2023', 'd7a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/omics-mixtures-toxicogenomics-2019',
                component: ComponentCreator('/docs/literature/omics-mixtures-toxicogenomics-2019', '406'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/optimal-ml-algorithms-toxicity-2025',
                component: ComponentCreator('/docs/literature/optimal-ml-algorithms-toxicity-2025', '541'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/pbpk-nam-risk-assessment-2026',
                component: ComponentCreator('/docs/literature/pbpk-nam-risk-assessment-2026', '41d'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/qsar-workflow-2024',
                component: ComponentCreator('/docs/literature/qsar-workflow-2024', '6d5'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/literature/standardizing-benchmark-dose-2014',
                component: ComponentCreator('/docs/literature/standardizing-benchmark-dose-2014', '095'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/big-data-toxicology',
                component: ComponentCreator('/docs/models-and-methods/big-data-toxicology', '59a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/challenges-omics-methods',
                component: ComponentCreator('/docs/models-and-methods/challenges-omics-methods', 'b49'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/computational-tools-toxicology',
                component: ComponentCreator('/docs/models-and-methods/computational-tools-toxicology', '49b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/data-integration-challenges',
                component: ComponentCreator('/docs/models-and-methods/data-integration-challenges', '180'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/data-integration-toxicology',
                component: ComponentCreator('/docs/models-and-methods/data-integration-toxicology', '9c1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/data-quality-toxicology',
                component: ComponentCreator('/docs/models-and-methods/data-quality-toxicology', '6a4'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/data-scarce-to-data-rich',
                component: ComponentCreator('/docs/models-and-methods/data-scarce-to-data-rich', 'e84'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/data-visualization-toxicology',
                component: ComponentCreator('/docs/models-and-methods/data-visualization-toxicology', '955'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/deeptox',
                component: ComponentCreator('/docs/models-and-methods/deeptox', '95f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/echra-raaf',
                component: ComponentCreator('/docs/models-and-methods/echra-raaf', '837'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/efsa-2025-guidance',
                component: ComponentCreator('/docs/models-and-methods/efsa-2025-guidance', '895'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/efsa-read-across-requirements',
                component: ComponentCreator('/docs/models-and-methods/efsa-read-across-requirements', '6e0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/explainable-ai',
                component: ComponentCreator('/docs/models-and-methods/explainable-ai', '1cd'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/future-directions-ivive',
                component: ComponentCreator('/docs/models-and-methods/future-directions-ivive', '267'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/genomics-toxicology',
                component: ComponentCreator('/docs/models-and-methods/genomics-toxicology', 'ec6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/grap-principles',
                component: ComponentCreator('/docs/models-and-methods/grap-principles', 'f73'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/ivive',
                component: ComponentCreator('/docs/models-and-methods/ivive', '529'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/ivive-limitations',
                component: ComponentCreator('/docs/models-and-methods/ivive-limitations', '4d6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/knime',
                component: ComponentCreator('/docs/models-and-methods/knime', 'f05'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/laboratory-automation-toxicology',
                component: ComponentCreator('/docs/models-and-methods/laboratory-automation-toxicology', '6cc'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/ml-in-toxicology',
                component: ComponentCreator('/docs/models-and-methods/ml-in-toxicology', '909'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/molecular-fingerprints',
                component: ComponentCreator('/docs/models-and-methods/molecular-fingerprints', '5e2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/omics-technologies-toxicology',
                component: ComponentCreator('/docs/models-and-methods/omics-technologies-toxicology', '11a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/opera-models',
                component: ComponentCreator('/docs/models-and-methods/opera-models', 'a0c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/pbtk-models',
                component: ComponentCreator('/docs/models-and-methods/pbtk-models', 'c13'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/proteomics-toxicology',
                component: ComponentCreator('/docs/models-and-methods/proteomics-toxicology', '9cc'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/quantitative-adverse-outcome-pathways-modeling',
                component: ComponentCreator('/docs/models-and-methods/quantitative-adverse-outcome-pathways-modeling', '372'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-analogue-approach',
                component: ComponentCreator('/docs/models-and-methods/read-across-analogue-approach', '07b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-category-approach',
                component: ComponentCreator('/docs/models-and-methods/read-across-category-approach', '8a9'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-data-gap-filling',
                component: ComponentCreator('/docs/models-and-methods/read-across-data-gap-filling', '400'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-methods',
                component: ComponentCreator('/docs/models-and-methods/read-across-methods', '2e4'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-regulatory-acceptability',
                component: ComponentCreator('/docs/models-and-methods/read-across-regulatory-acceptability', '6af'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-regulatory-applications',
                component: ComponentCreator('/docs/models-and-methods/read-across-regulatory-applications', '721'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/read-across-workflow',
                component: ComponentCreator('/docs/models-and-methods/read-across-workflow', '80b'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/systems-toxicology',
                component: ComponentCreator('/docs/models-and-methods/systems-toxicology', 'ee9'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models-and-methods/transcriptomics-toxicology',
                component: ComponentCreator('/docs/models-and-methods/transcriptomics-toxicology', '122'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models/benchmark-dose-modeling',
                component: ComponentCreator('/docs/models/benchmark-dose-modeling', 'ebe'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models/oecd-qsar-toolbox',
                component: ComponentCreator('/docs/models/oecd-qsar-toolbox', '68a'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models/points-of-departure',
                component: ComponentCreator('/docs/models/points-of-departure', '9a8'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/models/structural-alerts',
                component: ComponentCreator('/docs/models/structural-alerts', '21f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/biosecurity-and-dual-use-considerations',
                component: ComponentCreator('/docs/quality/biosecurity-and-dual-use-considerations', '8f1'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/dataset-quality-standard',
                component: ComponentCreator('/docs/quality/dataset-quality-standard', '83e'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/deprecation-policy',
                component: ComponentCreator('/docs/quality/deprecation-policy', '0f3'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/evidence-standards',
                component: ComponentCreator('/docs/quality/evidence-standards', '643'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/human-review-checkpoints',
                component: ComponentCreator('/docs/quality/human-review-checkpoints', '5f2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/model-validation-standard',
                component: ComponentCreator('/docs/quality/model-validation-standard', 'c77'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/regulatory-interpretation-disclaimer',
                component: ComponentCreator('/docs/quality/regulatory-interpretation-disclaimer', '3fc'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/study-quality-assessment-rubric',
                component: ComponentCreator('/docs/quality/study-quality-assessment-rubric', '7bb'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/uncertainty-representation',
                component: ComponentCreator('/docs/quality/uncertainty-representation', 'ecf'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/uncertainty-representation-standard',
                component: ComponentCreator('/docs/quality/uncertainty-representation-standard', '357'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/quality/versioning-and-audit-policy',
                component: ComponentCreator('/docs/quality/versioning-and-audit-policy', '619'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/agent-roles-and-capabilities',
                component: ComponentCreator('/docs/system/agent-roles-and-capabilities', '12c'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/citation-and-provenance-rules',
                component: ComponentCreator('/docs/system/citation-and-provenance-rules', '9f3'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/computational-toxicology-system-overview',
                component: ComponentCreator('/docs/system/computational-toxicology-system-overview', '2c0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/knowledge-representation-principles',
                component: ComponentCreator('/docs/system/knowledge-representation-principles', '954'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/known-limitations-of-the-wiki',
                component: ComponentCreator('/docs/system/known-limitations-of-the-wiki', 'b20'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/ontology-alignment-policy',
                component: ComponentCreator('/docs/system/ontology-alignment-policy', '740'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/responsible-use-policy',
                component: ComponentCreator('/docs/system/responsible-use-policy', 'd28'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/update-and-review-policy',
                component: ComponentCreator('/docs/system/update-and-review-policy', '09f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/wiki-mission-and-scope',
                component: ComponentCreator('/docs/system/wiki-mission-and-scope', 'ec3'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/system/wiki-operation-summary-20260808',
                component: ComponentCreator('/docs/system/wiki-operation-summary-20260808', '5ee'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/toxicological-endpoints/toxicity-endpoints',
                component: ComponentCreator('/docs/toxicological-endpoints/toxicity-endpoints', 'e7f'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/verification_reports/2026-08-08-nam-regulatory-toxicology-verification',
                component: ComponentCreator('/docs/verification_reports/2026-08-08-nam-regulatory-toxicology-verification', '9b6'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/verification_reports/2026-08-08-nam-verification-summary',
                component: ComponentCreator('/docs/verification_reports/2026-08-08-nam-verification-summary', 'c32'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/verification_reports/2026-08-08-verification-completion-summary',
                component: ComponentCreator('/docs/verification_reports/2026-08-08-verification-completion-summary', '158'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/verification_reports/verification_report_2026-08-08',
                component: ComponentCreator('/docs/verification_reports/verification_report_2026-08-08', '27e'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/aop-development-workflow',
                component: ComponentCreator('/docs/workflows/aop-development-workflow', '250'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/chemical-hazard-assessment-workflow',
                component: ComponentCreator('/docs/workflows/chemical-hazard-assessment-workflow', '935'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/contradiction-resolution-workflow',
                component: ComponentCreator('/docs/workflows/contradiction-resolution-workflow', 'feb'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/dataset-profiling-workflow',
                component: ComponentCreator('/docs/workflows/dataset-profiling-workflow', '4c3'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/evidence-extraction-workflow',
                component: ComponentCreator('/docs/workflows/evidence-extraction-workflow', '5b2'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/evidence-synthesis-workflow',
                component: ComponentCreator('/docs/workflows/evidence-synthesis-workflow', 'd85'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/human-review-escalation-workflow',
                component: ComponentCreator('/docs/workflows/human-review-escalation-workflow', 'a36'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/knowledge-graph-update-workflow',
                component: ComponentCreator('/docs/workflows/knowledge-graph-update-workflow', '1b9'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/literature-review-workflow',
                component: ComponentCreator('/docs/workflows/literature-review-workflow', '3ba'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/molecular-docking-workflow',
                component: ComponentCreator('/docs/workflows/molecular-docking-workflow', '193'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/profiler-improvement',
                component: ComponentCreator('/docs/workflows/profiler-improvement', '1c0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/qsar-prediction-workflow',
                component: ComponentCreator('/docs/workflows/qsar-prediction-workflow', 'cd0'),
                exact: true,
                sidebar: "wikiSidebar"
              },
              {
                path: '/docs/workflows/quantitative-adverse-outcome-pathways-implementation',
                component: ComponentCreator('/docs/workflows/quantitative-adverse-outcome-pathways-implementation', '8b2'),
                exact: true,
                sidebar: "wikiSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
