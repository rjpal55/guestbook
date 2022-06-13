import os
# import configparser
from flask import Flask, redirect, request, url_for
import logging
import sys

#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
# config = configparser.ConfigParser()
# has_config = config.read('vars.ini')

signatures = []

app = Flask(__name__)

# configurations
font = os.environ['DISPLAY_FONT']
font_color = os.environ['DISPLAY_COLOR']
environment = os.environ['ENVIRONMENT']

@app.route('/', methods=['GET'])
def index():
    html = """
    Signatures: <br />
    <font face="%(font)s" color="%(color)s">
        %(messages)s
    </font>

    <br /> <br />
    <form action="/signatures" method="post">
        Sign the Guestbook: <input type="text" name="message"><br>
        <input type="submit" value="Sign">
    </form>

    <br />
    <br />
    Debug Info: <br />
    ENVIRONMENT is %(environment)s
    """
    messages_html = "<br />".join(signatures)
    return html % {"font": font, "color": font_color, "messages": messages_html, "environment": environment}

@app.route('/signatures', methods=['POST'])
def write():
    message = request.form.get('message')
    signatures.append(message)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
