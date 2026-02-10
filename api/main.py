from flask import Flask, request, jsonify
from core.agent.ng9e_agent import NG9EAgent

app = Flask(__name__)
agent = NG9EAgent()

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    result = agent.run(user_input)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
