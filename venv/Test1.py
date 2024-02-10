import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import merger
from selenium.webdriver.chrome.options import Options
import pdfkit
import os.path


chrome_options = Options()
# chrome_options.add_argument('--headless')
# // run this for executing in the backend without a visible window


def module_fetch(m_name,lang,f_name,drvr):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # // run this for executing in the backend without a visible window

    mod_name = m_name
    driver = drvr


    driver.get("http://training.saveetha.in/?redirect=0")

    driver.find_element(By.XPATH, "//a[text()='" + mod_name + "']").click()

    quant = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")

    wkhtmltopdf_options = {"enable-local-file-access": ""}

    l = len(quant)

    print(l)

    log = {}

    count = 1

    for j in range(l - 13, l):
        mods = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")
        print("Total number of seb challenges: ", len(mods))

        try:
            m = mods[j].find_elements(By.CLASS_NAME, "instancename")
            m[0].click()
            try:
                try:
                    atmpt = driver.find_element(By.XPATH, "//tr[@class = 'bestrow lastrow']")
                except:
                    atmpt = driver.find_element(By.XPATH, "//tr[@class = 'bestrow']")

                atmpt.find_element(By.TAG_NAME, "a").click()

                print("page:", count)
                count += 1

            except:
                atmpt = driver.find_element(By.XPATH, "//tr[@class = 'lastrow']")

                atmpt.find_element(By.TAG_NAME, "a").click()
                print("page:", count)
                count += 1

            # page or a day's conetnt 5 - 2 questions is f_clearfix

            f_clearfix = driver.find_elements(By.XPATH, "//*[contains(@class, 'formulation clearfix')]")
            print("Clearfix ", len(f_clearfix))

            # inside a single page
            for i in range(0, len(f_clearfix)):
                q1 = f_clearfix[i].find_elements(By.TAG_NAME, 'p')
                q2 = f_clearfix[i].find_elements(By.TAG_NAME, 'h4')
                print("Questions: ", len(q1), len(q2))

                if len(q2) >= 2:
                    Q = q2[1].text
                    print(Q)
                    print("Heading")
                else:
                    for l in q1:
                        try:
                            if (len(l.text) > 0):
                                Q = l.text
                                print(Q)
                                break
                        except:
                            pass

                # Retrieving the Answer from the textarea
                try:
                    r = f_clearfix[i].find_elements(By.XPATH,
                                                    "/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[" + str(
                                                        i + 1) + "]/div[2]/div[1]/textarea")
                    A = r[0].get_attribute("value")
                    log[Q] = A
                    print("Answer in 1st meth")
                except:
                    r = f_clearfix[i].find_elements(By.XPATH, "//textarea[@class='coderunner-answer edit_code']")
                    A = r[i].get_attribute("value")
                    log[Q] = A
                    print("Answer 2nd meth")

                print("Answer loaded")

            print(log)

            print("done!! \n")


        except:
            driver.back()
            print("Except block")
            continue
        time.sleep(4)

        driver.back()

        time.sleep(4)

        driver.back()

    json_obj = json.dumps(log, indent=4)
    directory = './' + lang + '/'
    filename = f_name + ".json"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(file_path, "w") as op:
        op.write(json_obj)

    time.sleep(2)

