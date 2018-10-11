from sanic import Sanic
from sanic.response import json

from models.item import Item
from settings import HOST, PORT

app = Sanic()

@app.route('/')
async def index(request):
    return json({})

@app.route('/learn', methods=['POST'])
async def learn(request):
    item = Item.from_dict(request.json)
    return json({})

@app.route('/predict',  methods=['POST'])
async def predict(request):
    return json({})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
