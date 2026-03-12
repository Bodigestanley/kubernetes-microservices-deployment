from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Order Service</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: #fff;
            width: 400px;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }
        .card h1 { color: #11998e; font-size: 40px; margin-bottom: 15px; }
        .card p { font-size: 20px; color: #333; margin-bottom: 20px; }
        .card button {
            background-color: #11998e;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px 25px;
            font-size: 16px;
            cursor: pointer;
        }
        .card button:hover { background-color: #38ef7d; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Order Service</h1>
        <p>Handles Customer Orders</p>
        <button>Create Order</button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)