# Flask setup with imports, routes, and all website pages:

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/macros')
def macros():
    return render_template('macros.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

# GET and POST using log page:

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        meal = request.form['meal']
        calories = request.form['calories']
         # Print and show meal user just logged:
        message = f"Meal logged: {meal} ({calories} calories)"
        print(message)  # Still shows in the terminal too
        return render_template('log.html', message=message)
    return render_template('log.html')


# When I run python app.py, go ahead and start the website server so I can see my pages:
if __name__ == '__main__':
    app.run(debug=True)
