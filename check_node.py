#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Write a Python program to send POST request and handle JSON responce.

from dotenv import load_dotenv
import os
import requests
import json
import time

load_dotenv()
alert_treshold = int(os.getenv('ALERT_TRESHOLD'))
sleep_timeout = int(os.getenv('SLEEP_TIMEOUT'))
host_name = os.getenv('HOST_NAME')

url_node = os.getenv('URL_NODE')
data_node = {'jsonrpc': '2.0', 'method': 'eth_syncing', 'params': [], 'id': 1}
headers_node = {'Content-Type': 'application/json'}

# Send alert to telegram
def send_alert(title, message):
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url_tg = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    data_tg = {'parse_mode': 'markdown', 'chat_id': telegram_chat_id, 'text': f"*{title}*\n{message}"}
    headers_tg = {'Content-Type': 'application/json'}
    response = requests.post(url_tg, data=json.dumps(data_tg), headers=headers_tg).json()
    print(response)
    return response.get('ok')

while True:
    response = requests.post(url_node, data=json.dumps(data_node), headers=headers_node).json()
    # test_response = {"jsonrpc":"2.0","result":{"Active":{"expires_at":1713262470000}},"id":1}
    # response = test_response
    expires_at = time.time()
    if response['result'] == False:
        print('Node is not answer!!!')
        res = send_alert(title=host_name, message='⛔ Node is not answer!!!')
        print('Send alert:', res)
    else:
        result = response['result']
        
    if 'Active' in result and 'expires_at' in result['Active']:
        print('Bioauth is Active')
        print('Bioauth status will expire at', result['Active']['expires_at'])
        expires_at = (result['Active']['expires_at'])/1000

    # Get time now
    now = time.time()
    diff = expires_at - now
    print('Diff:', diff)
    if diff < 0:
        print('Bioauth status has expired')
        res = send_alert(title=host_name, message='⛔ Bioauth status has expired')
        print('Send alert:', res)

    elif diff < alert_treshold:
        print('Bioauth status will expire in', diff, 'seconds')
        send_alert(title=host_name, message=f'⚠️ Bioauth status will expire in {diff} seconds')
        print('Send alert:', res)

    time.sleep(sleep_timeout)
