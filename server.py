#!/usr/bin/env python

import requests
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def home():
    #home page
    return render_template("home.html")

@app.route('/working')
def serverTest():
    #testing and debug page
    return render_template("working.html")

@app.route('/lesson1')
def lesson1():
    #home page
    return render_template("lesson1.html")

@app.route('/lesson2')
def lesson2():
    #home page
    return render_template("lesson2.html")

@app.route('/lesson3')
def lesson3():
    #home page
    return render_template("lesson3.html")

@app.route('/lesson4')
def lesson4():
    #home page
    return render_template("lesson4.html")

@app.route('/lesson5')
def lesson5():
    #home page
    return render_template("lesson5.html")

if __name__ == '__main__':
    app.run()
