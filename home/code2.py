
SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/supriya/playlists'
ACCESS_TOKEN = 'BQDD_2oxhwmsvKszhngKrH-cKanl56kvvRI3iR0-F5svG0hXA5TOW0S8T-hZVvlmsxU2dTlHnsC-lPrpgdxcIuqNkchm863JLqHR_4fiat0-CYGW7Zzymbrt-JgRpSTQDtSDNakMkizO0YnrdSI39CKt6QIbH0bP2OcwXBK0Ik5bavUZX5JR7k2sWFT3qQpJZkMMZP3oN-6979-DZpiIqury-Gvlt0vJM1TpABa4-pll1ouCOQ47660DTWUw'

def home(request):
  
     if request.method == 'POST':
          playlist = create_playlist_on_spotify(
          name = 'My new playlist 22/9',
          public=False
         )
     
          print(f"Playlist", playlist)
     return render(request, "home.html")

def create_playlist_on_spotify(name, public):
     response = requests.post(
          SPOTIFY_CREATE_PLAYLIST_URL,
          headers={
               "Authorization": f"Bearer {ACCESS_TOKEN}"
          },
          json={
               "name": name,
               "public": public
          }
     )
     json_resp = response.json()
     return json_resp



