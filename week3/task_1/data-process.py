#網路連線
# import urllib.request as request
# import ssl
# import certifi

# context = ssl.create_default_context(cafile=certifi.where())
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src, context=context) as response:
#     data = response.read().decode("utf-8")
# print(data)

import urllib.request as request
import ssl
import certifi
import json
import csv
context = ssl.create_default_context(cafile=certifi.where())
assignment1_src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
assignment2_src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

district_list = ["中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區"]


with request.urlopen(assignment1_src, context=context) as assignment1_response:
    assignment1_data = json.load(assignment1_response) # 利用JSON模組處理資料格式
assignment1_clist = assignment1_data["data"]["results"]

with request.urlopen(assignment2_src, context=context) as assignment2_response:
    assignment2_data = json.load(assignment2_response) # 利用JSON模組處理資料格式
assignment2_clist = assignment2_data["data"]

with open("data_test.csv" , "w" , encoding="utf-8") as file:
    writer = csv.writer(file)
    
    for spot in assignment1_clist:
        title = spot["stitle"]
        longitude = spot["longitude"]
        latitude = spot["latitude"]
        filelist = spot["filelist"]
        info = spot["info"]
        
        first_image_url = "https"+filelist.split("https")[1]
       
        writer.writerow([title ,longitude,latitude,first_image_url])

        def info_to_station_name(info,)
    for spot in assignment2_clist:
        mrt = spot["MRT"]
        address = spot["address"]





with open("mrt.csv" , "w" , encoding="utf-8") as file:
    writer = csv.writer(file)
    
    for spot in assignment2_clist:
        mrt = spot["MRT"]
       
        writer.writerow([mrt])