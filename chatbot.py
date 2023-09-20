from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# import logging

# logging.basicConfig(level=logging.INFO)


bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/pychatbot'
)


# Create a new ChatBot instance
trainer = ChatterBotCorpusTrainer(ChatBot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english"
)

print('Type something to begin...')

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break