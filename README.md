# 📰 Stock News Scraper (Naver & Google)

This is a desktop-based Python script that allows users to **search stock-related news articles** from **Naver News** and **Google News**  
by entering either a **stock name** or a **stock code**.  
It is designed to be used with an Excel file (`code_name.xlsx`) containing NASDAQ stock names and codes.

> ⚠️ This project is for **educational and research use only.**  
> It does **not store personal data**, and no responsibility is taken for financial decisions based on its output.

---

## 📌 Features

- Keyword search via GUI (using `pyautogui.prompt`)
- Automatic stock name-code matching from Excel
- News search results from:
  - 🔎 **Naver News**
  - 🔎 **Google News**
- Supports both **stock name** and **ticker code** input
- No browser pop-ups (Selenium headless mode)
- Outputs URLs and titles to the console

---


## ⚙️ How It Works

1. The script loads an Excel file (`code_name.xlsx`) containing NASDAQ stock names and ticker codes.
2. When the script runs, a GUI prompt appears:
   - If the user enters `'1'`, they can search for a stock using a keyword (e.g., "apple").
   - The program matches the keyword against stock names and codes in the Excel file.
   - If the user enters a valid name or code directly, it skips the matching step.
3. The user is then prompted to enter how many pages of news to retrieve.
4. The script performs a web scraping process:
   - Searches **Naver News** by both the matched **stock name** and **code**.
   - Searches **Google News** using Selenium (headless mode) for both the name and code.
5. All news titles and URLs are printed to the console in an organized format.
6. The script loops, allowing repeated searches.

> 📌 Note: This script only displays results in the terminal; it does not store any data.


---


## 📁 Directory Structure

```plaintext
.
├── code_name.xlsx       # Excel file with stock names and codes (required)
├── news_scraper.py      # Main Python script
└── README.md
```


---

## ⚙️ Requirements

- Python 3.8+
- Chrome browser
- ChromeDriver installed (must match Chrome version)

Install required packages:
```bash
pip install -r requirements.txt
