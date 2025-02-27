from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path ke ChromeDriver
chrome_driver_path = r"C:\Users\ThinkPad\Downloads\chromedriver-win64\chromedriver.exe"

# Inisialisasi driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Buka halaman hasil dadu di Google
url = "https://www.google.com/search?si=APYL9bsmP4tYr6TlA_hIJp-E39rUuK-V3ZVI8d4eBZz16GMgZZCMDFCUzfsZj1EzdKBXn1SlMH1puugDcm8KYg-lC41akIeiR-BDihjADo9lm1tGf8sek-LDiw7B6i0bLJRgJ3PRJKpsPPUqf8ntiZhHd6tSlFnWC-BX9dUQC92czBoTyv2UzQTAOleE5bfganJlrEGNMIM69A27KdwmUd2C2etq4YnMl4BrnDXyUbVxNYP4n-FStsgriROuVcB1PYqnMJxWc7wPLQSXsmkXXtS2NbGzwXGQ1BIC3j797-8ZWgQAeSShBvGN1gUOgqg56k6EX3K9v1qrqMlzThqhwHB_EkJRhUqP6GMKDhGRJVa3MYFaTKztEhBVROi95cZG3PnA_VYsD9dWRMu3U7xnRF_dornFcjknWFJUjyjlt2pM-k_SzQ8wOtydlGkCdXYoofqy2oUSGDb4J1U_md6UF9Mcg6wtE0AN0PTtTmtS2yRhoAWUL5AU1fCLXFl3vbV4Lm89wPZR4qiJFvMGhxfGFP3S3kWP25Mv2Q%3D%3D&hl=id-ID&shndl=21&source=sh%2Fx%2Ffbx%2Fm1%2F2&kgs=d125faaacc6e5e29"
driver.get(url)

# Tunggu halaman dimuat
time.sleep(5)

# Cari elemen angka dadu di halaman (Harus menyesuaikan dengan HTML halaman)
try:
    dadu_element = driver.find_element(By.CLASS_NAME, "class_yang_mengandung_angka_dadu")  # Sesuaikan class ini
    angka_dadu = int(dadu_element.text)

    # Tentukan kategori dadu
    kategori = "Kecil" if angka_dadu <= 31 else "Besar"

    # Tampilkan hasil
    print(f"Angka Dadu: {angka_dadu}")
    print(f"Kategori: {kategori}")

except Exception as e:
    print("Gagal mengambil data dadu:", e)

# Tutup browser
driver.quit()
