import os
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Coba import config jika ada
try:
    import config
    CHROME_DRIVER_PATH = config.CHROME_DRIVER_PATH
    SOURCE_URL = config.SOURCE_URL
except ImportError:
    print("⚠️  File config.py tidak ditemukan, gunakan nilai default!")
    CHROME_DRIVER_PATH = "C:/Users/ThinkPad/downloads/chromedriver.exe"  # Ganti dengan path chromedriver yang benar
    SOURCE_URL = "https://www.google.com/search?q=lemparan+dadu" # Ganti dengan URL sumber yang benar

# Setup Chrome Driver
service = Service(CHROME_DRIVER_PATH)
options = Options()
options.add_argument("--headless")  # Mode tanpa GUI
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Buat folder "data" jika belum ada
os.makedirs("data", exist_ok=True)

def scrape_data():
    """Mengambil data dari website dan menyimpannya ke CSV"""
    try:
        print("🔄 Mengakses halaman...")
        driver.get(SOURCE_URL)

        # Tunggu elemen muncul sebelum mengambil data (update selector sesuai kebutuhan)
        wait = WebDriverWait(driver, 10)  # Maksimal tunggu 10 detik
        dadu_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "selector-untuk-dadu")))
        
        hasil_dadu = dadu_elem.text
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Simpan hasil ke CSV
        csv_file = "data/hasil_prediksi.csv"
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([hasil_dadu, timestamp])

        print(f"✅ Data berhasil disimpan: {hasil_dadu} ({timestamp})")

    except Exception as e:
        print(f"❌ Gagal mengambil data: {e}")

    finally:
        driver.quit()
        print("🚪 Browser ditutup.")

if __name__ == "__main__":
    scrape_data()
