import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt


load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))

taylor = "06HL4z0CvFAxyc27GXpf02"

top10 = con.artist_top_tracks(taylor)

tracks = []
for track in top10['tracks']:
    track_data = {
        'Track Name': track['name'],
        'Popularity': track['popularity'],
        'Duration': track['duration_ms'],
    }
    tracks.append(track_data)

df = pd.DataFrame(tracks)



scatter_plot = plt.scatter(df['Popularity'], df['Duration'])
plt.xlabel('Popularity')
plt.ylabel('Duration')
plt.title('Track Popularity vs. Duration')
plt.savefig('scatter_plot.png')