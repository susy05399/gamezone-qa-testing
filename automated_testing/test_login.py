# automated_testing/test_login.py

import time
import pytest
from selenium.webdriver.common.by import By

def test_login_fallido(browser):
    # 1. Abrir página ficticia (puedes usar un sitio real o maqueta)
    browser.get("https://example.com/login")  # reemplaza con una URL de prueba si tienes

    # 2. Localizar campos y botones
    email = browser.find_element(By.NAME, "email")  # ajusta NAME según la página
    password = browser.find_element(By.NAME, "password")
    login_btn = browser.find_element(By.ID, "login-button")

    # 3. Ingresar datos erróneos
    email.send_keys("susana@mail.com")
    password.send_keys("clave_incorrecta")
    login_btn.click()

    time.sleep(2)  # espera para ver resultado (reemplaza por espera explícita si prefieres)

    # 4. Verificar mensaje de error
    error = browser.find_element(By.ID, "error-message")
    assert "Contraseña incorrecta" in error.text
