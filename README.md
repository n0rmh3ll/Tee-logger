![Tee-logger](https://socialify.git.ci/n0rmh3ll/Tee-logger/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&name=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Dark)

## Overview
This is a updated Python keylogger that logs keystrokes and sends them to a specified Telegram chat using a Telegram bot. This project can be used for monitoring keystrokes and receiving notifications in real-time.

* **Note: The use of keyloggers without explicit consent is unethical and potentially illegal. This script is intended for educational purposes only, and it is crucial to respect privacy and adhere to applicable laws and regulations** 

# Features
* Keylogging: Captures keystrokes in real-time and logs them into a designated file.
* Telegram Integration: Sends logged keystrokes to a specified Telegram chat, enabling remote monitoring.

# Getting Started 🚀 
## Prerequisites
* Python 3.x
* keyboard library (`pip install keyboard`)
* requests library (`pip install requests`)
## Setup
* 1 : Clone the Repository
```bash
 https://github.com/n0rmh3ll/Tee-logger
```
* 2 : Install Dependencies
```bash
  pip install keyboard request
```
* 3 : Obtain `Telegram Bot Token` and `Chat ID`
  
    * Create a new bot using [@BotFather](https://t.me/BotFather) on Telegram.
    * Obtain the bot token provided by BotFather.
    * Start a chat with your bot and get the chat ID using tools like `getids.net` or simply use [@MissRose_bot](https://t.me/MissRose_bot) and use /id command for chat id

* 4 : Configure the Script

  - Update the configuration variables in `tee-logger.py`

  - `CHAT_ID:` Your Telegram chat ID.

  - `BOT_TOKEN:` Your Telegram bot token.

## Usage
Run the script, and it will start sending key presses, along with timestamps in real time will be sent to the specified Telegram chat
```bash
python3 tee-logger.py
```
* Stop the Keylogger:

Press `Ctrl+C` to stop the keylogger

## Security Considerations
Ensure that you have appropriate permissions before running this script, as it monitors keystrokes.
Avoid running the keylogger on systems where you don't have authorization or where monitoring keystrokes could violate privacy laws or policies.
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://n0rmh3ll.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/n0rmh3ll/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/n0rmh3ll)

## Contributing
Contributions are welcome! Please feel free to submit pull requests to improve the project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
