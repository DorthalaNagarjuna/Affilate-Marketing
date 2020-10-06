from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Response, session
import requests
import json

app = Flask(__name__)
app.secret_key = "nagarjunapythondeveloper"


# this route will display the lender app home  page
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
