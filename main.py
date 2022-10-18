from flask import Flask, request, url_for
import os
from datetime import datetime

app = Flask(__name__)


@app.get("/")
def index():
    # query http://127.0.0.1:5000?name=100
    name = request.args.get('name')
    return f"<p>Hello, World! {name}</p>"


# param http://127.0.0.1:5000/user/123
@app.get("/user/<name>")
def user(name):
    return f"User {name}"


@app.post('/upload')
def upload():
    try:
        f = request.files.get('file')
        if f.filename == '':
            return {
                'code': -1,
                'msg': 'please choice file upload!'
            }
            pass
        timedate = datetime.now().strftime('%Y%m%d_%H%M_%s')
        [filename, suffix] = os.path.splitext(f.filename)
        filename_fmt = f'{filename}_{timedate}{suffix}'
        filepath = os.path.join(os.path.abspath('.'), 'static/upload', filename_fmt)
        f.save(filepath)
        app.logger.info('file upload successful')
        return {
            'code': 0,
            'msg': 'ok'
        }
    except BaseException as e:
        app.logger.error('file upload fail')
        return {
            'code': -1,
            'error': e,
            'msg': 'fail',
        }
