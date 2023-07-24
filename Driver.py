from selenium import webdriver

class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(options=options)

    def load(self)->webdriver.Chrome:
        return self.driver
