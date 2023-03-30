import requests
from datetime import datetime
import os
import json



endpoint = "http://localhost:8000/api/bond/"


data_file = f"{os.path.dirname(os.path.realpath(__file__))}/../bondscanner/data/bond_data.txt"


with open(data_file) as f:
    for link in f:
        try:

            data = json.loads(link)
        
            get_response = requests.post(endpoint, data)
        except Exception as e:
            continue

