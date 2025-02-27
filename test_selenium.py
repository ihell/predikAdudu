from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import config

# Setup Chrome Driver
service = Service(config.CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Mode tanpa GUI
driver = webdriver.Chrome(service=service, options=options)

# Coba buka Google
driver.get("https://www.google.com")
print("Selenium berhasil dijalankan! Halaman saat ini:", driver.title)

driver.quit()
