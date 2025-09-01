from datetime import datetime,timedelta
import requests

'''
function streams:
    given list of sports,start hours int,end minutes int, url str
    returns list of streams with info in dictionary format {'title','sport','time','url'}
    used to get streams and their info
'''

def streams(sports,start_hours,end_minutes,url):

    cur_time = datetime.now() #get current time
    earliest = (cur_time - timedelta(hours=start_hours)).timestamp() * 1000 #get earliest start time to accept (-8 hrs)
    latest = (cur_time + timedelta(minutes=end_minutes)).timestamp() * 1000 #get latest start time to accept (+20 mins)

    response = requests.get(url) #call to api

    response_json = response.json() #store json of api call

    #limit matches output to sports of interest
    output_dict = [x for x in response_json if x['category'] in sports and x['date']>earliest and x['date']<latest] #get all matches that are in sport of interest

    #setup empty list to store eventual matches with urls
    m3u_dict = []

    #loop through each match in list
    for i in range(0,len(output_dict)):

        #setup empty list for all sources and their info
        sources_dict = []

        #loop through all sources for match
        for s in range(0, len(output_dict[i]['sources'])):
            source = output_dict[i]['sources'][s]['source'] #gets source name
            id = output_dict[i]['sources'][s]['id'] #gets source id
            sources_url = f"https://streamed.pk/api/stream/{source}/{id}" #url for api call for additional source info
            response2 = requests.get(sources_url) #call to api
            response2_json = response2.json() #store json of api call

            #add source to sources dict as long as it is in English and in HD
            sources_dict.append([x for x in response2_json if x['language'] == 'English' and x['hd'] == True])
        
        #try/except to get stream with the maximum number of viewers, will return empty if no valid sources appear
        try:
            max_viewers = max(sources_dict[0], key=lambda x:x['viewers'])
        except:
            max_viewers=[]

        #if max viewers stream exists convert date (milliseconds) to 12 Hour H:M format & then append info to m3u_dict
        if len(max_viewers)>0:
            timestamp = datetime.fromtimestamp((output_dict[i]['date'])/1000)
            match_start_time = timestamp.strftime("%I:%M %p")
            m3u_dict.append({'title':output_dict[i]['title'],'sport':output_dict[i]['category'],'time':match_start_time,'url':max_viewers['embedUrl']})
   
    return m3u_dict
        
