# Description
This script checks the Bioauth of the Humanode node and sends an alert in Telegram if the Bioauth is expired, about to expire on not answering.  
*SLEEP_TIMEOUT* in the .env file is the time in seconds between checks.  
Script should be run on the same machine as the Humanode node.  
To check availability humanode RPC you can use the following command:
```bash
curl http://127.0.0.1:9933 -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"bioauth_status","params":[],"id":1}'
```
If the response is similar to the following, the RPC is available:
```json
{"jsonrpc":"2.0","result":{"Active":{"expires_at":1713262470000}},"id":1}
```

# Installation  
There are two ways to install the script:
1. Using directly the script (requires installation of some python dependencies and tmux)  

```bash
git clone https://github.com/vilija19/humanode-alert.git
cd ~/humanode-alert/
sudo apt update
sudo apt install python3-pip tmux
tmux
cd ~/humanode-alert/
pip install python-dotenv
pip install requests
cp .env.example .env
```
Edit the .env file and add the required values.  
Start the script:
```bash
./check_node.py
```
Script will be run in tmux session, so you can detach from the session and close the terminal.  
To reattach to the session, use the following command:
```bash
tmux a
```
2. Using docker (requires of installed docker)
```bash
git clone https://github.com/vilija19/humanode-alert.git
cd ~/humanode-alert/
cp .env-example .env
```
Edit the .env file and add the required values.  
Start the script:
```bash
./build.sh
./start.sh
```
To stop the script:
```bash
docker stop humanode-alert
```
To start or restart the script after changes in the .env file:
```bash
docker restart humanode-alert
```
# Telegram bot
To create a Telegram bot, you need to follow the instructions:
1. Register bot: send "/newbot" to @BotFather and follow instructions
2. Copy and paste the obtained token into the "TELEGRAM_BOT_TOKEN" field in .env file
3. If you want to send personal notifications, you need to get chat id of the user you want to send messages to:  
    3.1. Send "/getid" to "@myidbot" in Telegram messenger  
    3.2. Copy returned chat id and save it in the "TELEGRAM_CHAT_ID" in .env file   
    3.3. Ask the user to send "/start" to your bot (Telegram bot won't send anything to the user without it)  
4. If you want to send group notifications, you need to get group id of the group you want to send messages to:  
    4.1. Add "@myidbot" to your group  
    4.2. Send "/getgroupid@myidbot" in your group  
    4.3. Copy returned group id save it in the "TELEGRAM_CHAT_ID" in file .env file  
    4.4. Send "/start@your_bot_name_here" in your group (Telegram bot won't send anything to the group without it)  

  

Example of alerts:  
![ScreenShot](https://raw.github.com/vilija19/storage/main/2024-04-18_17-30.png)  

Tips to:  
hmp43ibc1Np1RL6KFwBThBBQpJC5bgoH9HkDVcfhr8NV35s3R