from sanic import Sanic
from sanic.response import json

from models.item import Item
from settings import HOST, PORT
from learn import predict_item, learn_item

app = Sanic()


@app.route('/')
async def index(request):
    return json({})


@app.route('/learn', methods=['POST'])
async def learn(request):
    item = Item.from_dict(request.json)
    learn_item(item)
    return json({})


@app.route('/predict', methods=['POST'])
async def predict(request):
    item = Item.from_dict(request.json)
    y = predict_item(item)
    return json({'y': y})


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
