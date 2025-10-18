from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def lua_script():
    url = "https://cdn.discordapp.com/attachments/1428012794678087950/1429119472144482484/8160032594895926.lua?ex=68f4fab9&is=68f3a939&hm=6ee0b769c80deebd168ad314e805223ce998a26af0699d257a26d10b9433ea94&"
    response = requests.get(url)
    if response.status_code == 200:
        lua_code = response.text
    else:
        lua_code = "Error: Không thể tải file Lua từ URL"
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
