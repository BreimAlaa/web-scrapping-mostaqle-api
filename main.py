from fastapi import FastAPI, BackgroundTasks, HTTPException, Query

from Extractor import Extractor
from Driver import Driver
from fastapi import Response
from typing import Annotated

app = FastAPI()
driver = Driver()
extractor = Extractor(driver)

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!",
            "url": extractor.test()   }


@app.get("/login")
async def demo_get(email: str, password: str):
    response = extractor.login(email=email, password=password)
    return {"message": response}

# get skills
@app.get("/skills")
async def get_skills(page:int = 1, query:str = ''):
    skills = extractor.get_skills(page, query)
    return Response(content=skills, media_type="application/json")

@app.get("/projects")
async def get_projects(page:int = 1, categories: str = '', skills: str = '', budget_min: int = 0, budget_max: int = 1000000):
    projects = extractor.get_projects(page, categories, skills, budget_min, budget_max)
    return {"projects": projects}

@app.get("/projects/{id}")
async def get_project(id: str):
    project = extractor.get_project(id)
    return {"project": project}