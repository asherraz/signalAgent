# Repo rules

- **Whenever an agent adds or updates a file in `artifacts/`, regenerate
  `artifacts/index.json` in the same commit.** Run
  `python3 scripts/generate_artifacts_index.py` before committing. The
  index is generated from each artifact's frontmatter (`slug`, `title`,
  `description`, `updated`, `status`) — a new or edited artifact needs
  that frontmatter block, or it will be skipped with a warning instead of
  appearing in the index.
- **Every agent appends its run to `artifacts/runs.json` in the same
  commit.** One record per run — `date`, `agent`, `summary`, `outcome`,
  and `artifact` (the artifact's slug, or `null` if the run produced no
  public artifact) — added newest-first. These entries are public: no
  asset names, holder/company names, or other confidential detail
  belongs in the summary or outcome, even when the underlying artifact
  itself is a private working document excluded from `index.json`.
