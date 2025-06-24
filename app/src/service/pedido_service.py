from datetime import datetime
from uuid import uuid4
from data.pedido import Pedido
from repository.pedido_repository import PedidoRepository


class PedidoService:
    def __init__(self):
        self.repository = PedidoRepository()

    def get_pedidos(self):
        return self.repository.get_pedidos()

    def get_pedido_by_id(self, pedido_id):
        return self.repository.get_pedido_by_id(pedido_id)

    def create_pedido(self, pedido):
        if not isinstance(pedido, Pedido):
            pedido['pedido_id'] = uuid4().__str__()
            pedido['data_hora'] = datetime.now().isoformat()
            pedido = Pedido(**pedido)

        return self.repository.create_pedido(pedido)

    def update_pedido(self, pedido_id, pedido):
        return self.repository.update_pedido(pedido_id, pedido)

    def delete_pedido(self, pedido_id):
        return self.repository.delete_pedido(pedido_id)