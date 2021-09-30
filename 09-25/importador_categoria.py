from time import sleep, timezone
from base import ImportadorBase

class JetNeoImportadorCategoria(ImportadorBase):

    CATEGORIA_URL = "https://painel1.plataformaneo.com.br/categoria/listar.asp"

    def cabecalho(self):
        return "id_pai;id;nome;ativo\n"

    def processar_categoria(self, categoria_element, id_pai=0):
        # id
        id = categoria_element.find_element_by_id(
            "hdnIdCategoria").get_property("value")
        try:
            # nome
            nome = categoria_element.find_element_by_name(
                "Nome").get_property("value")
            # status (Ativo Inativo)
            status = categoria_element.find_element_by_name(
                "status").get_attribute("data-status") == "A"
            self.categorias.append(
                [
                    nome,
                    status,
                    id,
                    id_pai
                ]
            )
            resultado = "{};{};\"{}\";{}\n".format(
                id_pai,
                id,
                nome,
                status
            )
        except Exception as ex:
            resultado = repr(ex)
        try:
            # categorias filhas
            listaCategoriasFilhas_element = categoria_element.find_element_by_xpath(
                "ul")
            categorias_filhas_elements = listaCategoriasFilhas_element.find_elements_by_xpath(
                "li")
            for categoria_filha_element in categorias_filhas_elements:
                self.processar_categoria(categoria_filha_element, id)
        except:
            pass

    def processar(self, retomar):
        self.driver.get(JetNeoImportadorCategoria.CATEGORIA_URL)
        sleep(1)
        self.categorias = []
        # categorias
        listaCategorias_element = self.driver.find_element_by_id(
            "listaCategorias")
        categorias_elements = listaCategorias_element.find_elements_by_xpath(
            "li")
        for categoria_element in categorias_elements:
            self.processar_categoria(categoria_element)
        print(self.categorias)

if __name__ == '__main__':
    JetNeoImportadorCategoria().importar()