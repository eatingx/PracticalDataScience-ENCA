import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv


#Authentication
with open("./Spotifyid.txt") as f:
    id_info = f.readlines()
    cid = id_info[0][0:-1]
    secret = id_info[1]

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp"
playlist_URI = playlist_link.split("/")[4].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

data=[]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name = track["track"]["name"]
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]

    #Album
    album = track["track"]["album"]["name"]
   
    #Popularity of the track
    track_pop = track["track"]["popularity"]

    data.append([artist_name, artist_pop, artist_genres,album])

    
    #print(artist_name, artist_pop, artist_genres,album)
file_header=["Artist Name", "Artist Popularity", "Artist Genres","Album Name"]
with open ("./Top50_USA.csv","w", newline='') as file:
    writer=csv.writer(file)
    writer.writerow(file_header)
    writer.writerows(data)

if __name__ == "__main__":
    sp.audio_features(track_uri)[0]