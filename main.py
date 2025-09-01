import get_streams
import get_m3u8
import m3u8_generator
import config
import webbrowser
import pyautogui
import time
import sys
import os

os.chdir(config.PYLOCATION)

#Set regions for searches //
screen_width, screen_height = pyautogui.size()
half_width = screen_width // 2
half_height = screen_height // 2
top_left = (0,0,half_width,half_height)

#open new webbrowser to speed up later scraping
webbrowser.open_new('https://www.google.com/')

#call to api and get all streams that meet requirements
matches = get_streams.streams(config.SPORTS,config.STARTHOURS,config.STARTMINUTES,config.STREAMSAPI)

#if api returns empty list exit script
if len(matches)==0:
    sys.exit()

#scrape m3u8 links from matches
for i in range(0,len(matches)):
    m3u8_link = get_m3u8.scrape(matches[i]['url'])
    matches[i].update({'m3u8':m3u8_link})

#setup for keeping only matches with valid m3u8 links
valid_m3u8 = [x for x in matches if x['m3u8'] != 'Invalid' ]

#generate m3u8 file to feed to threadfin
m3u8_generator.base_generate(valid_m3u8,config.M3UFILE)

time.sleep(1)

#refresh threadfin playlist
get_m3u8.threadfin_refresh(config.THREADFINURL)

#//close default webbrowser page
refresh_button = get_m3u8.search(False,False,'refresh.png',top_left,0.9,"Infinite")
pyautogui.click(refresh_button)
time.sleep(1)
pyautogui.hotkey('ctrl','w') #close tab
#//


