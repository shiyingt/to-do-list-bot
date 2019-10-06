# urllib requires python3
import json
import requests
import time
import urllib
from dbhelper import DBHelper

db = DBHelper()

TOKEN = "<your-api-token>"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

#get url downloads content from url
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

#gets string response from def(get_url) and parses it into a python dictionary
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

#uses previous two functions but only for retrieving updates, which can be done through specification in url
def get_updates(offset=None):
    url = URL + "getUpdates"
    #to understand how offset helps us get the latest msg from the server, read about longpolling.
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def handle_updates(updates):
    for update in updates["result"]:
        text = update["message"]["text"]    #returns telegram text message
        chat = update["message"]["chat"]["id"]    #returns telegram msd sender's id 
        #switch to check for cmds in telegram message
        print(text[0:8])
        if text == "/start":
            send_message("Welcome to itemListBot.", chat)  
        elif ("/additem" in text) and (text[0:8] == "/additem"):
           #breaks up message into msg to add to todo list
            itemName = text[9:]
            db.add_item(itemName)
        elif ("/removeitem" in text) and (text[0:11]== "/removeitem"):
            itemName = text[12:]
            if db.check_exists(itemName)==[]:
              send_message("item not in cart.", chat) 
            else:
              db.delete_item(itemName)
        elif text == "/entries":
            entry_msg = ""
            itemList = db.get_items()
            print(itemList)
            #concatenate itemList
            for i in range(len(itemList)):
              entry_msg+=itemList[i] +'\n'
            send_message(entry_msg,chat)
        elif text == "/itemListLength":
            lenItemList = len(db.get_items())
            send_message(lenItemList,chat)
        else:
          send_message("not a cmd", chat)

#gets content and sender id of last message in telegram
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

#uses sendMessageAPI cmd to send text and chat ID as url parameters
def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def main():
  #setup database
    db.setup()
    last_update_id = None
    #checks for new updates every 0.5 seconds
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

#import functions into another script without running anything
if __name__ == '__main__':
    main()