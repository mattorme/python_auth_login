from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Matt Orme',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Now'
    },

    {
        'author': 'Jane Dpe',
        'title': 'Blog Post 523',
        'content': 'hello post content',
        'date_posted': 'also now'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
    