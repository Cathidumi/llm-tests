import gerador
import json
from datetime import datetime
import os

def generateJSON(userInput=str, acID='TML', name='formulario', modelo='gpt-4o'):
    """Generates the full JSON form structure based on user input description,
    including itemContainer and navigationList fields."""
    form = {
        "extents": "StudioObject",
        "objectType": "Survey",
        "oid": "dXNlclVVSUQ6W3VuZGVmaW5lZF1zdXJ2ZXlVVUlEOltkMzllZTg5MC05MDhkLTExZWYtOWZmYS1jOTM3YmMwNTQ1ODddcmVwb3NpdG9yeVVVSUQ6WyBOb3QgZG9uZSB5ZXQgXQ==",
        "identity": {
            "extents": "StudioObject",
            "objectType": "SurveyIdentity",
            "name": name,
            "acronym": acID,
            "recommendedTo": "",
            "description": "",
            "keywords": []
        },
        "metainfo": {
            "extents": "StudioObject",
            "objectType": "SurveyMetaInfo",
            "creationDatetime": "2024-10-22T15:53:48.697Z",
            "otusStudioVersion": ""
        },
        "dataSources": [],
        "itemContainer": [],
        "navigationList": [],
        "staticVariableList": [],
        "surveyItemGroupList": []
    }

    #print("Generating items...")

    itemCont = gerador.generateItemContainer(userInput, modelo=modelo) #generates item container field

    form['itemContainer'] = itemCont['itemContainer'] #adds generated field to forms dictionary

    numOfItens = len(form['itemContainer'])

    #print('Generating navigation...')

    navigationList = gerador.generate_navigation_structure(numOfItens)

    form['navigationList'] = navigationList['navigationList']

    #print('Adjusting indexes...')

    acronym = form['identity']['acronym']
    numOfItens = len(form['itemContainer'])
    alphaArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(0, numOfItens):
        form['itemContainer'][i]['templateID'] = f'{acronym}{i+1}'
        form['itemContainer'][i]['customID'] = f'{acronym}{i+1}'

        if form['itemContainer'][i]['objectType'] == 'CheckboxQuestion':
            currentIndex = form['itemContainer'][i]['templateID']
            for j in range(0, len(form['itemContainer'][i]['options'])):
                form['itemContainer'][i]['options'][j]['optionID'] = f'{acronym}{i+1}{alphaArray[j]}'
                form['itemContainer'][i]['options'][j]['customOptionID'] = f'{acronym}{i+1}{alphaArray[j]}'
        
    return form #retorna dicionario que deve ser convertido para json na exportação

def getTime():
    currentTime = str(datetime.now())
    currentTime = currentTime.replace(' ', 'T')
    currentTime = currentTime.replace(':', '_')
    currentTime = currentTime[:19]
    return currentTime


if __name__ == "__main__":

    #listaModelos = ['google/gemini-2.0-flash-001', 'gpt-4o', 'openai/gpt-4o-mini','google/gemini-2.5-flash-lite' ,'google/gemini-2.5-flash', 'google/gemini-2.5-pro' ]
    listaModelos = ['gpt-4o'] #test with only one model to avoid hitting rate limits during development

    
    questdirectory = os.path.dirname(os.path.abspath(__file__))
    questdirectory = questdirectory.replace('experimentos', 'questforms')
    questdirectory = questdirectory.replace('/modularOpenrouter', '')

    form = 'prompt3.txt'

    with open (f'{questdirectory}/{form}', 'r') as file:
        userForm = file.read()


    #model = listaModelos[5] #choose the model to be used in generation, changing the index will change the model

    for model in listaModelos:
        if model == 'google/gemini-2.0-flash-001':
            experiment = 'sample_MO_Gemini20Flash'
        elif model == 'gpt-4o':
            experiment = 'sample_MO_GPT4o'
        elif model == 'openai/gpt-4o-mini':
            experiment = 'sample_MO_GPT4oMini'
        elif model == 'google/gemini-2.0-flash-lite-001':
            experiment = 'sample_MO_Gemini20FlashLite'
        elif model == 'google/gemini-2.5-flash-lite':   
            experiment = 'sample_MO_Gemini25FlashLite'
        elif model == 'google/gemini-2.5-flash':
            experiment = 'sample_MO_Gemini25Flash'
        elif model == 'google/gemini-2.5-pro':
            experiment = 'sample_MO_Gemini25Pro'
        else:
            experiment = 'sample_MO_OpenRouter'
        for i in range(1,10,1): #number of forms to be generatedç~~~
            try:
                print(f'Tentativa formulário {i+1}...')
                generatedForm = generatedForm = generateJSON(
                    userInput=userForm,
                    acID='TML',
                    name='formularioTeste',
                    modelo=model)
                
                #saving sample to my computer
                mydirectory = os.path.dirname(os.path.abspath(__file__))
                mydirectory = mydirectory.replace('experimentos', 'samples')
                mydirectory = mydirectory.replace('/modularOpenrouter', '')
                if not os.path.exists(mydirectory):
                    os.makedirs(mydirectory)

                if os.name == 'nt': #windows
                    with open(f'{mydirectory}\\{experiment}_{getTime()}.json', 'w') as outfile:
                        json.dump(generatedForm, outfile)
                else: #linux or others
                    with open(f'{mydirectory}/{experiment}_{getTime()}.json', 'w') as outfile:
                        json.dump(generatedForm, outfile) 

            except Exception as e:
                print(f'Error generating form {i+1}: {e}')
                with open(f'error_log_{experiment}_{getTime()}.txt', 'a') as error_file:
                    error_file.write(f'{getTime()} - Error generating form {i+1}: {e}\n')
                pass
        
            #sleep(15) #sleep to avoid hitting rate limits