from urllib import response
import requests
import base64
import json
from . import crud
from django.shortcuts import render
import requests

authurl = "https://accounts.spotify.com/api/token"
autoheader = {}
authdata = {}
client_id='21c2202ac97246a1b6b447b700da337c'
client_secret='cd9e627234cd4509905cfe3d305d9034' 

def home(request):
     if request.method == 'POST':
          message = f"{client_id}:{client_secret}"
          messageBytes = message.encode('ascii')
          base64Bytes = base64.b64encode(messageBytes)
          base64Message = base64Bytes.decode('ascii')

          
          autoheader['Authorization'] = f"Basic {base64Message}"
          authdata['grant_type'] = "client_credentials"

          res = requests.post(authurl, headers=autoheader, data=authdata)
          responseObject = res.json()
          print(json.dumps(res.json(), indent=2))
          
          accesstoken = responseObject['access_token']

          print(accesstoken)

     return render(request,'home.html') 

