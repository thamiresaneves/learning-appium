import unittest
from appium import webdriver
import time

class AppiumCourse(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'Appium',
            'app': '/Users/thamiresneves/Downloads/AppiumTest.apk'
        }

        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        time.sleep(10)

    def tearDown(self):
        self.instance.quit()

    def test_01_open_about(self):
        time.sleep(5)
        btn_sobre = self.instance.find_element_by_id('com.example.cursoappium:id/button_sobre')
        btn_sobre.click()

        time.sleep(4)
        btn_ok = self.instance.find_element_by_id('com.example.cursoappium:id/button_ok')
        check = btn_ok.is_displayed()
        assert check, 'Botão OK não localizado'

    def test_02_cadastrar_com_nome_vazio(self):
        time.sleep(5)
        btn_abrir_cadastro = self.instance.find_element_by_id('com.example.cursoappium:id/button_cadastrar')
        btn_abrir_cadastro.click()

        time.sleep(2)
        email_field = self.instance.find_element_by_id("com.example.cursoappium:id/TextInputEmail")
        email_field.send_keys("test@gmail.com")
        btn_cadastrar = self.instance.find_element_by_id('com.example.cursoappium:id/BotaoCadastrar')
        btn_cadastrar.click()

        time.sleep(1)
        errorMessage = self.instance.find_element_by_id('com.example.cursoappium:id/textinput_error')
        check = errorMessage.is_displayed()
        assert check, 'Mensagem de erro não exibida'


    def test_03_cadastrar_com_email_vazio(self):
        time.sleep(5)
        btn_abrir_cadastro = self.instance.find_element_by_id('com.example.cursoappium:id/button_cadastrar')
        btn_abrir_cadastro.click()

        time.sleep(2)
        name_field = self.instance.find_element_by_id("com.example.cursoappium:id/TextInputNome")
        name_field.send_keys("Rafaelly")
        btn_cadastrar = self.instance.find_element_by_id('com.example.cursoappium:id/BotaoCadastrar')
        btn_cadastrar.click()

        time.sleep(1)
        errorMessage = self.instance.find_element_by_id('com.example.cursoappium:id/textinput_error')
        check = errorMessage.is_displayed()
        assert check, 'Mensagem de erro não exibida'

    def test_04_cadastrar_com_email_invalido(self):
        pass
