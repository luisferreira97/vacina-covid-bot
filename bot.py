from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

is_marcado = False

while is_marcado==False:
    try:
        #chrome_options = Options() 
        #chrome_options.add_argument("headless") # TO DO: colocar a correr em modo headless

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(('https://covid19.min-saude.pt/pedido-de-agendamento/'))

        dia = browser.find_element_by_id('f_dia')
        dia.send_keys("16") ######### MUDAR AQUI
        mes = browser.find_element_by_id('f_mes')
        mes.send_keys("7") ######### MUDAR AQUI
        ano = browser.find_element_by_id('f_ano')
        ano.send_keys("1998") ######### MUDAR AQUI
        nextButton = browser.find_element_by_xpath("//input[@value='Validar']")
        nextButton.click()

        n_utente = browser.find_element_by_id('HealthcardNumber')
        n_utente.send_keys("179961812") ######### MUDAR AQUI
        nome = browser.find_element_by_id('FullName') 
        nome.send_keys("Tiago de Faria Ferreira") ######### MUDAR AQUI
        data = browser.find_element_by_id('BirthDate')
        data.send_keys("16/07/1998") ######### MUDAR AQUI

        nextButton = browser.find_element_by_xpath("//button[@class='btn btn-primary submit-login g-recaptcha']")
        nextButton.click()

        distrito = browser.find_element_by_id('ddl_district_vac')
        distrito.send_keys("Braga") ######### MUDAR AQUI
        concelho = browser.find_element_by_id('ddl_county_vac')
        concelho.send_keys("Vila Verde") ######### MUDAR AQUI

        time.sleep(3) # time sleep para dar tempo de as opções aparecerem

        local = browser.find_element_by_id('ddl_local_vac')
        local.send_keys("USF Prado") ######### MUDAR AQUI
        telefone1 = browser.find_element_by_id('txt_contacto_preferencial')
        telefone1.send_keys("963864511") ######### MUDAR AQUI
        telefone2 = browser.find_element_by_id('repeat_txt_contacto_preferencial')
        telefone2.send_keys("963864511") ######### MUDAR AQUI
        termos = browser.find_element_by_id('terms')
        termos.click()

        nextButton = browser.find_element_by_id('SubmitFormScheduleCovid19')
        nextButton.click()

        #submitdate
        #modal-slots-exit
        #modal-noslots-exit

        time.sleep(3) # time sleep para dar tempo de aparecer o pop up

        try:
            nextButton = browser.find_element_by_id('modal-slots-exit') # este botão só aparece se houver datas
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

    time.sleep(600) ######### MUDAR AQUI periodicidade 