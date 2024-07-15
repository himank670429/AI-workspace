from os import environ
import google.generativeai as genai
from colorama import Fore, Style

class Chat():
    @staticmethod 
    def start_chat_session(GENERATION_CONFIG, MODEL_NAME, SAFETY_SETTINGS, API_KEY):
        # setup instance

        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=GENERATION_CONFIG
            # safety_settings = SAFETY_SETTINGS
        )

        chat_session = model.start_chat(
            history=[
            ]
        )

        while True:
            user_promt = input("$ ")
            if (user_promt == ".exit"):
                break
            response = chat_session.send_message(user_promt)
            print(Fore.BLUE + response.text)

        print("exiting chat session")
