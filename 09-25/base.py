from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager as CM
from time import sleep


class ImportadorBase():

    def login(self):
        try:
            self.log("login logado? {}".format(self.logado))
            if self.logado:
                return self
            self.driver.get("https://login.plataformaneo.com.br/")
            # nome da loja
            self.driver.find_element_by_id(
                "nomeloja").send_keys(self.nome_loja)
            # usuario
            self.driver.find_element_by_id("usuario").send_keys(self.usuario)
            # senha
            self.driver.find_element_by_id("senha").send_keys(self.senha)
            # botao login
            self.driver.find_element_by_id("msgLoginResult").click()
            sleep(1)
            try:
                mensagem = self.driver.find_element_by_xpath(
                    "//div[@class='alertBox active']").find_element_by_xpath("p").text
            except:
                mensagem = ""
            if mensagem != "":
                raise Exception(mensagem)
            self.logado = True
            self.log("login feito")
            return self
        except Exception as ex:
            raise Exception("erro no login: " + repr(ex))

    def cabecalho(self):
        return ""

    def log(self, mensagem):
        print(mensagem)

    def get_parametros(self):
        return {
            'nome_loja': 'petcenterexpress',
            'nome_usuario': 'petcenterexpress',
            'senha': '#Petcenterexpress2020'
        }

    def set_parametros(self):
        self.log("setando parâmetros")
        parametros = self.get_parametros()
        self.nome_loja = parametros["nome_loja"]
        self.usuario = parametros["nome_usuario"]
        self.senha = parametros["senha"]
        self.logado = False

    def abrir_chrome(self):
        try:
            self.log("abrindo chrome")
            options = Options()
            # options.add_argument("headless")
            options.add_argument('disable-gpu')
            options.add_argument('log-level=3')
            options.add_argument('no-sandbox')
            options.add_argument('disable-dev-shm-usage')
            self.driver = webdriver.Chrome(
                executable_path=CM().install(),
                options=options
            )
        except Exception as ex:
            raise Exception("erro na criação do Chrome: " + repr(ex))

    def processar(self, retomar):
        pass

    def _processar(self, retomar):
        try:
            self.log("processar")
            self.processar(retomar)
            self.log("processar feito")
        except Exception as ex:
            raise Exception("erro no processar: " + repr(ex))

    def handle_exception(self, ex):
        self.log("erro ocorreu {}".format(repr(ex)))

    def retomar(self, execucao_id):
        self.log("retomar execucao_id {}".format(execucao_id))
        self.set_parametros()
        try:
            self.abrir_chrome()
            self.login()
            self._processar(True)
        except Exception as ex:
            self.handle_exception(ex)
        finally:
            self.execucao_finalizada()

    def execucao_finalizada(self):
        self.log("salvando execucao")
        self.log("execucao salva")

    def importar(self):
        self.log("importar")
        try:
            self.set_parametros()
            self.abrir_chrome()
            self.login()
            self._processar(False)
        except Exception as ex:
            self.handle_exception(ex)
        finally:
            self.execucao_finalizada()
