# miniature-invention

Stats SA economic datasets

A Python project for retrieving and processing South African economic data from Statistics South Africa.

## Overview

This repository contains scripts and workflows to automatically fetch and process economic datasets from Stats SA.

## Requirements

- Python 3.10+
- `requests` library

## Installation

```bash
pip install requests
```

## Usage

Run the main script to fetch Stats SA data:

```bash
python fetch_stats.py
```

## Automated Processing

This repository includes a GitHub Actions workflow that automatically runs the stats script:
- **Trigger**: On every push to `main` branch
- **Schedule**: Optionally runs daily at midnight UTC

See `.github/workflows/process-stats.yml` for workflow configuration.

## License

MIT

## Author

pearlxaba-dot
