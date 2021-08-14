from neuralintents import GenericAssistant
import os

chatbot = GenericAssistant("intents.json")
chatbot.train_model()
chatbot.save_model()

def reply(msg):
    if msg is not None:
        response = chatbot.request(msg)
        return response


