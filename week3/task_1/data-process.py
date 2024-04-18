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
import re
context = ssl.create_default_context(cafile=certifi.where())
assignment1_src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
assignment2_src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"




with request.urlopen(assignment1_src, context=context) as assignment1_response:
    assignment1_data = json.load(assignment1_response) # 利用JSON模組處理資料格式
assignment1_clist = assignment1_data["data"]["results"]

with request.urlopen(assignment2_src, context=context) as assignment2_response:
    assignment2_data = json.load(assignment2_response) # 利用JSON模組處理資料格式
assignment2_clist = assignment2_data["data"]

spot_data = []
assignment1_serial_location = {}
assignment2_serial_district = {}
assignment2_mrt_serial = {}
pattern = r'\w+區'

for spot in assignment1_clist:
        title = spot["stitle"]
        longitude = spot["longitude"]
        latitude = spot["latitude"]
        filelist = spot["filelist"]
        info = spot["info"]
        serial_no1 = spot["SERIAL_NO"]
        
        first_image_url = "https"+filelist.split("https")[1]
        serial_no1_district = assignment2_serial_district.get(serial_no1)  
        
        if title not in assignment1_serial_location:
             assignment1_serial_location[serial_no1] = [title]
        else:
             assignment1_serial_location[serial_no1].append(title)
       


        spot_data.append([title ,serial_no1_district,longitude,latitude,first_image_url])
# print(assignment1_serial_location)
# for all_key in spot_data:
#     print(all_key)

for spot in assignment2_clist:
        serial_no2 = spot["SERIAL_NO"]
        address = spot["address"]
        mrt = spot["MRT"]

        #使用re.search搭配group()
        matching_no2_district = re.search(pattern,address)
        no2_district = matching_no2_district.group()
        assignment2_serial_district[serial_no2] = no2_district

        if mrt in assignment2_mrt_serial:
             assignment2_mrt_serial[mrt].append(serial_no2)
        else:
             assignment2_mrt_serial[mrt] = [serial_no2]



# print(assignment2_mrt_serial)
# for key , value in assignment2_serial_district.items():
#     print(key ,value)



#清單1和清單2的序號互相比較
for mrt , serials in assignment2_mrt_serial.items():
    updated_serials = []
    for serial in serials :
        if serial in assignment1_serial_location :
            updated_serials.extend(assignment1_serial_location[serial])
        else:
            updated_serials.append(serial)
    assignment2_mrt_serial[mrt] = updated_serials




with open("spot.csv" , "w" , encoding="utf-8") as file:
    writer = csv.writer(file)
    for data in spot_data:
        writer.writerow(data)

with open("mrt.csv" , "w" , encoding="utf-8") as file:
    writer = csv.writer(file)
    # max_len = max(len(serials) for serials in  assignment2_mrt_serial.values())
    # header = ["MRT Station"] + [f"Spot {i+1}" for i in range(max_len)]
    # writer.writerow(header)
    for mrt_station, spot in assignment2_mrt_serial.items():
        row = [mrt_station] + spot
        writer.writerow(row)
    
    