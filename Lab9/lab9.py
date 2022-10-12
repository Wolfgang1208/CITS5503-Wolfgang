from html import entities
from urllib import response
import boto3
import json

client = boto3.client('comprehend')

texten = "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799."

textes = "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha."

textfr = "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir"

textit = "L'amor che move il sole e l'altre stelle."

text = []

text.append(texten)
text.append(textes)
text.append(textfr)
text.append(textit)

def dectectLang(testText):
    #Detect_Entities
    response = client.detect_dominant_language(
        Text = testText,
    )
    print("Output:")
    lang = ""
    langCode = response['Languages'][0]['LanguageCode']
    if response['Languages'][0]['LanguageCode'] == 'en':
        lang = "English"
    if response['Languages'][0]['LanguageCode'] == 'it':
        lang = "Italian"
    if response['Languages'][0]['LanguageCode'] == 'fr':
        lang = "Franch"
    if response['Languages'][0]['LanguageCode'] == 'es':
        lang = "Spanish"
    pro = int(response['Languages'][0]['Score']*100)
    print(f"{lang} detected with {pro}% confidence")

    #Batch_detect_sentiment
    response = client.batch_detect_sentiment(
        TextList=[
            testText,
        ],
        LanguageCode=langCode
    )
    if response['ResultList']:
        SA = response['ResultList'][0]['Sentiment']
        print(f"This text is {SA}")
    else:
        print("Error when generating response.")

    #Detect_entities
    response = client.detect_entities(
        Text=testText,
        LanguageCode=langCode,
    )
    if response['Entities']:
        entities = response['Entities'][0]['Type']
        print(f"Entity is {entities}")
    else:
        print("Error when generating response.")

    #Detect_key_phrases
    response = client.detect_key_phrases(
        Text=testText,
        LanguageCode=langCode
    )
    if response['KeyPhrases']:
        key = response['KeyPhrases'][0]['Text']
        print(f"KeyPhrases is {key}")
    else:
        print("Error when generating response.")
    
    #Detect_syntax
    response = client.detect_syntax(
        Text=testText,
        LanguageCode=langCode
    )
    if response['SyntaxTokens']:
        syntax = response['SyntaxTokens'][0]['PartOfSpeech']['Tag']
        print(f"SyntaxTokens is {syntax}")
    else:
        print("Error when generating response.")
    
    print("______________________________________")

for t in text:
    dectectLang(t)
