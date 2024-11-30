import requests

class Bearer_auth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, request):
        request.headers["authorization"] = "Bearer " + self.token
        return request