class cliente:
    def __init__(self, idCliente : int, nome : str, telefone : str):
        self.__idCliente = idCliente
        self.__nome = nome
        self.__telefone = telefone
    
    def __str__(self):
        return f"Cliente({self.__idCliente}, {self.__nome}, {self.__telefone})"

class enderecoEntrega:
    def __init__(self, idEndereco : int, rua : str, numero : str, bairro : str, cidade : str, complemento : str=""):
        self.__idEndereco = idEndereco
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__complemento = complemento

    def __str__(self):
        return f"Endereço: ({self.__rua}, {self.__numero} - {self.__bairro}, {self.__cidade} ({self.__complemento}))"

class produto:
    def __init__(self, idProduto : int, nomeProduto : str, descricao : str="", preco : float=0.0):
        self.__idProduto = idProduto
        self.__nomeProduto = nomeProduto
        self.__descricao = descricao
        self.__preco = preco

    def __str__(self):
        return f"({self.__idProduto}, {self.__nomeProduto}, R$ {self.__preco:.2f})"
    
class metodoPagamento:
    def __init__(self, idMetodoPagamento : int, tipo : str):
        self.__idMetodoPagamento = idMetodoPagamento
        self.__tipo = tipo

    def __str__(self):
        return f"Método: {self.__tipo}"