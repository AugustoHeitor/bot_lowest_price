# importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time


# Configurações
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


class LowestPrice:
    def __init__(self, name):
        self.name = name.lower()
        self.result = []
        self.driver = webdriver.Chrome(options=chrome_options)

    # O método "web_config" é responsavel por contem configurações do bot!
    def web_config(self):
        self.driver.maximize_window()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        self.driver.execute_cdp_cmd(
            "Network.setUserAgentOverride", {"userAgent": user_agent}
        )

    # O método "kabum" contem a automação do site kabum!
    def kabum(self):
        try:
            # Iniciando a pesquisa no site Kabum!
            print("Iniciando pesquisa por produto no site Kabum!")

            # Abrindo o site Kabum!
            self.driver.get("https://www.kabum.com.br/")

            time.sleep(3)

            # Capturando a notificação!
            allow_notifications = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Entendi')]")
                )
            )

            # Clicando na notificação!
            allow_notifications.click()

            # Capturando a barrra de pesquisa!
            search_field = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="input-busca"]'))
            )

            # Digitando na barra de pesquisa e apertando enter!
            search_field.send_keys(self.name + Keys.ENTER)

            # Capturando a main!
            main = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, "//main"))
            )

            # Verificando se main foi carregada!
            if main:
                time.sleep(2)

                # Capturando o parágrafo de não encontrado!

                not_found = self.driver.find_elements(
                    By.XPATH, '//div[@id="listingEmpty"]'
                )

                # Verificando se o parágrafo de não encontrado existe!
                if not not_found:
                    # Capturando o filtro!
                    select = Select(
                        self.driver.find_element(
                            By.XPATH, '//*[@id="Filter"]/div[1]/select'
                        )
                    )

                    # Selecionando o preço crescente do filtro!
                    select.select_by_visible_text("Preço crescente")

                    time.sleep(2)

                    # Capturando os produtos!
                    products = self.driver.find_elements(
                        By.XPATH, '//div[contains(@class, "productCard")]'
                    )

                    # Percorrendo a lista dos produtos!
                    for product in products:
                        time.sleep(0.5)

                        # Scrollando para o produto!
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView();", product
                        )

                        # Capturando o título do produto!
                        productTitle = product.find_element(By.XPATH, ".//h2")

                        # Armazenando o texto do título e convertendo o para minúsculo!
                        text = productTitle.text.lower()

                        # Verificando se o texto contem parcialmente o que foi pedido na pesquisa!
                        if re.search(re.escape(self.name), text):
                            # Clicando no produto encontrado!
                            product.click()

                            time.sleep(2)

                            img = WebDriverWait(self.driver, 60).until(
                                EC.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        '//*[@id="carouselDetails"]/div[2]/div[1]/figure/img',
                                    )
                                )
                            )

                            # Verificando se imagem foi carregada!
                            if img:
                                # Capturando o link do produto!
                                link = self.driver.current_url

                                # Criando um objeto e adicionando a lista!
                                self.result.append({"web": "Kabum", "link": link})

                                # Scrollando para baixo!
                                self.driver.execute_script("window.scrollBy(0, 200)")

                                # Printando a tela!
                                self.driver.save_screenshot("kabum_screenshot.png")

                                # Retornando uma msg e finalizando a pesquisa!
                                return print(
                                    "Pesquisa por produto no site Kabum Finalizada!"
                                )
                    # Lançando um erro!
                    raise ValueError("Produto não encontrado no site Kabum!")

            else:
                # Lançando um erro!
                raise ValueError("Produto não encontrado no site Kabum!")

        except Exception as Error:
            # Lançando um erro!
            error = {"error": "Ops! Ocorreu um erro inesperado.", "msg": Error}

            # Printando a mensagem de erro!
            print(error)

    # O método "amazon" contem a automação do site amazon!
    def amazon(self):
        try:
            # Iniciando a pesquisa no site Amazon!
            print("Iniciando pesquisa por produto no site Amazon!")

            # Abrindo o site da Amazon!
            self.driver.get("https://www.amazon.com.br/")

            time.sleep(3)

            # Capturando a barra de pesquisa!
            search_field = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="twotabsearchtextbox"]')
                )
            )

            # Digitando na barra de pesquisa e apertando enter!
            search_field.send_keys(self.name + Keys.ENTER)

            # Capturando a main!
            main = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="search"]'))
            )

            # Verificando se main foi carregada!
            if main:
                time.sleep(2)

                # Capturando o parágrafo de não encontrado!
                not_found = self.driver.find_elements(
                    By.XPATH, '//span[contains(text(),"Nenhum resultado para")]'
                )

                # Verificando se o parágrafo de não encontrado existe!
                if not not_found:
                    # Capturando o filtro
                    select = Select(
                        self.driver.find_element(
                            By.XPATH, '//*[@id="s-result-sort-select"]'
                        )
                    )

                    # Selecionando o Preço do menor para o maior do filtro!
                    select.select_by_visible_text("Preço: Do menor para o maior")

                    time.sleep(2)

                    # Capturando a div que contem os produtos!
                    productList = WebDriverWait(self.driver, 60).until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                '//*[@id="search"]/div[1]/div[1]/div',
                            )
                        )
                    )

                    # Verificando se a div foi carregada!
                    if productList:
                        # Capturando os produtos!
                        products = self.driver.find_elements(
                            By.XPATH,
                            "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']",
                        )

                        # Percorrendo a lista dos produtos!
                        for product in products:
                            time.sleep(0.5)

                            # Scrollando para o produto!
                            self.driver.execute_script(
                                "arguments[0].scrollIntoView();", product
                            )

                            # Armazenando o texto do título e convertendo o para minúsculo!
                            text = product.text.lower()

                            # Verificando se o texto contem parcialmente o que foi pedido na pesquisa!
                            if re.search(re.escape(self.name), text):
                                # Capturando o link do produto!
                                product = product.find_element(By.XPATH, ".//a")

                                # Clicando no link do produto!
                                product.click()

                                time.sleep(2)

                                # Scrolando para cima!
                                self.driver.execute_script("window.scrollTo(0, 0);")

                                # Capturando o link do produto!
                                link = self.driver.current_url

                                # Criando um objeto e adicionando na lista!
                                self.result.append({"web": "Amazon", "link": link})

                                # Scrollando para baixo!
                                self.driver.execute_script("window.scrollBy(0, 0)")

                                # Printando a tela!
                                self.driver.save_screenshot("amazon_screenshot.png")

                                # Finalizando a pesquisa e retornando uma msg!
                                return print(
                                    "Pesquisa por produto no site Amazon Finalizada!"
                                )

                        else:
                            # Lançando um erro!
                            raise ValueError("Produto não encontrado no site Amazon!")

            else:
                # Lançando um erro!
                raise ValueError("Produto não encontrado no site Amazon!")
        except Exception as Error:
            # Lançando um erro!
            error = {"error": "Ops! Ocorreu um erro inesperado.", "msg": Error}

            # Printando a mensagem de erro!
            print(error)

    # O método "pichau" contem a automação do site pichau!
    def pichau(self):
        try:
            # Iniciando a pesquisa na Pichau!
            print("Iniciando pesquisa por produto no site Pichau!")

            # Abrindo o site da Pichau!
            self.driver.get("https://www.pichau.com.br/")

            time.sleep(3)

            # Capturando a notificação!
            allow_notifications = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Prosseguir')]")
                )
            )

            # Clicando na notificação!
            allow_notifications.click()

            # Capturando a barrra de pesquisa!
            search_field = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//input[@placeholder="Digite o que você procura..."]')
                )
            )

            # Digitando na barra de pesquisa e apertando enter!
            search_field.send_keys(self.name + Keys.ENTER)

            # Capturando o main!
            main = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main'))
            )

            # Verificando se o main foi carregado!
            if main:
                time.sleep(2)

                # Capturando o parágrafo de não encontrado!
                not_found = self.driver.find_elements(
                    By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div[2]/div/p'
                )

                # Verificando se o parágrafo de não encontrado existe!
                if not not_found:
                    # Capturando o botão de filtro!
                    filter_button = WebDriverWait(self.driver, 60).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//div[contains(text(),"Relevância")]')
                        )
                    )

                    # Clicando no botão de filtro
                    filter_button.click()

                    # Capturando a opção do menor valor no filtro!
                    button_lower_value = WebDriverWait(self.driver, 60).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//li[contains(text(),"Menor valor")]')
                        )
                    )

                    # Clicando na opção!
                    button_lower_value.click()

                    time.sleep(4)

                    # Capturando os produtos da lista!
                    products = self.driver.find_elements(
                        By.XPATH, '//a[@data-cy="list-product"]'
                    )

                    # Percorrendo a lista de produtos!
                    for product in products:
                        time.sleep(0.5)

                        # Scrollando para o produto!
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView();", product
                        )

                        # Capturando o título do produto!
                        productTitle = product.find_element(By.XPATH, ".//h2")

                        # Armazenando o texto do título e convertendo o para minúsculo!
                        text = productTitle.text.lower()

                        # Verificando se o texto contem parcialmente o que foi pedido na pesquisa!
                        if re.search(re.escape(self.name), text):
                            # Clicando no produto!
                            product.click()

                            time.sleep(2)

                            # Capturando a imagem do produto!
                            img = WebDriverWait(self.driver, 60).until(
                                EC.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        '//*[@id="__next"]/main/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/figure/div/img',
                                    )
                                )
                            )

                            # Verificando se imagem foi carregada!
                            if img:
                                # Scrollando para cima!
                                self.driver.execute_script("window.scrollTo(0, 0);")

                                # Capturando o link do produto!
                                link = self.driver.current_url

                                # Adicionando as informações em uma lista!
                                self.result.append(
                                    {
                                        "web": "Pichau",
                                        "link": link,
                                    }
                                )

                                # Scrollando para baixo!
                                self.driver.execute_script("window.scrollBy(0, 100)")

                                # Printando a tela!
                                self.driver.save_screenshot("pichau_screenshot.png")

                                # Finalizando a pesquisa e printando uma msg!
                                return print(
                                    "Pesquisa por produto no site Pichau Finalizada!"
                                )

                    # Lançando um erro
                    raise ValueError("Produto não encontrado no site Pichau!")

                else:
                    # Lançando um erro
                    raise ValueError("Produto não encontrado no site Pichau!")
        except Exception as Error:
            # Lançando um erro!
            error = {"error": "Ops! Ocorreu um erro inesperado.", "msg": Error}

            # Printando a mensagem de erro!
            print(error)

    # O método "show_result" imprimi o resultado da pesquisa em um pdf!
    def show_result(self):
        print(self.result)

    # O método "call" chama todos os outros métodos!
    def call(self):
        self.web_config()
        self.kabum()
        self.amazon()
        self.pichau()
        self.show_result()
        self.driver.quit()


# Criando uma instancia da classe e passando o valor da pesquisa!
application = LowestPrice("Kingston")

# Chamando o método "call"!
application.call()
