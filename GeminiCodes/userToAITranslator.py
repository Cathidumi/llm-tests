import os
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional


load_dotenv()

class Translator(BaseModel):
  typeQuestion: str
  question: str
  options: Optional[list[str]]

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=
            """-You are a helpful assistant whose task is to put information in a structured json
            -This json will further be user for another assistant in an forms aplication.
            Your  
            -The list of possible types for a question is: [SingleSelectionQuestion, CheckboxQuestion, CalendarQuestion, IntegerQuestion, DecimalQuestion, TextQuestion, EmailQuestion, TimeQuestion, PhoneQuestion, TextItem]
            -Generate a response without lines and spaces
            -Translate this: **one SingleSelectionQuestion item, with the following question: 'What is your City?' with the following options: 'Porto', 'Alegrete', 'Viamao'. Include one CheckboxQuestion item with the following question: 'what is do you eat?' with the following options: 'meat', 'vegetables'. Include one CalendarQuestion with the following question: 'When is your birthday?'. Include one IntegerQuestion with the following question: 'How Old are you?**
            """,
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[Translator],
    },
)

print(response.text)