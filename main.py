import scraper
import analyze

if __name__ == "__main__":
    print("🔄 Mengumpulkan data dadu...")
    scraper.scrape_data()
    
    print("📊 Menganalisis hasil...")
    analyze.analyze_data()
