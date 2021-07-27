from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
  
# abrir ficheiro config
with open('config.json', encoding='utf-8-sig') as f:
    config = json.load(f)

is_marcado = False

while is_marcado==False:
    try:
        #chrome_options = Options() 
        #chrome_options.add_argument("headless") # TO DO: colocar a correr em modo headless

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(('https://covid19.min-saude.pt/pedido-de-agendamento/'))

        dia = browser.find_element_by_id('f_dia')
        dia.send_keys(str(config["dia"]))
        mes = browser.find_element_by_id('f_mes')
        mes.send_keys(str(config["mes"]))
        ano = browser.find_element_by_id('f_ano')
        ano.send_keys(str(config["ano"]))
        nextButton = browser.find_element_by_xpath("//input[@value='Validar']")
        nextButton.click()

        n_utente = browser.find_element_by_id('HealthcardNumber')
        n_utente.send_keys(str(config["n_utente"]))
        nome = browser.find_element_by_id('FullName') 
        nome.send_keys(str(config["nome"]))
        data = browser.find_element_by_id('BirthDate')
        data.send_keys(str(config["data"]))

        nextButton = browser.find_element_by_xpath("//button[@class='btn btn-primary submit-login g-recaptcha']")
        nextButton.click()

        distrito = browser.find_element_by_id('ddl_district_vac')
        distrito.send_keys(str(config["distrito"]))
        concelho = browser.find_element_by_id('ddl_county_vac')
        concelho.send_keys(str(config["concelho"]))

        time.sleep(3) # time sleep para dar tempo de as opções aparecerem

        local = browser.find_element_by_id('ddl_local_vac')
        local.send_keys(str(config["local"]))
        telefone1 = browser.find_element_by_id('txt_contacto_preferencial')
        telefone1.send_keys(str(config["telemovel"]))
        telefone2 = browser.find_element_by_id('repeat_txt_contacto_preferencial')
        telefone2.send_keys(str(config["telemovel"]))
        termos = browser.find_element_by_id('terms')
        termos.click()

        nextButton = browser.find_element_by_id('SubmitFormScheduleCovid19')
        nextButton.click()

        #submitdate
        #modal-slots-exit
        #modal-noslots-exit

        time.sleep(3) # time sleep para dar tempo de aparecer o pop up

        try:
            # este botão só aparece se houver datas, por isso se não existir é porque não há datas
            nextButton = browser.find_element_by_id('modal-slots-exit') 
            nextButton.click()
            nextButton = browser.find_element_by_id('submitdate')
            nextButton.click()   
            text_file = open("logs.txt", "a")
            text_file.write(time.strftime("%d/%m/%y %H:%M:%S") + ": Marcado!\n")
            text_file.close() 
            is_marcado = True
        except:
            text_file = open("logs.txt", "a")
            text_file.write(time.strftime("%d/%m/%y %H:%M:%S") + ": Nao ha datas\n")
            text_file.close()

        browser.close()
    except:
        text_file = open("logs.txt", "a")
        text_file.write(time.strftime("%d/%m/%y %H:%M:%S") + ": Erro\n")
        text_file.close()        

    time.sleep(int(config["periodicidade"]))