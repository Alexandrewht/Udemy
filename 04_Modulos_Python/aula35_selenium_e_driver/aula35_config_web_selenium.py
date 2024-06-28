from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
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
    # Chrome options
    # https://peter.sh/experiments/chromium-command-line-switches/
    # options = ('--disable-gpu',)
    options = ()
    browser = make_chrome_browser(*options)


    # como antes
    browser.get('https://www.google.com.br/')

    # dorme 10 segundos
    sleep(10)