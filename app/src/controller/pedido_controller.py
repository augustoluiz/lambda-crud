from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from service.pedido_service import PedidoService

app = APIGatewayRestResolver()
pedido_service = PedidoService()

@app.get("/pedidos")
def get_pedidos():
    pedidos = pedido_service.get_pedidos()
    return {
        "statusCode": 200,
        "message": "Pedidos retornados com sucesso",
        "data": pedidos
    }

@app.get("/pedidos/<id>")
def get_pedido_by_id(id):
    pedido = pedido_service.get_pedido_by_id(id)
    return {
        "statusCode": 200,
        "message": "Pedido retornado com sucesso",
        "data": pedido
    }

@app.post("/pedidos")
def create_pedido():
    pedido = app.current_event.json_body
    pedido_criado = pedido_service.create_pedido(pedido)
    return {
        "statusCode": 201,
        "message": "Pedido criado com suesso",
        "data": pedido_criado
    }


@app.patch("/pedidos/<id>")
def update_pedido(id):
    pedido = app.current_event.json_body
    pedido_atualizado = pedido_service.update_pedido(id, pedido)
    return {
        "statusCode": 200,
        "message": "Pedido atualizado com sucesso",
        "data": pedido_atualizado
    }

@app.delete("/pedidos/<id>")
def delete_pedido(id):
    resultado = pedido_service.delete_pedido(id)
    return {
        "statusCode": 200,
        "message": resultado['message']
    }
