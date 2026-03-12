from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Frontend Service</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        h1 { color: #8E44AD; }
        p { font-size: 18px; }
        .service-box { display: inline-block; margin: 20px; padding: 20px; border: 1px solid #ccc; border-radius: 10px; }
    </style>
</head>
<body>
    <h1>Frontend Service</h1>
    <p>This microservice provides the UI for other services.</p>
    <div class="service-box">Auth Service</div>
    <div class="service-box">Product Service</div>
    <div class="service-box">Order Service</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)