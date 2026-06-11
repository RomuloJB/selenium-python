from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get('https://www27.receita.fazenda.gov.br/simulador-irpf/')

navegador.maximize_window()

botao_ano = navegador.find_element("id", "mat-select-0")

botao_ano.click()

lista_opcoes_ano = navegador.find_elements("class name", "mat-option-text")
for opcao in lista_opcoes_ano:
    if "2022" in opcao.text:
        opcao.click()
        break



time.sleep(10)