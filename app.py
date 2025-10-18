from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def lua_script():
    url = "https://cdn.discordapp.com/attachments/1428012794678087950/1429113913525538916/6274860928774003.lua?ex=68f4f58c&is=68f3a40c&hm=9d46c1463da5e69511a99bf404e98d498e8ffb275de3689082fbe710adfff288&"
    response = requests.get(url)
    if response.status_code == 200:
        lua_code = response.text
    else:
        lua_code = "Error: Không thể tải file Lua từ URL"
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
