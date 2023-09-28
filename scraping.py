import re

# https://docs.python.org/3/library/re.html
from bs4 import BeautifulSoup
# https://pypi.org/project/beautifulsoup4/
from selenium import webdriver
# https://pypi.org/project/selenium/
# https://www.selenium.dev/documentation/webdriver/
from selenium.webdriver.chrome.service import Service
# https://www.selenium.dev/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.service.html
from selenium.webdriver.support import expected_conditions as EC
# https://selenium-python.readthedocs.io/waits.html
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# https://pypi.org/project/webdriver-manager/
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"

wait = WebDriverWait(driver, 10)

driver.get(url)

get_url = driver.current_url
wait.until(EC.url_to_be(url))

if get_url == url:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features="html.parser")
    keyword = "yoga"
    matches = soup.body.find_all(string=re.compile(keyword))
    print(matches)

print("Done")