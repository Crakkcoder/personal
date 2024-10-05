from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts
posts = [
    {"title": "First Post", "content": "This is my first blog post!"},
    {"title": "Second Post", "content": "Here's some more content."},
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
