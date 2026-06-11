from selenium import webdriver
import time
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.get('https://www27.receita.fazenda.gov.br/simulador-irpf/')

navegador.maximize_window()

botao_ano = navegador.find_element("id", "mat-select-0")

botao_ano.click()

lista_opcoes_ano = navegador.find_elements(By.CLASS_NAME, "mat-option-text")
for opcao in lista_opcoes_ano:
    if "2022" in opcao.text:
        opcao.click()
        break

#campo rendimentos tributaveis
botao_rendimentos = navegador.find_element(By.CLASS_NAME, "mat-form-field-autofill-control")
botao_rendimentos.send_keys("150000")

botao_previdencia = navegador.find_element(By.ID, "mat-input-1")
#fazer o selenium dar um scroll para baixo e encontrar e centralizar o elemento desejado
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_previdencia)
time.sleep(3)
#campo previdencia
navegador.find_element(By.ID, "mat-input-1").send_keys("1000")

botao_dependentes = navegador.find_element(By.ID, "mat-input-2")
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_dependentes)
time.sleep(3)
#campo dependentes
navegador.find_element(By.ID, "mat-input-2").send_keys("1000")

botao_pensao = navegador.find_element(By.ID, "mat-input-3")
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_pensao)
time.sleep(3)
#campo pensao alimenticia
navegador.find_element(By.ID, "mat-input-3").send_keys("1000")

botao_outras_deducoes = navegador.find_element(By.ID, "mat-input-4")
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_outras_deducoes)
time.sleep(3)
#campo outras deducoes
navegador.find_element(By.ID, "mat-input-4").send_keys("1000")

time.sleep(10)