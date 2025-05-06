from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'this_is_a_secret_key'  # 用來加密 session

# 首頁
@app.route('/')
def index():
    return render_template('index.html')

# 商品頁
@app.route('/shop')
def shop():
    return render_template('shop.html')

# 最新消息
@app.route('/news')
def news():
    return render_template('news.html')

# FAQ
@app.route('/faq')
def faq():
    return render_template('faq.html')

# cookies聲明
@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

# 會員登入頁
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 這裡你可以接上資料庫驗證
        if username == 'admin' and password == '1234':  # 測試用帳密
            session['user'] = username
            return redirect(url_for('member'))
        else:
            return "登入失敗"
    return render_template('login.html')

# 會員中心頁
@app.route('/member')
def member():
    if 'user' in session:
        return render_template('member.html', user=session['user'])
    else:
        return redirect(url_for('login'))

# 登出
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
