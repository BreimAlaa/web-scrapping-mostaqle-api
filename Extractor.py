from selenium import webdriver
from selenium.webdriver.common.by import By
from Driver import Driver

class Extractor:
    def __init__(self, driver: Driver):
        self.driver = driver.load()

    def test(self):
        self.driver.get("https://www.google.com")
        return self.driver.current_url

    def login(self, email:str, password:str) -> str:
        self.driver.get("https://accounts.hsoub.com/login?source=mostaql&locale=ar")
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys(email)

        email_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys(password)

        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[3]/div/div/button')
        submit_button.click()
        self.cookies = self.driver.get_cookies()
        return self.driver.current_url

    def get_skills(self, page:int = 1, query:str="")->str:
        self.driver.get(f"https://mostaql.com/ajax/skills?search={page}&query={query}")
        skills = self.driver.find_element(By.TAG_NAME,"pre").text
        return skills


    # https: // mostaql.com / projects?category = business, development & budget_min = 50 & budget_max = 10000
    def get_projects(self, categories: list = [], skills:list = [], budget_min: int = 0, budget_max: int = 1000000):
        self.driver.get("https://mostaql.com/projects?")
        projects = self.driver.find_elements(By.CLASS_NAME, "project-card")
        return projects