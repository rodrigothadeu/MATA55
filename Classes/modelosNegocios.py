from datetime import datetime
from modelosBase import cliente, enderecoEntrega, produto, metodoPagamento

class itemPedido:
    def __init__(self, idItemPedido : int, produto : produto, quantidade : int):
        self.__idItemPedido = idItemPedido
        self.__produto = produto
        self.__quantidade = quantidade
        self.__subtotal = (produto.preco * quantidade)
        
    def __str__(self):
        return f"{self.__quantidade} x {self.__produto} = R$ {self.__subtotal:.2f}"

class pedido:
    def __init__(self, idPedido : int, dataHora : datetime, status : str, cliente : cliente, endereco : enderecoEntrega, itens : list, desconto : float=0.0):
        self.__idPedido = idPedido
        self.__dataHora = dataHora
        self.__status = status
        self.__cliente = cliente
        self.__endereco = endereco
        self.__itens = itens
        self.__desconto = desconto
        
        self.__valorTotal = sum(item.subtotal for item in itens)
        self.__valorFinal = (self.__valorTotal - self.__desconto)
        
    def __str__(self):
        return f"Pedido({self.__idPedido}) - Cliente: {self.__cliente.nome} - Total: R$ {self.__valorFinal:.2f}"
    
class pagamento:
    def __init__(self, idPagamento : int, valorPago : float, dataPagamento : datetime, pedido : pedido, metodoPagamento : metodoPagamento):
        self.__idPagamento = idPagamento
        self.__valorPago = valorPago
        self.__dataPagamento = dataPagamento
        self.__pedido = pedido
        self.__metodoPagamento = metodoPagamento
        
    def __str__(self):
        return f"Pagamento({self.__idPagamento}) - R$ {self.__valorPago:.2f} via {self.__metodoPagamento}"