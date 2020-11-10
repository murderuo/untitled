import requests
from bs4 import BeautifulSoup as bs

def save_picture(link,img_name,auth,year,where):
    file_name=img_name+"-"+auth+","+year+"-"+where+'.jpg'
    Picture_request=requests.get(link)
    if Picture_request.status_code == 200:
        with open(file_name,'wb') as f:
            f.write(Picture_request.content)
    print("Picture saved..")

def save_details(detail,img_name,auth,year,where):
    file_name=img_name+"-"+auth+","+year+"-"+where+'.txt'
    with open(file_name,'w') as f:
        f.write(detail)
    print("details saved..")

def go_url(link):
    req=requests.get(link)
    html=req.content
    soup=bs(html,"html.parser")
    pageStatus=soup.find('img',attrs={'class':'share_image_image img-responsive'})['alt']
    if pageStatus=='DailyArt app, your daily dose of art getdailyart.com':


    print(pageStatus)
    div_item_specs=soup.find('div',attrs={'class':'share_title'})
    # print(div_item_specs)
    head=div_item_specs.h1.text
    author=div_item_specs.h1.next_sibling.next_sibling
    date=div_item_specs.h1.next_sibling.next_sibling.next_sibling.next_sibling
    where_place=div_item_specs.h1.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    details=soup.find('div',attrs={'class':'share_text'}).text

    # save_picture(url2,head,author.text,date.text,where_place.text)
    # save_details(details,head,author.text,date.text,where_place.text)

go_url('https://www.getdailyart.com/21964/unknown-artist/prayer-niche-(mihrab)')








# url="https://www.getdailyart.com/21965/unknown-artist/prayer-niche-(mihrab)#"
# url2='https://dailyartartwork.s3.amazonaws.com/jGjKQmNLpJ_ipad.jpg'



# div_item_specs_text=soup.find('div',attrs={'class':'share_title'}).text
# div_item_specs=soup.find('div',attrs={'class':'share_title'})
# head=div_item_specs.h1.text
# author=div_item_specs.h1.next_sibling.next_sibling
# date=div_item_specs.h1.next_sibling.next_sibling.next_sibling.next_sibling
# where_place=div_item_specs.h1.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling

# print(head)
# print(author.text)
# print(date.text)
# print(where_place.text)

