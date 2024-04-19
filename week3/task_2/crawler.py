import urllib.request as request
import ssl
import certifi
import bs4
import csv


context = ssl.create_default_context(cafile=certifi.where())

def get_every_page_info(every_article_url):
        req = request.Request(every_article_url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Cookie":"over18=1"
    })
        with request.urlopen(req,context=context) as response:
            data=response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data,"html.parser")
        
        # 尋找文章的時間
        publish_time = None
        metalines = root.find_all("div" , class_="article-metaline")
        for metaline in metalines:
             meta_tag = metaline.find("span" , class_="article-meta-tag")
             if meta_tag and meta_tag.text == "時間":
                  meta_value = metaline.find("span", class_="article-meta-value")
                  if meta_value:
                       publish_time = meta_value.text

        
        like_count = 0 
        dislike_count = 0 
        push_tags = root.find_all("span", class_="hl push-tag")
        for tag in push_tags:
            if tag.text.strip() == "推":
                like_count+=1
            elif tag.text.strip() == "噓":
                dislike_count+=1
        return publish_time , like_count , dislike_count


def get_data(url):
    data_storage = []
    req = request.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Cookie":"over18=1"
    })
    with request.urlopen(req,context=context) as response:
        data=response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"html.parser")

    titles = root.find_all("div" , class_="title")
    for title in titles:
        if title.a is not None:
            article_title = title.a.string.strip()
            article_url =  "https://www.ptt.cc" + title.a["href"]
            publish_time , like_count , dislike_count = get_every_page_info(article_url)
            data_storage.append([article_title,f"{like_count}/{dislike_count}",publish_time])

    next_link = root.find("a", string="‹ 上頁")
    if next_link:
         next_page_url = "https://www.ptt.cc" + next_link["href"]
    return  data_storage , next_page_url


all_data = []
page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
page_count = 0

while page_url and page_count<3:
    current_data , next_page_url = get_data(page_url)
    all_data.extend(current_data)
    page_url = next_page_url
    page_count += 1

with open("task_2/article.csv" , "w" , encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(all_data)