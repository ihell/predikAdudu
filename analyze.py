import pandas as pd

def analyze_data():
    try:
        df = pd.read_csv("data/hasil_prediksi.csv", names=["Dadu", "Timestamp"])
        
        df["Dadu"] = pd.to_numeric(df["Dadu"], errors="coerce")
        df.dropna(inplace=True)

        df["Kategori"] = df["Dadu"].apply(lambda x: "Dadu Kecil" if 9 <= x <= 31 else "Dadu Besar")

        print(df.tail())  # Menampilkan hasil terbaru

    except Exception as e:
        print("Gagal menganalisis data:", e)

if __name__ == "__main__":
    analyze_data()
