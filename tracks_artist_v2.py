#!/usr/bin/env python

#original program, simplified in v1 to include less for loops

import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(
        username=USERNAME,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

shortTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
print("Top Songs last 4 Weeks\n")
for i, x in enumerate(shortTracks['items']):
	print(str(i+1)+'.', x['name'], '-', x['artists'][0]['name'])


shortArtists = sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')
print("\n\nTop Artists last 4 Weeks\n")
for i, x in enumerate(shortArtists['items']):
        print(str(i+1)+'.', x['name'])


medTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
print("\n\nTop Songs last 6 Months\n")
for i, x in enumerate(medTracks['items']):
	print(str(i+1)+'.', x['name'], '-', x['artists'][0]['name'])


medArtists = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
print("\n\nTop Artists last 6 Months\n")
for i, x in enumerate(medArtists['items']):
        print(str(i+1)+'.', x['name'])


longTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
print("\n\nTop Songs All Time\n") #spotify doesn't keep more than 50 values in spotipy database, top two were rain songs to sleep to
for i, x in enumerate(longTracks['items']):
	if "Rain" not in x["name"]: 
		print(str(i-1)+'.', x['name'], '-', x['artists'][0]['name'])

longArtists = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
print("\n\nTop Artists All Time\n")
for i, x in enumerate(longArtists['items']):
        print(str(i+1)+'.', x['name'])

"""

							      TRIAL AND ERRORS

      formating the JSON data was the most challenging part. 

print(json.dumps(tracks, indent=3)) # dumped the data to get a better view of how to format. 

print("Top 10 tracks - Short Term (4 weeks)\n")
tracks = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')
for i, x in enumerate(tracks['items']):
	print(str(i+1)+'.', x['name'], '-', x['artists'][0]['name'])


print("\n\nTop 25 artists - Short Term (4 weeks)\n")
trackx = sp.current_user_top_artists(limit=25, offset=0, time_range='short_term')
for i, item in enumerate(trackx['items']):
        print(str(i+1)+'.', item['name'])

for x in tracks["items"]:
	print(x["name"])

print([x["name"] for x in tracks["items"]])

for x in tracks["items":"artists"]:
		print(x['name'])

print(sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term'))
for item in tracks["items"]:
    print(item["track"]["name"])

for x, y in tracks["items"]:
    if x["name"] != "Rain Sound : Night Time" and x["name"] != "Rain Sound : Dark Sky":
    	print(x["name"])
    print(x["name"], x["popularity"])	
"""
