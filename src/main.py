from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def index(request):
    return json({})

@app.route('/learn', methods=['POST'])
async def learn(request):
    return json({})

@app.route('/predict',  methods=['POST'])
async def predict(request):
    return json({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
