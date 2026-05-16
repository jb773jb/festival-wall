from flask import Flask, request

app = Flask(__name__)

messages = []

@app.route("/")
def display():
    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="2">
    </head>
    <body style="background:black;color:white;font-family:Arial;padding:40px">
    <h1>Festival Wall</h1>
    """

    for msg in reversed(messages[-20:]):
        html += f"<p style='font-size:30px'>{msg}</p>"

    html += "</body></html>"
    return html


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            messages.append(msg)

    return """
    <html>
    <body style="font-family:Arial;padding:40px">
        <h1>Send Message</h1>
        <form method="POST">
            <input name="message" style="width:300px;height:40px">
            <button type="submit">Send</button>
        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    