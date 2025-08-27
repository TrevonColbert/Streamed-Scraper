import webbrowser
import pyautogui
import pyperclip
import time

#Time to search for 200 image when looking for m3u8 network link
timeout_seconds = 10

#Open webbrowser
webbrowser.open("https://streamed.pk/watch/1756245600000-us-open-stadium-17-baptiste-siniakova/bravo/1")

#set location and image file for locateonscreen (looking for refresh image)
location = None
imagefile = "refresh.png"
while location == None:
    try:
        location = pyautogui.locateOnScreen(imagefile)
    except Exception as e:
        print(e)
print(location)

#Open network info
pyautogui.hotkey('ctrl','shift','e')

#Set region to lower left quarter of screen for searching for 200 image //
screen_width, screen_height = pyautogui.size()
left = 0
top = screen_height // 2
width = screen_width // 2
height = screen_height // 2
region = (left, top, width, height)
#//

#Setup locateonscreen info
location = None
imagefile = "200.png"
validty = "Invalid"
start_time = time.time()
while time.time() - start_time < timeout_seconds:
    try:
        location = pyautogui.locateOnScreen(imagefile, confidence=0.9,region = region)
    except Exception as e:
        print(e)
    else:
        validty = "Valid"

if validty == "Valid":
    print(location)
    pyautogui.click(location) #click on 200 image / m3u8 link
    pyautogui.hotkey('ctrl','c') #copy link
    time.sleep(1) #wait 1 second for clipboard to update
    clipboard_content = pyperclip.paste() #get link from clipboard
    print(clipboard_content)
else:
    print("No valid link")


