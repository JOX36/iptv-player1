from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests as req

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy/api')
def proxy_api():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No URL'}), 400
    try:
        r = req.get(url, timeout=15)
        resp = app.response_class(
            response=r.content,
            status=r.status_code,
            mimetype=r.headers.get('Content-Type','application/json')
        )
        return resp
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
