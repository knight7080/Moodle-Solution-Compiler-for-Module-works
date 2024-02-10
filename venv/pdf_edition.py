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


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

driver.get("http://training.saveetha.in/login/index.php")

rno = "21000045"
pas = "t65363"
mod_name = "TT JAVA MODULE-II"
u_btn = driver.find_element(By.NAME,"username")
u_btn.send_keys(rno)
p_btn = driver.find_element(By.NAME,"password")
p_btn.send_keys(pas)
time.sleep(4)
driver.find_element(By.ID,"loginbtn").click()
time.sleep(10)

driver.get("http://training.saveetha.in/?redirect=0")

driver.find_element(By.XPATH,"//a[text()='" + mod_name + "']").click()

quant = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")

wkhtmltopdf_options = {"enable-local-file-access": ""}

l = len(quant)

print(l)

log = {}

count = 1


for j in range(l):
        mods = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")

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
                count+=1

            except:
                atmpt = driver.find_element(By.XPATH, "//tr[@class = 'lastrow']")

                atmpt.find_element(By.TAG_NAME, "a").click()
                print("page:", count)
                count += 1

            page = driver.page_source.encode('utf-8')

            # res = "result" + str(j) + ".html"

            # Extracting content -- Starting

            # content = driver.find_elements(By.CLASS_NAME, "content")

            #page or a day's conetnt 5 - 2 questions is f_clearfix

            f_clearfix = driver.find_elements(By.XPATH, "//*[contains(@class, 'formulation clearfix')]")
            print("Clearfix ", len(f_clearfix))
            for i in range(0, len(f_clearfix)):
                q1 = f_clearfix[i].find_elements(By.TAG_NAME, 'p')
                q2 = f_clearfix[i].find_elements(By.TAG_NAME,'h4')
                print(len(q1),len(q2))
                r = f_clearfix[i].find_elements(By.XPATH, "//textarea[@class='coderunner-answer edit_code']")
                if len(q2) >= 2:
                    Q = q2[1].text
                    print(Q)
                else:
                    for l in q1:
                        try:
                            if (len(l.text) > 0):
                                Q = l.text
                                print(Q)
                                break
                        except:
                            pass

                A = r[i].get_attribute("value")
                log[Q] = A

            print(log)

            print("done!! \n")

            file = open('result.html', 'wb')

            file.write(page)

            file.close()


            # op_file = r'C:\Users\kaushik\PycharmProjects\moodle_doc\venv\output' + str(j) + '.pdf'
            #
            # pdfkit.from_file(r'C:\Users\kaushik\PycharmProjects\moodle_doc\venv\result.html', op_file,
            #                  options=wkhtmltopdf_options, verbose=True)
        except:
            driver.back()
            continue
        time.sleep(4)

        driver.back()

        time.sleep(4)

        driver.back()

# merger.merge_pdfs(l,mod_name)

# file_path = "venv/Java/J1.json"
#
#
# with open(mod_name + ".json","w") as op :
#     op.write(json_obj)

json_obj = json.dumps(log,indent = 4)
directory = './Java/'
filename = input() + ".json"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
with open(file_path,"w") as op :
    op.write(json_obj)

time.sleep(2)
driver.close()
driver.quit()