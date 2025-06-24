from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.spotrac.com/nba/cap/_/year/2025"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")

teamSalaryTable = soup.find("table", class_="table dataTable premium")

headers = [th.text.strip() for th in teamSalaryTable.find_all("th")]

rows = []
for row in teamSalaryTable.find_all("tr")[1:]:
    cells = [td.text.strip() for td in row.find_all("td")]
    rows.append(cells)

df = pd.DataFrame(rows, columns=headers)

df.to_csv("team_caps_2025.csv", index=False)

