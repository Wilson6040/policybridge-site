# Phase 07 — PolicyBridge Wording Studio Audit / Rebuild Prompt — COMPLETION NOTE
Status: COMPLETE
Output: PolicyBridge_Wording_Studio_Audit_Rebuild_Prompt.docx (+PDF)

- A ready-to-paste prompt for Emergent/Opus to audit and (safely) upgrade PolicyBridge so it can replicate the Phase 06 workflow.
- Current-state finding included: the present app is a 'Document Centre' (FastAPI serves a static documents list + download endpoints; React list/download UI). It does NOT ingest wordings, parse clauses, compare, generate redlines, or run accept/reject — so it serves outputs, it does not yet produce them.
- Prompt enforces: discovery first; no destructive changes; no data deletion; no schema changes without review; do not break existing functionality; use the seven TMHCC documents as a test project; final QA report + screenshots + sample outputs.
- Includes the ten audit checks and the product standard (definition of done).
Assumptions/blockers: none.
