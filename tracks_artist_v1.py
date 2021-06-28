#!/usr/bin/env python

import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(
        username=USERNAME,
        scope='user-library-read user-top-read',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
	tracks = sp.current_user_top_tracks(time_range=sp_range, limit=50)
	artist = sp.current_user_top_artists(time_range=sp_range, limit=50)

	if sp_range == "short_term":
		print("Top Tracks last 4 Weeks\n")
	elif sp_range == "medium_term":
		print("\n\nTop Tracks last 6 months\n")
	elif sp_range == "long_term":
		print("\n\nTop Tracks All Time\n")

	for i, x in enumerate(tracks['items']):	
			
		if sp_range == "long_term": #spotify doesn't keep more than 50 values in spotipy database, top two were rain songs to sleep to
			if "Rain" not in x["name"]:
				print(str(i-1)+'.', x['name'], '-', x['artists'][0]['name']) #values are from JSON file
		else:
			print(str(i+1)+'.', x['name'], '-', x['artists'][0]['name'])

	if sp_range == "short_term":
		print("\n\nTop Artists last 4 Weeks\n")
	elif sp_range == "medium_term":
		print("\n\nTop Artists last 6 months\n")
	elif sp_range == "long_term":
		print("\n\nTop Artists All Time\n")

	for i, x in enumerate(artist['items']):
		print(str(i+1)+'.', x['name'])

