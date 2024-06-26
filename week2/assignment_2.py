# === Task 1 ===
print("=== Task 1 ===")
def find_and_print(messages, current_station):
    station_map_list = (
        "Xiaobitan",
        "Songshan",
        "Nanjing Sanmin",
        "Taipei Arena",
        "Nanjing Fuxing",
        "Songjiang Nanjing",
        "Zhongshan",
        "Beimen",
        "Ximen",
        "Xiaonanmen",
        "Chiang Kai-Shek Memorial Hall",
        "Guting",
        "Taipower Building",
        "Gongguan",
        "Wanlong",
        "Jingmei",
        "Dapinglin",
        "Qizhang",
        "Xindian City Hall",
        "Xindian",
    )
    def transform_current_station(current_station,station_map_list):
        for index , station_name in enumerate(station_map_list):
            if station_name == current_station:
                return index
        return None
    def transform_message_data(messages,station_map_list):
        name_and_station_newdata = {}
        for person , description in messages.items():
            for index , station_name in enumerate(station_map_list):
                if station_name in description:
                    name_and_station_newdata[person] = index
        return name_and_station_newdata

    user_station_index = transform_current_station(current_station,station_map_list)
    friend_new_data = transform_message_data(messages,station_map_list)
    closest_friend = None
    min_distance = float("inf")
    for friend , friend_station_index in friend_new_data.items():
        #比較朋友的索引位置
        if friend_station_index == 0 :
            distance = abs(17 - user_station_index) + 1
        elif user_station_index == 0 :
            distance =  abs(friend_station_index - 17 ) + 1
        elif friend_station_index == 0 and user_station_index == 0 :
            distance = 0
        else:
            distance = abs(friend_station_index - user_station_index)

        if distance < min_distance :
            min_distance = distance
            closest_friend = friend
    return closest_friend

messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.", 
    "Copper":"I just saw a concert at Taipei Arena.", 
    "Vivian":"I'm at Xindian station waiting for you."
}
print(find_and_print(messages, "Wanlong")) # print Mary 
print(find_and_print(messages, "Songshan")) # print Copper 
print(find_and_print(messages, "Qizhang")) # print Leslie 
print(find_and_print(messages, "Ximen")) # print Bob 
print(find_and_print(messages, "Xindian City Hall")) # print Vivian
# === Task 2 ===
print("=== Task 2 ===")

def book(consultants, hour, duration, criteria):
    
    if criteria == "rate" :
        sorted_consultants = sorted(consultants,key=lambda x:x["rate"],reverse = True)
    elif criteria == "price" :
        sorted_consultants = sorted(consultants,key=lambda x:x["price"])
    

    for consultant in sorted_consultants:
        consultant_name = consultant["name"]
        matched_consultant = dictionary_forConsultants[consultant_name]
        is_available = True;
        
        for i in range(hour, hour + duration):
            if not matched_consultant["hour"][i]:
                is_available = False;
                break
        if is_available : 
            for i in range(hour, hour + duration):
                matched_consultant["hour"][i] = False
            return consultant["name"]
    
    return "No service"

consultants = [
    {"name":"John", "rate":4.5, "price":1000}, 
    {"name":"Bob", "rate":3, "price":1200}, 
    {"name":"Jenny", "rate":3.8, "price":800}
]
consultant_availability = [
    {
        "name":consultant["name"],
        "hour":{hour:True for hour in range(9,22)}
    }   for consultant in consultants
]
dictionary_forConsultants = {}
for i in consultant_availability:
    dictionary_forConsultants[i["name"]] = {"hour" : i["hour"]}

print(book(consultants, 15, 1, "price")) # Jenny 
print(book(consultants, 11, 2, "price")) # Jenny 
print(book(consultants, 10, 2, "price")) # John 
print(book(consultants, 20, 2, "rate")) # John 
print(book(consultants, 11, 1, "rate")) # Bob 
print(book(consultants, 11, 2, "rate")) # No Service 
print(book(consultants, 14, 3, "price")) # John


# === Task 3 ===
print("=== Task 3 ===")
def func(*data):
    compare_list = []
    unique_count = 0
    unique_friend =[]
    
    for x in data :
        char_to_compare = []
        if len(x) == 2 or len(x) == 3 :
            char_to_compare = x[1]
        else :
            char_to_compare = x[2]
        compare_list.append({"name" : x , "char": char_to_compare })

    for i in compare_list :
        count = 0
        for j in compare_list : 
            if i["char"] == j["char"] :
                count += 1
        if count == 1 :
            unique_count += 1 
            unique_friend.append(i["name"])
            result = ",".join(unique_friend)

            
    if unique_count == 0 :
        return "沒有"
    return  result

print(func("彭大牆", "陳王明雅", "吳明","郭靜雅"))
print(func("彭大牆", "陳王明雅", "吳明")) # print 彭大牆
print(func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")) # print 林花花 
print(func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")) # print 沒有 
print(func("郭宣雅", "夏曼藍波安", "郭宣恆")) # print 夏曼藍波安

# === Task 4 ===
print("=== Task 4 ===")

def get_number(index):

    arr = [0]
    if index == 0 :
        return 0
    i = 1
    while i <= index:
        arr.append(0)
        if i % 3 == 0 :
            arr[i] = arr[i-1] - 1
        else:
            arr[i] = arr[i-1] + 4
        i += 1
    return arr[index]
    



print(get_number(1)) # print 4
print(get_number(5)) # print 15 
print(get_number(10)) # print 25 
print(get_number(30)) # print 70

# === Task 5 ===
print("=== Task 5 ===")

def find(spaces, stat, n):
   

    spaces_turn_check_available = []
    
    for i in spaces:
        if i >= n:
            spaces_turn_check_available.append(i)
        else:
            spaces_turn_check_available.append("No service")
   
    
    for key , value in enumerate(stat):
        if(value == 0):
            spaces_turn_check_available[key] = "No service"
   
    
    min_seat = float("inf")
    available_seat = ""

    for index , value in enumerate(spaces_turn_check_available):
        if value == "No service":
            continue
        
        seat = value - n

        if seat <= min_seat :
            min_seat = seat
            available_seat = index
    if available_seat == "" :
        return -1
    return available_seat

print(find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2)) # print 5 
print(find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)) # print -1 
print(find([4, 6, 5, 8], [0, 1, 1, 1], 4)) # print 2
