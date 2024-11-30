from fgt_api_base import post
import os

apikey = os.environ.get('APIKEY')
ip = "192.168.74.1"
port = 8443
ext_url = "cmdb/user/local"
headers = { "Content-Type": "application/json" }
body = {
  "name": "testuser2",
  "status": "enable",
  "type": "password",
  "passwd": "Fortinet123!",
  "two-factor": "disable",
  "authtimeout": 1440,
  "auth-concurrent-value": 100,
  "username-sensitivity": "disable"
}


response = post(apikey, body, ip, port, ext_url)

print(response)