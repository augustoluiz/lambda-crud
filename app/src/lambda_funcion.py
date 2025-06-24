from controller.pedido_controller import app

def lambda_handler(event, context):
    app.resolve(event, context)


if __name__ == '__main__':
    # leia event.json e armazene em um objeto
    import json
    with open('event.json', 'r') as file:
        event = json.load(file)
    response = lambda_handler(event, '')
    print(response)