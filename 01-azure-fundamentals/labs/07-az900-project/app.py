import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # Read an environment variable called APP_MESSAGE (set in Azure App Service)
    message = os.environ.get("APP_MESSAGE", "Hello from Azure Web App (default)")
    return f"""
    <html>
      <head>
        <title>Azure Fundamentals Python App</title>
      </head>
      <body style="font-family:Segoe UI, Arial; text-align:center; margin-top:50px;">
        <h1>{message}</h1>
        <p>This is a simple Python Flask app running on Azure App Service.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
