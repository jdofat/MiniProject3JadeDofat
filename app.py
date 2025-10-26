# Flask setup- imports, routes, and all website pages:

from flask import Flask, render_template, request
from models import get_db_connection

app = Flask(__name__)

# for homepage-
@app.route('/')
def home():
    return render_template('index.html')

# about page-
@app.route('/macros')
def macros():
    return render_template('macros.html')

# sign in-
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        message = "Account Created!"
        return render_template('register.html', message=message)
    return render_template('register.html')

# log in-
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cur.fetchone()
        conn.close()
        if user:
            message = "You are Logged In"
        else:
            message = "Oh No, Invalid!"
        return render_template('login.html', message=message)
    return render_template('login.html')



# GET and POST using log page so users can log food and see log history

# LOG: lets user enter a meal & cals-

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        meal = request.form['meal']
        calories = request.form['calories']
        
         # Print in term and show on screen the meal user just logged:
        message = f"Meal logged: {meal} ({calories} calories)"
        print(message)
        return render_template('log.html', message=message)
    return render_template('log.html')

# LOGS: shows list of all meals saved in the database-

@app.route('/logs')
def logs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT meal, calories FROM meals WHERE user_id = 1')
    meals = cur.fetchall()
    conn.close()
    return render_template('logs.html', meals=meals)



# When I run python app.py, go ahead and start the website server so I can see my pages:
if __name__ == '__main__':
    app.run(debug=True)
