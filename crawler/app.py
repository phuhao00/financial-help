from flask import Flask, request, jsonify
from crawl4ai import WebCrawler

app = Flask(__name__)
crawler = WebCrawler()

@app.route('/crawl')
def crawl():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400

    try:
        result = crawler.run(url)
        return jsonify({'content': result.to_text()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
