from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# دیکشنری برای ذخیره نام کاربری و رمز عبور
users_db = {
    "correct_username": "correct_password"
}

# صفحه اصلی
@app.route('/')
def home():
    return render_template('home.html')

# صفحه ثبت‌نام
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # ذخیره اطلاعات کاربر در دیکشنری
        users_db[username] = password
        flash("Registration Successful! Please log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

# صفحه ورود
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # بررسی نام کاربری و رمز عبور از دیکشنری
        if users_db.get(username) == password:
            session['user'] = username
            return redirect(url_for('map'))
        else:
            flash("Invalid credentials", "error")
    return render_template('login.html')

# صفحه نقشه
@app.route('/map')
def map():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)