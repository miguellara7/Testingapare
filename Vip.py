import pyautogui
import cv2
import numpy as np
import pytesseract
import time
import requests

# Telegram Bot API details
telegram_bot_token = "6183971971:AAEmtjVRdGbFBONNUZCCmk7EVkPFJYL6kik"  # Replace with your bot token
telegram_chat_id = "-956570940"  # Replace with your chat ID

# Initialize a counter to keep track of player changes
player_change_counter = 0
player_thresholds = [1, 20, 30, 50]  # Thresholds for sending alerts
alert_intervals = [300, 300, 120, 120]  # Intervals (in seconds) for checking and sending alerts
alert_sent_count = [0, 0, 0, 0]  # Count of alerts sent for each threshold

# Initialize a variable to store the current player list
current_player_list = []

# Initialize a variable to store the last sent message ID
last_sent_message_id = None

# Captura de pantalla de la región específica
def capture_screen_region(region):
    screenshot = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Comprobar si el texto está en verde (color del jugador en línea) o rojo (color de jugador fuera de línea)
def is_text_color(image, text, green_color, red_color):
    # Create a mask for the green color in the text
    mask_green = cv2.inRange(image, green_color, green_color)

    # Create a mask for the red color in the text
    mask_red = cv2.inRange(image, red_color, red_color)

    # Calculate the green pixel ratio in the text
    green_pixel_ratio = np.sum(mask_green > 0) / mask_green.size

    # Calculate the red pixel ratio in the text
    red_pixel_ratio = np.sum(mask_red > 0) / mask_red.size

    # If the majority of pixels are green, the text is in green
    if green_pixel_ratio > red_pixel_ratio:
        return True
    else:
        return False

# Function to send a message to the Telegram group and return the message ID
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    data = {'chat_id': telegram_chat_id, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        message_data = response.json()
        return message_data['result']['message_id']
    else:
        print(f'Error sending Telegram message: {response.text}')
        return None

# Function to edit an existing message in the Telegram group
def edit_telegram_message(message_id, message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/editMessageText'
    data = {'chat_id': telegram_chat_id, 'message_id': message_id, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print(f'Error editing Telegram message: {response.text}')

# Function to handle Telegram notifications
def telegram_notifications(player_names):
    global player_change_counter
    global alert_sent_count
    global current_player_list
    global last_sent_message_id

    total_players = len(player_names)

    # Check if the player list has changed
    if player_names != current_player_list:
        current_player_list = player_names

        # Send the updated player list as a single message or edit the existing message
        message = '🔥Online Enemy List🔥:\n' + '\n'.join(player_names)
        if last_sent_message_id is None:
            last_sent_message_id = send_telegram_message(message)
        else:
            edit_telegram_message(last_sent_message_id, message)

    # Check if the total number of players has changed
    if total_players != player_change_counter:
        player_change_counter = total_players

        # Check if the change exceeds any of the defined thresholds
        for i, threshold in enumerate(player_thresholds):
            if total_players >= threshold and alert_sent_count[i] < 3:
                alert_sent_count[i] += 1
                message = f'Connected Bombs x{total_players}:'
                if i == 0:
                    message = f'*{message}*'
                send_telegram_message(message)

# Define the region to capture
region = (1550, 35, 190, 900)  # Change these coordinates based on your region

# Define the green and red colors
green_color = (96, 248, 96)
red_color = (248, 96, 96)

while True:
    # Capture the specific region
    region_image = capture_screen_region(region)

    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(region_image)

    # Split the text into lines to get player names
    lines = extracted_text.split('\n')
    player_names = [line.strip() for line in lines if line.strip()]

    # Count players online
    players_in_line = 0

    # Check if players are online or offline
    for player_name in player_names:
        if is_text_color(region_image, player_name, green_color, red_color):
            players_in_line += 1

    # Send Telegram notifications with the player list and check for player changes
    telegram_notifications(player_names)

    # Sleep before capturing again
    time.sleep(5)  # Adjust the sleep time as needed
