#
#
from config_env import get_base_url

import requests

def main():
    base_url = get_base_url()
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            print("API aktif:" response.status_code)
        else:
            print("gagal:", response.status_code)
    except Exception as e:
        print("Konekasi gagal:", e)
        
if__name__ == "__main___":
    main()