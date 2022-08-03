
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



def validar_mensaje_leido(elem):
    try:
        elem.find_element(By.CLASS_NAME, '_1pJ9J')
    except Exception as e:
        return False
    return True




def buscar_chat():
   
    if len(browser.find_elements(By.CLASS_NAME, 'zaKsw'))==0:
        print("chat abierto")

    print("BUSCANDO MENSAJES RECIBIDOS")
    elements_general = browser.find_elements(By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/div[12]')

    for element in elements_general:
        print("buscando mensajes sin leer")

        chat_abierto = element.find_elements(By.CLASS_NAME, '_1pJ9J')

        if len(chat_abierto) == 0:
            print("Ya se leyo el chat")

        element.click()
        print("chat abierto")



def enviar_mensaje(mensaje:str):

    
    chat = browser.find_element(By.CLASS_NAME, 'p3_M1')
    chat.send_keys(mensaje+ Keys.ENTER)
    print("SE ESCRIBIÓ EL MENSAJE")
    sleep(2)
    enviar = browser.find_element(By.TAG_NAME, 'button')
    enviar.click()
    print("SE ENVIO EL MENSAJE")

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
    
    sleep(10)
    buscar_chat()

        

bot_whatsapp()
