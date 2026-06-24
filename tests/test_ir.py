import time
from selenium.webdriver.common.by import By

# definindo o url da pagina que sera testada
URL_BASE = 'https://www27.receita.fazenda.gov.br/simulador-irpf/'

# teste para verificar se o ambiente de teste está configurado corretamente
def test_ambiente():
    assert True

def selecionar_ano(driver_visivel):
    driver_visivel.get(URL_BASE)
    driver_visivel.maximize_window()
    botao_ano = driver_visivel.find_element("id", "mat-select-value-1")
    botao_ano.click()
    lista_opcoes_ano = driver_visivel.find_elements(By.CLASS_NAME, "mat-option-text")
    for opcao in lista_opcoes_ano:
        if "2022" in opcao.text:
            opcao.click()
            break

def selecionar_rendimento(driver_visivel, valor_rendimento):
    botao_rendimentos = driver_visivel.find_element(By.ID, "mat-input-0")
    botao_rendimentos.send_keys(valor_rendimento)

# def scroll_to_element(driver_visivel, element):
#     driver_visivel.execute_script("arguments[0].scrollIntoView();", element)

def test_ir_isento(driver_visivel):
    # Arrange
    aliquota_esperada = "0,00"
    parcela_a_deduzir_esperada = "0,00"
    valor = "190397"

    selecionar_ano(driver_visivel)

    # Act
    time.sleep(3)
    selecionar_rendimento(driver_visivel, valor)

    # Assert
    time.sleep(3)
    aliquota_obtida = driver_visivel.find_element(By.CLASS_NAME, "card-result-input")
    parcela_a_deduzir_obtida = driver_visivel.find_element(By.TAG_NAME, "card-subtitle-input.card-result-input")

    assert aliquota_obtida.text == aliquota_esperada
    assert parcela_a_deduzir_obtida.text == parcela_a_deduzir_esperada

    time.sleep(2)
