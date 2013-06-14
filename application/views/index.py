
from application import app
from flask import request
from application.apps import dianzan

@app.route('/')
def index():
    return '''
    <html>
        <form action="/dianzan" method="post">
            <input type="text" value="qq" name="qq"/>
            <input type="password" name="pwd" />
            <input type="submit" value="confirem">
        </form>
    </html>
    '''

@app.route('/dianzan', methods = ['POST'])
def _dianzan():
    if request.method != 'POST':
        return 'methods not allowed!'
    qq = request.form.get('qq')
    pwd = request.form.get('pwd')
    D = dianzan.Dianzan(qq = qq, pwd = pwd)
    return D.dianzan()

@app.route('/dianzan_verify', methods = ['POST'])
def _dianzan_verify():
    if request.method != 'POST':
        return 'methods not allowed!'
    headers = dict()
    headers['Origin'] = 'http://pt.3g.qq.com'
    headers['Host'] = 'pt.3g.qq.com'
    #headers['User-Agent'] = 'curl/7.21.3 (i686-pc-linux-gnu) libcurl/7.21.3 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.18'
    headers['User-Agent'] = ''

    D = dianzan.Dianzan_verify()
    D.verify(data = request.form, headers = headers)
    return D.dianzan()
