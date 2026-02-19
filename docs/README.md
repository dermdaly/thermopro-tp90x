# Sphinx Documentation for ThermoPro TP90x

This directory contains Sphinx documentation for the ThermoPro TP90x library.

## Building Documentation Locally

### Prerequisites

```bash
pip install -r requirements.txt
```

### Build HTML Documentation

```bash
cd docs
make html
```

Generated docs in `build/html/index.html`.

### Clean Build

```bash
make clean
```

## Configuration

- `source/conf.py` - Sphinx configuration
- `source/index.rst` - Main documentation index
- `source/api/` - API reference pages

## Docstring Format

Uses reStructuredText format (parsed natively by Sphinx).
