
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import userToAITranslator

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def singleSelectionQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
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
    return response.text

def checkboxQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **CheckboxQuestion:{"extents":"SurveyItem","objectType":"CheckboxQuestion","templateID":"TML2","customID":"TML2","dataType":"Array","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"CheckboxQuestion input","formattedText":"CheckboxQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"options":[{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2a","customOptionID":"TML2a","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 1 input","formattedText":"option 1 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2b","customOptionID":"TML2b","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 2 input","formattedText":"option 2 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2c","customOptionID":"TML2c","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 3 input","formattedText":"option 3 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}],"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def CalendarQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **CalendarQuestion:{"extents":"SurveyItem","objectType":"CalendarQuestion","templateID":"TML3","customID":"TML3","dataType":"LocalDate","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"CalendarQuestion input","formattedText":"CalendarQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def integerQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **IntegerQuestion:{"extents":"SurveyItem","objectType":"IntegerQuestion","templateID":"TML4","customID":"TML4","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"IntegerQuestion input","formattedText":"IntegerQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"unit":{"ptBR":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""}},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def decimalQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **DecimalQuestion:{"extents":"SurveyItem","objectType":"DecimalQuestion","templateID":"TML5","customID":"TML5","dataType":"Decimal","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"DecimalQuestion input","formattedText":"DecimalQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"unit":{"ptBR":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""}},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def textQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TextQuestion:{"extents":"SurveyItem","objectType":"TextQuestion","templateID":"TML6","customID":"TML6","dataType":"String","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TextQuestion input","formattedText":"TextQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def emailQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **EmailQuestion:{"extents":"SurveyItem","objectType":"EmailQuestion","templateID":"TML7","customID":"TML7","dataType":"String","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"EmailQuestion input","formattedText":"EmailQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def timeQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TimeQuestion:{"extents":"SurveyItem","objectType":"TimeQuestion","templateID":"TML8","customID":"TML8","dataType":"LocalTime","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TimeQuestion input","formattedText":"TimeQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}},"options":{"extends":"StudioObject","objectType":"QuestionOption","data":{}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def phoneQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **PhoneQuestion:{"extents":"SurveyItem","objectType":"PhoneQuestion","templateID":"TML9","customID":"TML9","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"PhoneQuestion input","formattedText":"PhoneQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def textItem(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TextItem:{"extents":"SurveyItem","objectType":"TextItem","templateID":"TML10","customID":"TML10","dataType":"String","value":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TextItem input","formattedText":"TextItem input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def autocompleteQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **AutocompleteQuestion: {"extents":"SurveyItem","objectType":"AutocompleteQuestion","templateID":"TML11","customID":"TML11","dataType":"String","dataSources":[],"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"AutocompleteQuestion input","formattedText":"AutocompleteQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def fileUploadQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **FileUploadQuestion: {"extents":"SurveyItem","objectType":"FileUploadQuestion","templateID":"TML12","customID":"TML12","dataType":"Binary","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"FileUploadQuestion input","formattedText":"FileUploadQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def ImageItem(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **ImageItem: {"extents":"SurveyItem","objectType":"ImageItem","templateID":"TML13","customID":"TML13","dataType":"String","url":"","footer":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

if __name__ == "__main__":
   generatedJson = singleSelectionQuestion(userToAITranslator.translation('Gere uma pergunta de seleção única'))

   print(generatedJson)

   