from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



browser = webdriver.Edge(executable_path='./driver/msedgedriver')

def validar_qr():
    try:
        browser.find_element(By.TAG_NAME, 'canvas')
    except Exception as e:
        return False
    return True

def buscar_chat(nombre : str):
    buscando = True

    while buscando:
        print("BUSCANDO CHAT")
        elements = browser.find_elements(By.TAG_NAME, 'span')
        for element in elements:
            if element.text == nombre:
                print("Chat encontrado")
                element.click()
                buscando = False
                break




def enviar_mensaje(mensaje:str):

    
    chat = browser.find_element(By.CLASS_NAME, 'p3_M1')
    chat.send_keys(mensaje+ Keys.ENTER)
    print("SE ESCRIBIÓ EL MENSAJE")
    sleep(2)

    """
    enviar = browser.find_element(By.TAG_NAME, 'button')
    enviar.click()
    print("SE ENVIO EL MENSAJE")
    """

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
    
    sleep(20)
    buscar_chat("Hermanita Heidy")
    sleep(5)
    enviar_mensaje("Hola")
        

bot_whatsapp()
