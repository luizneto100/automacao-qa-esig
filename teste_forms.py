from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Configura e abre o navegador automaticamente
print("Abrindo navegador...")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# 2. Acessa o Formulário
navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSdaTu50nME8M-mJA4j5AIWFryU7o_b6qGgQmLockSeXMNEh6A/viewform?pli=1")

# Dá 3 segundos pro Google Forms carregar a página inteira
time.sleep(3) 

# 3. Preenchendo os campos
print("Preenchendo formulário...")

# CAMPO NOME (Su bstituao aria-labelledby pelo número que você achar no Inspecionar)
navegador.find_element(By.XPATH, "//input[@aria-labelledby='i1 i4']").send_keys("Seu nome")
time.sleep(1) # Pausa rápida para ficar bonito no vídeo

# CAMPO EMAIL (No Forms, geralmente o input de email é o único type='email')
navegador.find_element(By.XPATH, "//input[@type='email']").send_keys("nomeproprio@outlook.com")
time.sleep(1)

# CAMPO CARTÃO DE CRÉDITO (Visa, Mastercard, Elo)
elemento_visa = navegador.find_element(By.XPATH, "//*[contains(text(), 'Visa')]")
navegador.execute_script("arguments[0].click();", elemento_visa)
time.sleep(1)

# CAMPO NÚMERO DO CARTÃO 
navegador.find_element(By.XPATH, "//input[@aria-labelledby='i25 i28']").send_keys("123456789")
time.sleep(1)

# CAMPO DATA DE NASCIMENTO
navegador.find_element(By.XPATH, "//input[@type='date']").send_keys("01012002")
time.sleep(1)

# 4. Clicar em Enviar
navegador.find_element(By.XPATH, "//span[text()='Enviar']").click()

# Deixa a tela aberta 5 segundos pra recrutadora ver que deu certo/errado, depois fecha
time.sleep(5)
navegador.quit()
print("Teste finalizado!")
