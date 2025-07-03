from flask import Flask, render_template_string, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to ECS App</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
            .container { max-width: 400px; margin: 80px auto; background: #fff; padding: 30px 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            h1 { color: #2d6cdf; }
            input[type=text] { width: 100%; padding: 8px; margin: 10px 0 20px 0; border: 1px solid #ccc; border-radius: 4px; }
            button { background: #2d6cdf; color: #fff; border: none; padding: 10px 18px; border-radius: 4px; cursor: pointer; }
            button:hover { background: #1a4e8a; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to ECS App!</h1>
            <form method="post">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name" placeholder="Your name..." required>
                <button type="submit">Greet Me</button>
            </form>
            {% if name %}
                <h2>Hello, {{ name }}!</h2>
            {% endif %}
        </div>
    </body>
    </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
