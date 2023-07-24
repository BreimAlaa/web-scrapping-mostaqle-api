from fastapi import FastAPI, BackgroundTasks, HTTPException
from Extractor import Extractor
from Driver import Driver
from fastapi import Response

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
async def get_skills(page:int = 1, query:str = ""):
    skills = extractor.get_skills(page, query)
    return Response(content=skills, media_type="application/json")

# get projects
@app.get("/projects")
async def get_projects(categories: list = [], skills:list = [], budget_min: int = 0, budget_max: int = 1000000):
    extract_projects(driver, categories)
    projects = getProjects(driver)
    return {"projects": projects}