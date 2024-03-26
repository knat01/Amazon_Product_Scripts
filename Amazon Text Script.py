from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set window size

# Set the path to your chromedriver executable
driver_path = r"path\to\chromedriver.exe"
service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://chat.openai.com/?model=text-davinci-002-render-sha")
    
    input_element = driver.find_element(By.ID, "prompt-textarea")
    input_element.send_keys("Hello, I have a question.")
    
    send_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='send-button']")
    send_button.click()

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
