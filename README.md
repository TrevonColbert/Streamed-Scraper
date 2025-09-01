This script scrapes m3u8 stream links from streamed.pk. This script is intended for use on jellyfin servers with Threadfin installed.  Ensure that after initially setting up, filters are used in threadfin (not ignored) and that the group title 'live' is marked as a live event so all channels appear active by default.

Use firefox browser in dark mode in order for this script to work.
  
Buffer should be set to ffmpeg in threadfin, & playlist origin: 'https://embedsports.top' & referer: 'https://embedsports.top/'.  Set m3u file to be location same as M3UFILE config variable

Required python libraries: 

	requests, pyautogui, pyperclip, datetime, webbrowser, sys

Config file should be updated for the following variables:

	SPORTS = ['basketball','baseball','american-football','fight'] | this updates what sports will be pulled, refer to streamed.pk documentation/api for list of sports
	
	M3UFILE = 'Y:\\base.m3u8' | location to save m3u8 file that the script generates to feed into threadfin
	
	STARTHOURS = 8 | How many hours before current time to start looking for streams based on start time
	
	STARTMINUTES = 20 | How many minutes after current time to look for streams based on start time
	
	STREAMSAPI = 'https://streamed.pk/api/matches/all-today' #all matches today from api url | API call made to streamed.pk to get matches info
	
	THREADFINURL = 'http://192.168.1.100:16977/web/' | url for threadfin web interface

	PYLOCATION = "C:\\Users\\trebo\\Python Projects\\Streamed Scraper" | location of script folder so images and paths can properly be referenced
