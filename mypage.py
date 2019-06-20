from flask import Flask, render_template

app = Flask('__name__',
            static_folder='static',
            template_folder='templates')


@app.route('/')
def home():
    message = "Hello, World"
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
