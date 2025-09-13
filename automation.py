from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# Load credentials from config.json
with open('config.json', 'r') as file:
    config = json.load(file)

username = config['username']
password = config['password']

# Setup Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

try:
    # Step 1: Open Flipkart
    driver.get("https://www.flipkart.com/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Login process
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]")))
    close_button.click()

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]")))
    login_button.click()

    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='_2IX_2- VJZDxU']")))
    username_input.send_keys(username)

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    time.sleep(5)

    # Step 3: Search for a product
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("smartphone")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Select first product
    first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'_1fQZEK')])[1]")))
    first_product.click()

    driver.switch_to.window(driver.window_handles[1])

    # Step 5: Add to cart
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]")))
    add_to_cart.click()

    time.sleep(3)

    # Step 6: Proceed to checkout
    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Cart')]")))
    cart_button.click()

    proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Place Order')]")))
    proceed_button.click()

    # Step 7: Select payment method (example: Net Banking)
    time.sleep(3)
    payment_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='NET_BANKING']")))
    payment_option.click()

    # Step 8: Enter dummy payment details (optional simulation)

    # Step 9: Validate navigation to OTP page
    otp_page = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Enter OTP')]")))
    assert otp_page.is_displayed()

    print("Test case passed: Reached OTP page successfully.")

except Exception as e:
    print("Test case failed:", e)

finally:
    time.sleep(5)
    driver.quit()
