from selenium import webdriver
from time import sleep



browser = webdriver.Edge(executable_path='./driver/msedgedriver')

def validar_qr():
    try:
        browser.find_element_by_tag_name("canvas")
    except Exception as e:
        return False
    return True


def bot_whatsapp():

    browser.get('https://web.whatsapp.com')
    sleep(5)

    validar = True 

    while validar:
        print("validando QR")
        validar = validar_qr()
        sleep(3)
        if validar == False:
            print("iniciamos sesión")
            break
    
        

bot_whatsapp()
