from flask import Flask, render_template, jsonify, request
import processor
import webbrowser
import threading
import time

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = processor.chatbot_response(the_question)
        return jsonify({"response": response})
    else:
        return jsonify({"response": ""})

def open_browser():
    """Function to open browser after server starts"""
    time.sleep(1)  # Wait for server to start
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    # Start browser in a separate thread to avoid blocking Flask
    threading.Thread(target=open_browser).start()
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)