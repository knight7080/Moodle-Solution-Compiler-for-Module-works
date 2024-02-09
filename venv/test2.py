from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

driver.get("file:///C:/Users/kaushik/PycharmProjects/moodle_doc/venv/result.html")

content = driver.find_elements(By.CLASS_NAME,"content")

log = {}

for i in range(0,len(content)-1):
    q = l[i].find_elements(By.TAG_NAME,'p')
    r = l[i].find_elements(By.XPATH, "//textarea[@class='coderunner-answer edit_code']")
    Q = q[0].text
    A = r[i].get_attribute("value")
    log[Q] = A

    # # print(len(q))
    #
    #
    # print(len(q),len(r))
    # for k in r:
    #     print(k.get_attribute("value"))

    print("YAYYYYYYYYYYYYYY \n \n")


# print(l)
#
# print(len(l))
print(log)
time.sleep(10)

driver.close()

