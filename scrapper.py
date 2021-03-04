import requests
import smtplib
from bs4 import BeautifulSoup
url = 'https://www.amazon.in/Lenovo-Tab-M10-FHD-Plus/dp/B08BZSR4TX?ref_=Oct_DLandingS_D_827b4554_60&smid=A14CZOWI0VEHLG'
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('<youremailid>','**********')
    subject = 'Price fell down'
    body = 'check the amazon link asap https://www.amazon.in/Lenovo-Tab-M10-FHD-Plus/dp/B08BZSR4TX?ref_=Oct_DLandingS_D_827b4554_60&smid=A14CZOWI0VEHLG'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        '<from email>',
        '<to email>',
        msg
    )
    print('Mail Sent!')
    server.quit()
def check_price():
    page = requests.get(url,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id = "priceblock_dealprice").get_text().strip()
    new_price = ''.join([i for i in price[2:-2] if i.isdigit()])
    if(int(new_price) <= 18000):
        send_mail()
    print(new_price)
    print(title)
    


check_price()