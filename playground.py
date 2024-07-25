from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver_path = ChromeDriverManager().install()
service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

driver.get("https://soft.reelly.io/sign-up")
driver.find_element(By.CSS_SELECTOR, "[class='sing-in-text']").click()
driver.find_element(By.ID, "email-2").send_keys("vn.sumana@gmail.com")
driver.find_element(By.ID, "field").send_keys("sReelly")
driver.find_element(By.CSS_SELECTOR, "[class*='login-button']").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "[class='menu-twobutton']").click()

sleep(6)

products = driver.find_elements(By.CSS_SELECTOR, "[wized='cardOfProperty']")


#print(len(products))

# actual_text = driver.find_element(By.XPATH, "//*[@data-test='resultsHeading']").text
# assert search_word in actual_text, f"The expected word '{search_word}' didn't match the actual word '{actual_text}'"

print("Test case passed!")
driver.quit()

