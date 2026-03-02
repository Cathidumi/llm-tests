import os
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional
from google.genai import types

from openai import OpenAI


load_dotenv()

class Question(BaseModel):
  typeQuestion: str
  question: str
  options: Optional[list[str]]

class Questions(BaseModel):
  questions: list[Question]

def translation(userInput, modelo='gpt-4o'):
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
  )

  response = client.chat.completions.create(
    model=modelo,
    messages=[
      {
        "role": "system",
        "content": """- You are a helpful assistant whose task is to put information in a structured json
              - This json will further be user for another assistant in an forms aplication.  
              - The list of possible types for a question is: [SingleSelectionQuestion, CheckboxQuestion, CalendarQuestion, IntegerQuestion, DecimalQuestion, TextQuestion, EmailQuestion, TimeQuestion, PhoneQuestion, TextItem]
              - Fill the json properties as resquested by the user input
              - Do it step by step as specified by the system structure.
              - Generate a response without lines and spaces
              - The json schema obeys the following structure:
              
              list[{
                typeQuestion: str
                question: str
                options: Optional[list[str]]
                }]

              - You must generate only the list of json objects, without any other text, and without any line break or space. The json must be in a single line, and the properties must be in the same order as specified in the schema.
              """
      },
      {
        "role": "user",
        "content": f"**userInput:**{userInput}"
      }
    ]
  )
  return response.choices[0].message.content

def translation2(userInput, modelo='gpt-4o'):
  load_dotenv()
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
  )
  response = client.responses.parse(
    model=modelo,
    input=[
      {
        "role": "system",
        "content": """- You are a helpful assistant whose task is to put information in a structured json
            - This json will further be user for another assistant in an forms aplication.  
            - The list of possible types for a question is: [SingleSelectionQuestion, CheckboxQuestion, CalendarQuestion, IntegerQuestion, DecimalQuestion, TextQuestion, EmailQuestion, TimeQuestion, PhoneQuestion, TextItem]
            - Fill the json properties as resquested by the user input
            - Do it step by step as specified by the system structure.
            - Generate a response without lines and spaces"""
      },
      {
        "role": "user",
        "content": f"**userInput:**{userInput}"
      }
    ],
    text_format=Questions
  )
  questoes = response.output_parsed.__dict__
  lista_questoes = questoes['questions']
  return lista_questoes


if __name__ == "__main__":
  generatedJson = translation2('Gere um json com duas perguntas genéricas')
  print(generatedJson)
  #print(type(generatedJson))
  #questoes = generatedJson.__dict__
  #print(questoes)
  #lista_questoes = questoes['questions']
  #print(lista_questoes)

# -Translate this: **one SingleSelectionQuestion item, with the following question: 'What is your City?' with the following options: 'Porto', 'Alegrete', 'Viamao'. Include one CheckboxQuestion item with the following question: 'what is do you eat?' with the following options: 'meat', 'vegetables'. Include one CalendarQuestion with the following question: 'When is your birthday?'. Include one IntegerQuestion with the following question: 'How Old are you?**
