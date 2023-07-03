import requests

#calling the translation endpoint
url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk",
    "Content-Type": "application/json"
}
print('\n')
print('TEXT TO-AND-FROM ENGLISH TO 5 LOCAL UGANDAN LANGUAGES TRANSLATOR')
print('\n')

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

    #Passing data obtained from the users into the /translate endpoint
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    #Response generation
    if response.status_code == 200:
        translated_text = response.json()["text"]
        print("Translate text:", translated_text)
    else:
        print("Error:", response.status_code, response.text)
else:
    print('Text input should be more than 3 characters')