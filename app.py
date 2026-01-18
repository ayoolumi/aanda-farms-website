"""
A AND A FARMS AND FOODS LIMITED
Coming Soon Landing Page
Flask Application
"""

from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')


@app.route('/')
def index():
    """Landing page - Coming Soon"""
    return render_template('index.html')


@app.route('/health')
def health():
    """Health check endpoint for deployment"""
    return {'status': 'healthy'}, 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
