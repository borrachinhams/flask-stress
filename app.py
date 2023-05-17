from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/stress')
def stress(time=10):
    time_param = request.args.get('time', default=10, type=int)
    os.system(f'/usr/bin/stress-ng --cpu 4 --fork 2 --timeout {time_param}s')

    xpto = f'Processo finalizado --> tempo executado: {time_param}'
    return xpto


if __name__ == '__main__':
    app.run()
