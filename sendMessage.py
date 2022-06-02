from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import time

def findButtonSend(driver):
    try:
        time.sleep(10)
        user = driver.find_element_by_class_name("_1U1xa")
        user.click()
        return True    
    except:
        try:
            alert = driver.find_element_by_class_name("FV2Qy")
            alert.click()
            return False
        except:
            findButtonSend(driver)
        
def sendMessage(number, message, driver, paciente):
    url = "https://web.whatsapp.com/send?phone=%s&text=%s" %(number,message)
    driver.get(url)
    time.sleep(5)
    try:
        alert = driver.switch_to_alert
        alert.accept()
    except:
        pass
    if not findButtonSend(driver):
        listarNumerosComErro(number, paciente)
    time.sleep(5)
    

def initialize():
    driver = webdriver.Chrome(executable_path="%s/chrome/chromedriver.exe" % os.path.curdir)
    return driver

def listarNumerosComErro(number, paciente):
    desktop = Path.home() / "Desktop"
    lista = open('%s\lista.txt'%desktop,'a')
    lista.writelines('%s: %s\n' %(paciente,number))
    lista.close()
'''driver = initialize()
msg = """Secretaria Municipal de Saúde de Bragança Paulista-SP                                             
\nInformamos que *%s* tem um *%s* de *%s* no dia *%s* às *%s* agendado no *AME em Atibaia*. 
Favor confirmar a presença ou ausência *48 horas antes do agendamento*. 
E se já está com a guia do agendamento(se acaso não estiver, é só retirar no posto de saúde)
Muito Obrigado.
\n'A sua presença é muito importante para o tratamento da sua patologia e também para diminuir o absenteísmo (falta) no serviço que o SUS oferta.'"""
msg = msg %('bruno','exame','cardio','20/09/2020', '12:00')        
sendMessage('5511943790826',msg, driver)'''
'''driver = initialize()
sendMessage('5511000000000000000',"oi", driver)'''