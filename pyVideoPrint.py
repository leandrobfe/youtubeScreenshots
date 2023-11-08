
# Import the required modules
import pyautogui # for taking screenshots
import webbrowser # for opening the youtube video
import time # for pausing the script
import keyboard
import requests # for getting the video duration
import json

# Define the youtube video url
video_url = "https://www.youtube.com/watch?v=WWDgt7zek1E"

# Define the number of screenshots to take
num_screenshots = 5

# Define the time interval between screenshots in seconds
skip_duration = 10
initial_load_delay = 4
skip_delay = 0.5

api_key = "AIzaSyAe0TCfVVe-8rlF5CejBES_Fv8OSfmJTsg"
response = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_url.split('=')[-1]}&key={api_key}")
duration = response.json()["items"][0]["contentDetails"]["duration"]
duration = int(duration.replace("PT", "").replace("M", "").replace("S", ""))
screenshot_count = 0
elapsed_time = 0

# Open the youtube video in a new tab
webbrowser.open_new_tab(video_url)

# Wait for the video to load
time.sleep(initial_load_delay)
keyboard.press_and_release("m") # mute
keyboard.press_and_release("k") # pause
keyboard.press_and_release("f") # full screen

while elapsed_time < duration: # Take a screenshot and save it with a name 
    pyautogui.screenshot(f"screenshot_{screenshot_count+1}.png") # Increment the screenshot counter and the elapsed time 
    screenshot_count += 1
    elapsed_time += skip_duration # Skip forward the skip duration 
    #keyboard.press_and_release(f"right arrow {skip_duration} times") # skip forward
    keyboard.press_and_release("l") # skip forward
    time.sleep(skip_delay)

# Loop through the number of screenshots Bkp
# for i in range(num_screenshots):
#     # Take a screenshot and save it with a name
#     pyautogui.screenshot(f"screenshot_{i+1}.png")
#     # Wait for the time interval
#     keyboard.press_and_release("l") # skip forward

# Close the tab
webbrowser.close()