from textwrap import indent
from urllib import response
import requests
import base64
import json
from . import crud
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import render
import requests
import spotipy


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
          resobj = res.json()
          print(json.dumps(resobj, indent=2))


          token = resobj['access_token']
         
          playlistId = "299wK8hR8BjBO8o8eCKRzQ?si=abf068dbebdd43ae"
          playlistEndPoint=  f"https://api.spotify.com/v1/playlists/{playlistId}"
          
          getheaders = {
                    "Authorization": "Bearer " + token}

          res1 = requests.get(playlistEndPoint,headers=getheaders)
          res1obj =res1.json()
          #print(json.dumps(res1obj,indent=2))
          for t in res1obj['tracks']['items']:
               print('------------------------')
               for a in t['track']['artists']:
                    print(a['name'])
               
               songname = t['track']['name']
               print(songname)

          scope = 'playlist-modify-public'
          username = 'pfr6uz5l4q497psinbbn4zt09'

          token = SpotifyOAuth(scope=scope,username= username,client_id='21c2202ac97246a1b6b447b700da337c',client_secret='cd9e627234cd4509905cfe3d305d9034',redirect_uri='http://127.0.0.1:8000/')
          spotifyObject = spotipy.Spotify(auth_manager= token)

          playlist_name = 'SUPRIYA NEWLIST'
          playlist_desc ='SFFSFSFSF'
          spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_desc)

     
     return render(request,'home.html')


def create_playlist_on_spotify(name, public,token):
     response = requests.post(
          SPOTIFY_CREATE_PLAYLIST_URL,
          headers={
               "Authorization": f"Bearer {token}"
          },
          json={
               "name": name,
               "public": public
          }
     )
     json_resp = response.json()
     return json_resp
''' playlistId = "https://open.spotify.com/playlist/5uy0FokyDyuWyqdjiwZsEH?si=bea5fa366ab34161"
          playlistEndPoint= f"https://api.spotify.com/v1/playlists/{playlistId}"

          getheaders = {
                    "Authorization": "Bearer " + token}

          res = requests.post(url=playlistEndPoint,headers=getheaders)'''
        