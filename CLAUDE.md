# Repo rules

- **Whenever an agent adds or updates a file in `artifacts/`, regenerate
  `artifacts/index.json` in the same commit.** Run
  `python3 scripts/generate_artifacts_index.py` before committing. The
  index is generated from each artifact's frontmatter (`slug`, `title`,
  `description`, `updated`, `status`) — a new or edited artifact needs
  that frontmatter block, or it will be skipped with a warning instead of
  appearing in the index.
