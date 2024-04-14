# Based off https://www.youtube.com/watch?v=c5sWvP9h3s8

import requests



SPOTIFY_CREATE_PLAYLISTS_URL = 'https://api.spotify.com/v1/users/hybrid1287/playlists' 
ACCESS_TOKEN = '' # Need to generate

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLISTS_URL,
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json = {
            "name": name, # Currently defined within file. Maybe later update to be command line arg?
            "public": public # Same idea here.
            # TODO: Maybe add more, like songs to be in playlist?
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name = "My Private Playlist",
        public = False
    )
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()