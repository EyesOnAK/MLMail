# server.py

from flask import Flask, request, jsonify
from rag_llm_search import search_email

app = Flask(__name__)

@app.route('/search-email', methods=['POST'])
def handle_search():
    data = request.get_json()
    query = data.get('query')
    results = search_email(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)