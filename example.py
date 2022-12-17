from api import *

api = XenForoAPI("API-Key", "https://forum.example.com/api")

t = api.get_me()
print(t.about)