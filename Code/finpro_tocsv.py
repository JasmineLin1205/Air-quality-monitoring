import requests
import csv

# API網址
url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"

# 發送HTTP GET請求並獲取API回應
response = requests.get(url)
data = response.json()

# 要保留的欄位名稱
fields = ["sitename", "county", "aqi", "pm2.5", "longitude", "latitude", "publishtime", "pm10"]

# 指定要儲存的CSV檔案路徑
csv_file = r"C:\Users\Jasmine\Documents\課程專題\python\data.csv"


# 開啟CSV檔案並寫入資料
with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    
    # 寫入CSV標頭
    writer.writerow(fields)
    
    # 寫入每一筆資料
    for item in data["records"]:
        row = [item[field] for field in fields]
        writer.writerow(row)

print("資料已成功儲存為CSV檔案。")
