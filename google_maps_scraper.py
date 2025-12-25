from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

SEARCH_QUERY = "computer shop Sri Lanka"
SCROLL_COUNT = 8

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/maps")

time.sleep(5)

# Search
search_box = driver.find_element(By.ID, "searchboxinput")
search_box.send_keys(SEARCH_QUERY)
search_box.send_keys(Keys.ENTER)

time.sleep(6)

# Scroll results
scrollable = driver.find_element(By.XPATH, "//div[@role='feed']")
for _ in range(SCROLL_COUNT):
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        scrollable
    )
    time.sleep(3)

shops = driver.find_elements(By.CLASS_NAME, "hfpxzc")

data = []

for shop in shops:
    try:
        shop.click()
        time.sleep(4)

        name = driver.find_element(By.CLASS_NAME, "DUwDvf").text

        phone = "Not Available"
        address = "Not Available"

        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            label = btn.get_attribute("aria-label")
            if label:
                if "Phone" in label:
                    phone = label.replace("Phone:", "").strip()
                elif "Address" in label:
                    address = label.replace("Address:", "").strip()

        data.append([name, phone, address])
        print(f"{name} | {phone}")

    except Exception as e:
        print("Skipped:", e)

df = pd.DataFrame(data, columns=["Shop Name", "Phone", "Address"])
df.to_csv("sri_lanka_computer_shops.csv", index=False, encoding="utf-8-sig")

driver.quit()
print("✅ Phone numbers & addresses saved correctly")
