from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def home():
    return '''
        <form method="POST" action="/ask">
            <input type="text" name="question" placeholder="Ask me anything..." size="50">
            <button type="submit">Ask</button>
        </form>
    '''

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )
    answer = response.choices[0].message.content
    return f"<p><b>Q:</b> {question}</p><p><b>A:</b> {answer}</p><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)