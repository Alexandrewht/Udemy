from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)


    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10

    options = ()
    browser = make_chrome_browser(*options)

    # como antes
    browser.get('https://www.google.com.br/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)
    
    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # dorme 10 segundos
    sleep(TIME_TO_WAIT)