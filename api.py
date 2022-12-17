import requests
from request import  *

class XenForoAPI:
    def __init__(self, key: str, url: str) -> None:
        session = requests.sessions.Session()
        session.headers.update({'XF-Api-Key': key})
        if not url[-1] == "/":
            url = url + "/"

        self.url = url
        self.session = session

    def connect(self, session:requests.get, url:str, params={}):
        url = self.url + url + "/"
        request = session(url, params=params)
        
        try:    json = request.json()
        except: return Error({"request":request, "code":request.status_code})
        
        json.update({"request":request, "code":request.status_code})

        return json


    def get_me(self) -> GetME | Error:
        request = self.connect(self.session.get, "me")
        if type(request) == type(Error):
            return request
        
        return GetME(**request)