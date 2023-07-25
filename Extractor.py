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

    def get_parms(self, list:str, key:str, first:bool = False):
        if len(list) == 0:
            return ""
        if first:
            st = "?"
        else:
            st = "&"
        return f"{st}{key}=" + list

    def get_projects(self, page = 1, categories: list = [], skills:list = [], budget_min: int = 0, budget_max: int = 1000000):

        categories_params = self.get_parms(categories, "category")
        skills_params = self.get_parms(skills, "skills")

        self.driver.get(f"https://mostaql.com/projects?page={page}{categories_params}{skills_params}&budget_min={budget_min}&budget_max={budget_max}")

        job_wrappers = self.driver.find_elements(By.CLASS_NAME,'project-row')

        values = {}

        for job_wrapper in job_wrappers:
            job_title_wrapper = job_wrapper.find_element(By.CLASS_NAME, 'mrg--bt-reset')
            job_title = job_title_wrapper.find_element(By.TAG_NAME, 'a').text
            job_link = job_title_wrapper.find_element(By.TAG_NAME, 'a').get_attribute('href')

            job_decription = job_wrapper.find_element(By.CLASS_NAME, 'details-url').text
            id = job_link.split('project')[1].split('-')[0].replace('/', '');
            link = f'https://mostaql.com/project/{id}'
            values[id] = {'job_title':job_title, 'job_descrption':job_decription, 'job_link':link}

        return values
