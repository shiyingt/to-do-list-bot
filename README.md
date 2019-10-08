# Bot Building Workshop
The workshop is conducted on 8/10/2019 by Shi Ying from 3DC.
These notes are contributed by @lyqht, do note that optional sections were not covered in the workshop.

## Bot setup
To check your bot is up:
- Go to https://api.telegram.org/bot<bot-token>/getme
  - e.g. of bot-token: 928301972401-tsijksajdksahq 

To send a message from your bot to yourself:
1. Talk to your bot on telegram
2. Get your clientID based on the message you have just sent the bot:
   - Go to https://api.telegram.org/bot<bot-token>/getUpdates, in one of the messages, the ID is located under the messages.
3. Try sending a message to yourself from your bot via https://api.telegram.org/bot<bot-token>/sendMessage?chat_id=<chat-id>&text=<text-message>
   -  e.g. of textMessage: hellooooo
   -  e.g. of chat-id: 3291083190

## DB Initialization

For this app, there are 5 basic functions for the sqlite database.
1. `setup(self)`
2. `add_item(self, item_text)`
3. `delete_item(self, item_text)`
4. `get_items(self)`
5. `check_exists(self,item_text)`

Participants tried out writing the required functions by filling up the starter code in `dbsample.py`. The solution is in `dbhelper.py`.

This workshop does not cover indepth about how the sqlite3 works, but if you want to dive into the code further, you can refer to the [Sqlite3 API documentation](https://docs.python.org/2/library/sqlite3.html).

Some clarifications by Shi Ying on `dbsample.py`
- `self.conn.execute(stmt, args)` is an execution statement is required for every command that you do in the sqllite3 database. 
  - The return result is a tuple of the column values containing the data that we want. Hence we need use `x[0] for x in self.conn.execute(stmt)` to retrieve the specific data.
- `self.conn.commit()` is only required if you're making changes in the database.
  - Hence, only `add_item` & `delete_item` functions call this sqllite function.
- `(?)` refers to the placeholder that will be replaced by `args` later on, when the `.execute(stmt,args)` is called.

## Telegram Bot Communication

Replace the `TOKEN` variable appropriately. You can either directly replace it with your value or refer to [setting up secret environment variables (optional)](#storing-secret-variables-optional).

After that you can run the `telebot.py` file, and see the chat messages that you have sent to the bot in the terminal.

Your bot now supports the following commands:
- /additem __
- /removeitem __
- /entries
- /itemListLength

Telegram API documentation: https://core.telegram.org/bots/api

### Making available commands pop up as the user types (OPTIONAL)

Currently there is no indication if the bot has any commands availab le. To add commands, go back to botfather and add commands for your bot. The instructions are relatively simple to follow. After that you can go back to your bot and when you type in "/", you can see all the commands available.

### Storing secret variables (OPTIONAL)

This is not covered in the workshop but @lyqht thought it might be helpful to share to newbies. 

> Please never expose your secret variables to the world...

For storing and accessing secret environment variables in a `.env`, you need to install dotenv package.
```bash
pip install dotenv
```
Refer to `settings.py` for the code to do so. For more information of how this works, refer to https://github.com/theskumar/python-dotenv.

