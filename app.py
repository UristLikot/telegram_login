import hashlib
import hmac

from flask import Flask, render_template, request

app = Flask(__name__)
bot_api="459744558:AAEWYIqK8c-VTomDzIm_4Vre0f-bCJL0JXs"


@app.route('/')
def index():
    return render_template('index.html')
def string_generator(data_incoming):
    data = data_incoming.copy()
    del data['hash']
    keys = sorted(data.keys())
    print(keys)
    string_arr = []
    for key in keys:
        if data[key] is not None:
            string_arr.append(key + '=' + data[key])
    string_cat = '\n'.join(string_arr)
    return string_cat
@app.route('/login')
def login():
    tg_data = {
        "id": request.args.get('id',None),
        "first_name": request.args.get('first_name',None),
        "last_name": request.args.get('last_name',None),
        "username": request.args.get('username',None),
        "photo_url": request.args.get('photo_url',None),
        "auth_date": request.args.get('auth_date',None),
        "hash": request.args.get('hash')
    }
    data_check_string = string_generator(tg_data)
    data_check_string_bytes = bytes(data_check_string, 'utf-8')
    secret_key = hashlib.sha256(bot_api.encode('utf-8')).digest()
    secret_key_bytes = secret_key
    hmac_string = hmac.new(secret_key_bytes, data_check_string_bytes, hashlib.sha256).hexdigest()
    if hmac_string==tg_data['hash']:
        return render_template('testlogin.html')
    else:
        return render_template('fail.html')
if __name__ == '__main__':
    app.run(host="192.168.1.100",port=8001, debug=True)
