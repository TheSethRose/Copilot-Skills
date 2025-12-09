---
description: Auto-loaded context from Kit analysis (symbols, file tree, dependencies)
applyTo: "**"
---

# Kit Codebase Analysis

This codebase is analyzed by [Kit](https://kit.cased.com/), which provides pre-computed indexes for symbols, files, and dependencies.

## 📂 Analysis Files

The following analysis files are available in `.kit-analysis/`:

- **`symbols.json`**: Complete list of functions, classes, and methods with their file locations and line numbers.
  - Use this to find where a symbol is defined without searching the whole repo.
  - Format: `[{"name": "...", "kind": "...", "file": "...", "line": ...}, ...]`

- **`file_tree.json`**: Full directory structure of the repository.
  - Use this to understand the project layout.

- **`summary.md`**: High-level statistics and top files.

## 🤖 How to Use

1. **Symbol Lookup**: If you need to find a function or class, read `.kit-analysis/symbols.json` first. It is much faster than `grep` or `find`.
2. **Project Structure**: Read `.kit-analysis/file_tree.json` to see all files.
3. **Context Gathering**: When asked to "understand the codebase", start by reading `.kit-analysis/summary.md`.

## 🔄 Updates

These files are updated automatically. If you make significant changes (refactoring, adding many files), you can request a refresh by running:
`uv run --with cased-kit python .github/scripts/kit/bootstrap.py`
