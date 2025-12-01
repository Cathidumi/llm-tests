#imports for server 
from fastapi import FastAPI
from pydantic import BaseModel

#import env variables and OtusFormsGem
import OtusFormsGem 
from dotenv import load_dotenv
load_dotenv()#loads env variables

class Survey(BaseModel):
    description: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "homero-api-server"}

@app.get("/get-survey/")
async def get_survey():
    userForm = 'one text item element'
    generatedJSON = OtusFormsGem.generateJSON(userForm)
    return {"message": generatedJSON}

@app.post("/survey/")
async def create_survey(survey: Survey):
    userForm = survey.description
    generatedJSON = OtusFormsGem.generateJSON(userForm)
    return {"message": generatedJSON}
    
