from random import randint
from time import sleep
messages = ["You will suffer a terrible fate someday...", "I will find you.", "The ducks were quacking weirdly today, weren't they?",
            "Countdown began", "What do you remember about last week?"]
for i in range(10):
    try:
        print(messages[randint(0,5)])
    except IndexError:
        print("ERROR: Something is trying to communicate...")
    finally:
        print("The computer is watching you\n")
        sleep(1)