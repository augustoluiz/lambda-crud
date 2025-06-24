from decimal import Decimal


class Pedido:
    def __init__(self, pedido_id, data_hora, cliente, itens, preco_total):
        self.pedido_id = pedido_id
        self.data_hora = data_hora
        self.cliente = cliente
        self.itens = itens
        self.preco_total = Decimal(preco_total)

    def to_dict(self):
        return {
            "pedido_id": self.pedido_id,
            "data_hora": self.data_hora,
            "cliente": self.cliente,
            "itens": self.itens,
            "preco_total": self.preco_total
        }