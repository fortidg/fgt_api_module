from fgt_api_base import get
import os

apikey = os.environ.get('APIKEY')
ip = "192.168.74.1"
port = 8443
ext_url = "monitor/system/current-admins"
headers = { "Content-Type": "application/json" }


response = get(apikey, ip, port, ext_url)

#print(type(response))

# If the API request was successful, print the admin name and session ID
if type(response) != int:
    results = response.get("results")
    for result in results:
        id = result.get("id")
        admin_user = result.get("admin")
        print("Admin Name:", admin_user)
        print("Session ID:", id)
        print()
else:
    print("API request failed with status code:", response)
