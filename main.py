from flask import Flask, request, jsonify, render_template
import json

import

app = Flask(__name__)

app.secret_key("SECRETSECRETSECRET")

@app.route('/', methods=['GET'])
def display_page():
    #
    render_template()

