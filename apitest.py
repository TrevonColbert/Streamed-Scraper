import requests
import json





url = 'https://streamed.pk/api/matches/live' #live matches json from api

#url2 = 'https://streamed.pk/api/stream/intel/alycia-parks-mirra-andreeva'

response = requests.get(url)

response_json = response.json()


output_dict = [x for x in response_json if x['category'] == 'basketball'] #get all matches that are in sport of interest

print(output_dict)

#testing
print(output_dict[0]['sources'][0]['id'])
source = output_dict[0]['sources'][0]['source']
id = output_dict[0]['sources'][0]['id']

#print(response.json())


#print(response2.json())

sources_url = f"https://streamed.pk/api/stream/{source}/{id}"

response2 = requests.get(sources_url)

print(response2.json())


#Get all live matches from api

#Filter down live matches json to only sports / criteria of interest

#Loop through all matches of interest and get streams info

    #Get streams json from api
    #Filter down to only language in english & HD true (+any other criteria)
    #get link to stream (embeded link likely)
    #run through get_m3u8 to get m3u8 link or if invalid then exit 
    #May want to also get match info and structure it in a way that makes sense for channel name
    #Add m3u8 and #EXTINF info to custom m3u file that will be supplied to jellyfin
    