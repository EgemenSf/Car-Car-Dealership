import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()

# Import models from sales_rest, here.
# from sales_rest.models import Something
from sales_rest.models import AutomobileVO

def get_automobiles():
    automobile_api_url = "http://project-beta-inventory-api-1:8000/api/automobiles/"
    response = requests.get(automobile_api_url)
    if response.status_code == 200:
        return response.json().get('autos', [])
    else:
        print(f"Error: Status Code {response.status_code}")
        return []

def update_automobile_vo(automobile_data):
    for auto in automobile_data:
        vin = auto.get("vin")
        sold = auto.get("sold")
        AutomobileVO.objects.update_or_create(vin=vin, defaults={"sold": sold})




def poll(repeat=True):
    while True:
        print('Sales poller polling for data')
        try:
            automobiles = get_automobiles()
            update_automobile_vo(automobiles)
        except Exception as e:
            print(e, file=sys.stderr)

        if (not repeat):
            break

        time.sleep(60)


if __name__ == "__main__":
    poll()
