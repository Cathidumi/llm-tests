
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def singleSelectionQuestion(userInput):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **SingleSelectionQuestion:{"extents":"SurveyItem","objectType":"SingleSelectionQuestion","templateID":"TML1","customID":"TML1","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"SingleSelectionQuestion input","formattedText":"SingleSelectionQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"options":[{"extents":"StudioObject","objectType":"AnswerOption","value":1,"extractionValue":1,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 1 input","formattedText":"option 1 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"AnswerOption","value":2,"extractionValue":2,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 2 input","formattedText":"option 2 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"AnswerOption","value":3,"extractionValue":3,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 3 input","formattedText":"option 3 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}],"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}},"imageUrl":null  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    print(response.text)