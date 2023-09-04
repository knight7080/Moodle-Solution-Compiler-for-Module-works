from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable

chrome_driver_path = 'C:/path/to/chromedriver.exe'

# Set Chrome options for headless mode and to disable printing prompts
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--print-to-pdf=output.pdf')
# Specify the ChromeDriver executable path in the service

# Create a Chrome WebDriver instance using the service and options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the webpage you want to save as PDF
driver.get('https://google.com')

# Execute JavaScript to trigger printing (without the print dialog)
driver.execute_script('window.print();')

# Wait for a few seconds to ensure that the PDF is generated
import time
time.sleep(5)  # Adjust the delay as necessary

# Close the WebDriver
driver.quit()
