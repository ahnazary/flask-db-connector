from flask import Flask, request, jsonify
from postgres_interface import PostgresInterface
from sqlalchemy import text

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def handle_message():
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    print(f"Received query: {query}")
    pg_interface = PostgresInterface()
    response = str(pg_interface.execute(text(query)))
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
