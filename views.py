from flask import Flask,render_template, request, redirect, url_for, session
import time
import json
import os

class Session:
    def get_session(self):
        return session.get('username')
    def set_session(self,user_name):
        session['username'] = user_name

class Chat:
    def create_message(self,text,author="Анонимус"):
        time_now = time.localtime(time.time())
        messages = self.load_chat()
        messages[self.find_id_last_message()] = (text, author, time.strftime('%H:%M', time_now))
        with open('chat.json', 'w', encoding='utf-8') as file:
            json.dump(messages,file)
    def load_chat(self):
        with open("chat.json", "r", encoding='utf-8') as file:
            file = json.load(file)
        return file
    def find_id_last_message(self):
        messages = self.load_chat()
        if len(messages) > 0:
            return int(list(messages.keys())[-1]) + 1
        return 0

chat = Chat()
app = Flask(__name__)
sessions = Session()

app.secret_key = os.getenv("SECRET", "randomstring123")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form_message = request.form["text-message"]
        form_nickname = request.form["nickname-user"]

        nickname = form_nickname
        if 'username' in session:
            if form_nickname == '':
                nickname = sessions.get_session()
            else:
                sessions.set_session(form_nickname)
        else:
            if nickname == '': nickname = 'Анонимус'
            sessions.set_session(form_nickname)

        chat.create_message(form_message, nickname)
        return redirect(url_for("index"))

    messages = chat.load_chat()
    return render_template("chat.html", messages=messages)

if __name__ == '__main__':
    app.run(debug=True)