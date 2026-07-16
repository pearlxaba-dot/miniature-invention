import requests
import base64

name: Process Public Stats
on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * *' # Optional: Runs automatically every day at midnight

jobs:
  run-stats-script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install requests

      - name: Run Stats Script
        run: python your_script_name.py



