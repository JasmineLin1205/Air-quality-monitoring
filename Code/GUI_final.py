import folium
from folium.plugins import HeatMap
import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
import webview

def show_heatmap_aqi():
    # 讀取CSV檔案
    data = pd.read_csv(r'C:\Users\Jasmine\Documents\課程專題\python\data.csv')
    
   # 過濾掉缺失值（Num）
    data = data.dropna(subset=['aqi'])

    # 創建地圖對象
    m = folium.Map(location=[25.0330, 121.5654], zoom_start=10)
      
    heat_data = []
    for index, row in data.iterrows():
        latitude = row['latitude']
        longitude = row['longitude']
        aqi = row['aqi']

        # 根據 AQI 值指定顏色
        color = 0  # 將顏色改為數字表示
        if aqi >=20:
            color = 0.2
            if aqi >= 50:
                color = 0.5
                if aqi >= 100:
                    color = 1
                    if aqi >=150:
                        color = 1.5

        heat_data.append([latitude, longitude, color])
    # 建立熱力圖層時指定gradient參數為一個包含顏色的字典
    gradient = {0.0: 'deep green', 0.2:'light green', 0.5: 'yellow', 1.0: 'orange', 1.5: 'red'}  
    HeatMap(heat_data,gradient).add_to(m)
    
    # 保存地圖為HTML檔案
    m.save('heatmap.html')

    webview.create_window("Heatmap", url="heatmap.html", width=800, height=600)
    webview.start()
    
def show_heatmap_pm25():
    # 讀取CSV檔案
    data = pd.read_csv(r'C:\Users\Jasmine\Documents\課程專題\python\data.csv')
    
    data = data.dropna(subset=['pm2.5'])

    m = folium.Map(location=[25.0330, 121.5654], zoom_start=10)
      
    heat_data = []
    for index, row in data.iterrows():
        latitude = row['latitude']
        longitude = row['longitude']
        pm25 = row['pm2.5']

        # 根據 pm2.5 值指定顏色
        color = 0  # 將顏色改為數字表示
        if pm25 >= 15:
            color = 0.5
            if pm25 >= 30:
                color = 1
                if pm25 >= 35:
                    color = 1.5

        heat_data.append([latitude, longitude, color])

    # 定義一個包含顏色的漸層字典
    gradient = {0.0: 'deep green', 0.5: 'yellow', 1.0: 'orange', 1.5: 'red'}  

    HeatMap(heat_data,gradient).add_to(m)

    # 將地圖保存為HTML檔案
    m.save('heatmap_pm25.html')

    # 在webview中顯示熱力圖
    webview.create_window("PM2.5熱力圖", url="heatmap_pm25.html", width=800, height=600)
    webview.start()    

window = tk.Tk()
window.title("空氣品質監測GUI")
window.geometry("800x600")
window.configure(bg="#E4E7F0")

font_style = ("微軟正黑體", 28, "bold")

label = tk.Label(window, text="空氣品質監測", fg="#5D6A7D",
                bg="#E4E7F0",
                width=20, height=2,
                font=font_style)
label.pack()

# 載入圖片
image = Image.open(r'C:\Users\Jasmine\Documents\課程專題\python\taiwan.jpg') 
image = image.resize((300, 300))  # 調整圖片大小

# 將圖片轉換為Tkinter可用的圖像對象
photo = ImageTk.PhotoImage(image)

# 在視窗中創建標籤(Label)來顯示圖片
label = tk.Label(window, image=photo)
label.pack()

frame = tk.Frame(window, height=20)
frame.pack()

font_style = ("微軟正黑體", 14, "bold")
aqi_button = tk.Button(window, text="顯示AQI", command=show_heatmap_aqi, fg="white", bg="#5D6A7D", 
                       height=1, width=15, font=font_style)
aqi_button.pack()

frame = tk.Frame(window, height=20)
frame.pack()

button_font_style = ("微軟正黑體", 14, "bold")
pm25_button = tk.Button(window, text="顯示 PM2.5", command=show_heatmap_pm25, fg="white", bg="#5D6A7D", 
                        height=1, width=15, font=button_font_style)
pm25_button.pack()

window.mainloop()  
