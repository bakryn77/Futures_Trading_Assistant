from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_to_topstep(username, password):
    print("[INFO] Launching browser...")

    # 1. Start Chrome browser using WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 2. Open Topstep login page
    driver.get("https://app.topstepx.com/login")

    wait = WebDriverWait(driver, 20)

    # 3. Wait for the email input box to appear
    email_box = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_box.send_keys(username)
    print("[INFO] Typed email.")

    # 4. Wait for password input
    password_box = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_box.send_keys(password)
    print("[INFO] Typed password.")

    # 5. Find Login button and click it
    login_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Log In')]")
        )
    )
    login_btn.click()
    print("[INFO] Clicked login.")

    return driver
