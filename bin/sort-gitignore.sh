#!/usr/bin/env bash
export LC_ALL=C

cat <<EOF 1>&2
DEPRECATION WARNING: sort-gitignore is deprecated. Use:

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: file-contents-sorter
        files: .gitignore
EOF

exit 1
