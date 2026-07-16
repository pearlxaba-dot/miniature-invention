"""
Fetch economic datasets from Statistics South Africa (Stats SA)
"""

import requests
import json
from datetime import datetime

def fetch_stats_data():
    """
    Fetch data from Stats SA API or data source.
    Update the URL below with the actual Stats SA data endpoint.
    """
    
    # Example: Replace with actual Stats SA API endpoint
    # Reference: http://www.statssa.gov.za/ for available datasets
    
    url = "https://api.github.com/repos/pearlxaba-dot/miniature-invention"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Successfully retrieved data at {datetime.now().isoformat()}")
            print(f"  Repository: {data.get('full_name')}")
            print(f"  Description: {data.get('description')}")
            return data
        else:
            print(f"✗ Failed to retrieve data. Status code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching data: {e}")
        return None

def save_stats_data(data, filename="stats_data.json"):
    """
    Save fetched data to a JSON file.
    """
    if data:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✓ Data saved to {filename}")

if __name__ == "__main__":
    print("Fetching Stats SA economic datasets...")
    stats_data = fetch_stats_data()
    
    if stats_data:
        save_stats_data(stats_data)
