import requests
import time

url = "https://gmail.googleapis.com"
max_retries = 3
retry_delay = 1  # seconds

for i in range(max_retries):
    response = requests.get('https://gmail.googleapis.com')
    if response.status_code == 200:
        print("Successfull: status code is 200")
        break
    else:
        print("Error: Request failed with status code", response.status_code)
        if i < max_retries - 1:
            print("Retrying in {} seconds...".format(retry_delay))
            time.sleep(retry_delay)
