import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="session") # o fixture é uma configuração que é executada antes de cada teste, e o scope session significa que ele será executado apenas uma vez por sessão de teste
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # rodar o navegador em modo headless (sem interface gráfica)
    navegador = webdriver.Chrome(options=options)
    yield navegador
    navegador.quit()

@pytest.fixture(scope="session")
def driver_visivel():
    navegador = webdriver.Chrome()
    yield navegador
    time.sleep(10)
    navegador.quit()
