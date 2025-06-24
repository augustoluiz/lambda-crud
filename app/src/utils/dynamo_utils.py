import boto3
from botocore.exceptions import ClientError

class DynamoUtils:
    def __init__(self):
        self.table_name = "Pedidos"
        self.dynamo_client = boto3.resource("dynamodb")
        self.table = self.dynamo_client.Table(self.table_name)

    def get_item(self, pedido_id):
        try:
            response = self.table.get_item(Key={"pedido_id": pedido_id})
            return response.get("Item", {})
        except ClientError as e:
            return {"error": str(e)}

    def put_item(self, pedido):
        try:
            self.table.put_item(Item=pedido.to_dict())
            return {"message": "Pedido criado com sucesso"}
        except ClientError as e:
            return {"error": str(e)}

    def update_item(self, pedido_id, pedido):
        try:
            update_expression = "SET " + ", ".join(f"{k}=:{k}" for k in pedido.keys())
            expression_values = {f":{k}": v for k, v in pedido.items()}
            self.table.update_item(
                Key={"pedido_id": pedido_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_values,
            )
            return {"message": "Pedido atualizado com sucesso"}
        except ClientError as e:
            return {"error": str(e)}

    def delete_item(self, pedido_id):
        try:
            self.table.delete_item(Key={"pedido_id": pedido_id})
            return {"message": "Pedido deletado com sucesso"}
        except ClientError as e:
            return {"error": str(e)}