from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env
load_dotenv()

# Access the token
token = os.getenv("MY_TOKEN")

#calling the translation endpoint
url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
print('\n')
print('TEXT TO-AND-FROM ENGLISH TO 5 LOCAL UGANDAN LANGUAGES TRANSLATOR')
print('\n')

state = True

while state:
        #The user enters the source language
        source_language = input('Please choose the source language:')
        
        #The user enters the target language
        target_language = input('Please choose the target language: (one of Luganda, Runyankole, Ateso, Lugbara or Acholi):')

        #The user enters the text to be translated from the source language to the target language
        text = input('Enter the text to translate:')

        #The text should having 3 or more characters, an error occurs
        if len(text) >= 3:
            payload = {
            "source_language": source_language,
            "target_language": target_language,
            "text": text }

            #Translation from one local language to another
            if (source_language or target_language) != "English":
                 payload = {
                      "source_language": source_language,
                      "target_language": "English",
                      "text": text }

                 #Passing data obtained from the users into the /translate endpoint
                 response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

                 #Response generation
                 if response.status_code == 200:
                    translated_text = response.json()["text"]
                    payload = {
                        "source_language": "English",
                        "target_language": target_language,
                        "text": translated_text }
                    
                    #Passing data obtained from the users into the /translate endpoint
                    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)
                    #Response generation
                    if response.status_code == 200:
                        translated_text2 = response.json()["text"]
                        print("Translate text:", translated_text2)
                    else:
                        print("Error:", response.status_code, response.text)
                
                 else:
                    print("Error:", response.status_code, response.text)

            else:
                #Translating to a local language and English and from English to a local language
                #Passing data obtained from the users into the /translate endpoint
                response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)
                #Response generation
                if response.status_code == 200:
                    translated_text= response.json()["text"]
                    print("Translate text:", translated_text)
                else:
                    print("Error:", response.status_code, response.text)

        else:
            print('Text input should be more than 3 characters')
        
        #Prompting the user to enter y to continue translating or n to stop tanslating
        choice = input('Do you wnat to continue translating, please enter y/n ?')

        if choice == 'y':
             continue

        elif choice == 'n':
            break
        
while not state:
    break
    