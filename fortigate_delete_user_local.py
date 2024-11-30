from fgt_api_base import delete
import os

apikey = os.environ.get('APIKEY')
ip = "192.168.74.1"
port = 8443
ext_url = "cmdb/user/local"
headers = { "Content-Type": "application/json" }

unames = ["testuser2"]


response = delete(apikey, ip, port, ext_url, unames)

print(response)