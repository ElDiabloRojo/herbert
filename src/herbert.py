# import the random library to help us generate the random numbers
import random

# Create the herbert Class
class Herbert:

    # Create a constant that contains the default text for the message
    MSG_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Sure! How can I help?\n\n"
            ),
        },
    }

    # The constructor for the class. It takes the channel name as the a 
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    # Generate a random number to simulate flipping a coin. Then return the 
    # crafted slack payload with the coin flip message.
    def _flip_coin(self):
        rand_int =  random.randint(0,1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"

        text = f"The result is {results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.MSG_BLOCK,
                *self._flip_coin(),
            ],
        }