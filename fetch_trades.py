from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_trades(driver):
    print("[INFO] Navigating to Trade Log...")

    wait = WebDriverWait(driver, 20)

    # 1. Click the "Performance" tab
    performance_tab = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(), 'Performance')]")
        )
    )
    performance_tab.click()
    print("[INFO] Opened Performance tab.")

    # 2. Wait for the trade table to appear
    table = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table")
        )
    )
    print("[INFO] Table loaded.")

    # 3. Collect all rows from the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    trades = []

    # 4. Loop through each row
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")

        # Skip header rows (no data)
        if len(cols) < 5:
            continue

        trade = {
            "date": cols[0].text,
            "instrument": cols[1].text,
            "entry": cols[2].text,
            "exit": cols[3].text,
            "pnl": cols[4].text
        }

        trades.append(trade)

    print(f"[INFO] Extracted {len(trades)} trades.")
    return trades
