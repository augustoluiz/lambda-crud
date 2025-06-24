from utils.dynamo_utils import DynamoUtils


class PedidoRepository():
    def __init__(self):
        self.dynamo_utils = DynamoUtils()

    def get_pedidos(self):
        return self.dynamo_utils.scan_items()

    def get_pedido_by_id(self, pedido_id):
        return self.dynamo_utils.get_item(pedido_id)

    def create_pedido(self, pedido):
        return self.dynamo_utils.put_item(pedido)

    def update_pedido(self, pedido_id, pedido):
        return self.dynamo_utils.update_item(pedido_id, pedido)

    def delete_pedido(self, pedido_id):
        return self.dynamo_utils.delete_item(pedido_id)
