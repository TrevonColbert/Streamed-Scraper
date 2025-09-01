import webbrowser
import pyautogui
import pyperclip
import time

#//get_m3u8 info
'''
function scrape:
    given a url: str
    returns m3u8 link from network info, if no link then "Invalid"
    used to get m3u8 links

function search:
    given a start: time.time(),timeout : int,image: str,region,confidence (float 0:1,time_type: str ("Infinite" or "Timeout")
    returns location of image for pyautogui
    used to search for image file on webpage using pyautogui

function threafin_refresh():
    given url: str
    returns nothing
    opens up threadfin and updates playlist
'''
#//

#Time to search for 200 image when looking for m3u8 network link
timeout_seconds = 10
timeout_seconds_short = 5

#Set regions for searches //
screen_width, screen_height = pyautogui.size()
half_width = screen_width // 2
half_height = screen_height // 2
top_left = (0,0,half_width,half_height)
bottom_left = (0, half_height, half_width, half_height)
bottom = (0, half_height, screen_width, half_height)
top = (0, 0, screen_width, half_height)
left = (0, 0, half_width, screen_height)
#//

#set image files
refreshImage = 'refresh.png'
filterImage = 'filter.png'
clearImage = 'clear.png'
statusImage = '200.png'
playlistImage = 'playlist.png'
streamedImage = 'streamed.png'
updateImage = 'update.png'
m3uImage = 'm3u.png'

#scrape will retrieve and return m3u8 links (either link of "Invalid" if no link exists)
def scrape(url: str):

    #Open webbrowser
    webbrowser.open(url)
    time.sleep(2)

    #set location and image file for locateonscreen (looking for refresh image)
    refreshLoc = search(False,False,refreshImage,top_left,0.9,'Infinite') 
    pyautogui.click(refreshLoc) #click on refresh image to focus tab
    time.sleep(2) #pause 2 seconds
    search(False,False,refreshImage,top_left,0.9,'Infinite')  #find refresh image again to confirm page refreshed


    #Open network info
    pyautogui.hotkey('ctrl','shift','e')

    #search for filter
    filterLoc = None
    filterLoc = search(time.time(),timeout_seconds_short,filterImage,bottom_left,0.9,'Timeout')
    if filterLoc == None: #Couldn't find filter becuase network wasn't open
        pyautogui.hotkey('ctrl','shift','e') #Try to open network again
        filterLoc = search(time.time(),timeout_seconds_short,filterImage,bottom_left,0.9,'Timeout') #search for filter
    pyautogui.click(filterLoc) #click on filter image
    pyautogui.write("test", interval=0.1) #type in text to setup clear filter

    #search for filter clear button
    clearLoc = None
    clearLoc = search(False,False,clearImage,bottom,0.9,'Infinite')
    pyautogui.click(clearLoc) #click on clear button
    pyautogui.click(filterLoc) #click on filter image
    pyautogui.write("m3u8", interval=0.1) #type in m3u8 to filter just for m3u8

    #search for 200 status
    statusLoc = None
    statusLoc = search(time.time(),timeout_seconds,statusImage,bottom_left,0.9,'Timeout')
    if statusLoc == None:
        m3u8_link = "Invalid"
    else:
        pyautogui.click(statusLoc) #click on 200 status / m3u8 link
        pyautogui.hotkey('ctrl','c') #copy link
        time.sleep(.5) #wait .5 second for clipboard to update
        m3u8_link = pyperclip.paste() #get link from clipboard
        
    pyautogui.hotkey('ctrl','w') #close tab after getting link
    return m3u8_link
        
        


def search(start,timeout,image: str,region,confidence,time_type: str):
    location = None
    if time_type == 'Timeout':
        while time.time() - start < timeout and location == None:
            try:
                location = pyautogui.locateOnScreen(image, confidence = confidence,region = region)
            except Exception as e:
                pass
        return location
    if time_type == "Infinite":
        while location == None:
            try:
                location = pyautogui.locateOnScreen(image, confidence = confidence,region = region)
            except Exception as e:
                pass
        return location

def threadfin_refresh(url):

    webbrowser.open(url)

    time.sleep(2)

    #find refresh button and click to ensure loading
    refreshLoc = search(False,False,refreshImage,top_left,0.9,'Infinite')
    pyautogui.click(refreshLoc)

    time.sleep(1)

    #find playlist button and click
    playlistLoc = search(False,False,playlistImage,top,0.9,'Infinite')
    pyautogui.click(playlistLoc)

    time.sleep(1)

    #find streamed playlist and open
    streamedLoc = search(False,False,streamedImage,left,0.9,'Infinite')
    pyautogui.click(streamedLoc)

    time.sleep(1)

    #scroll to bottom of page
    pyautogui.scroll(-500) 

    #find update button and click
    updateLoc = search(False,False,updateImage,bottom,0.9,'Infinite')
    pyautogui.click(updateLoc)

    #this will make the code wait until the update is done and the playlist button can be found again
    playlistLoc2 = search(False,False,playlistImage,top,0.99,'Infinite')
    pyautogui.click(playlistLoc2)
    time.sleep(2)
    pyautogui.hotkey('ctrl','w') #close tab




