
def post(apikey, body, ip, port, ext_url):
    import requests
    from auth import Bearer_auth

    base_url = f"https://{ip}:{port}/api/v2"
    exturl = ext_url
    url = f"{base_url}/{exturl}"
    headers = { "Content-Type": "application/json" }

    response = requests.post(url, headers=headers, json=body, auth=Bearer_auth(apikey), verify=False)

    if response.status_code == 200:
        data = response.json()
        return(data)
    else:
        return(response.status_code)
    
def get(apikey, ip, port, ext_url):
    import requests
    from auth import Bearer_auth

    base_url = f"https://{ip}:{port}/api/v2"
    exturl = ext_url
    url = f"{base_url}/{exturl}"
    headers = { "Content-Type": "application/json" }

    response = requests.get(url, headers=headers, auth=Bearer_auth(apikey), verify=False)

    if response.status_code == 200:
        data = response.json()
        return(data)
    else:
        return(response.status_code)
    
def put(apikey, body, ip, port, ext_url):
    import requests
    from auth import Bearer_auth

    base_url = f"https://{ip}:{port}/api/v2"
    exturl = ext_url
    url = f"{base_url}/{exturl}"
    headers = { "Content-Type": "application/json" }

    response = requests.put(url, headers=headers, json=body, auth=Bearer_auth(apikey), verify=False)

    if response.status_code == 200:
        data = response.json()
        return(data)
    else:
        return(response.status_code)
    
def delete(apikey, ip, port, ext_url, unames):
    import requests
    from auth import Bearer_auth

    base_url = f"https://{ip}:{port}/api/v2"
    exturl = ext_url
    url = f"{base_url}/{exturl}"
    headers = { "Content-Type": "application/json" }
    names = unames


    for name in names:
        url = f"{base_url}/{exturl}/{name}"
        response = requests.delete(url, headers=headers, auth=Bearer_auth(apikey), verify=False)
        if response.status_code == 200:
            print(f"User {name} deleted successfully")
        else:
            print("API request failed with status code:", response.status_code)
