#! /usr/bin/python
# -*- coding:utf-8 -*-

## MODULES
from flask import *
from pexpect import *
import os
import sys
import re

## VARIABLES
app = Flask(__name__)

## MAIN
@app.route('/')
def main():
    return render_template('main.html')

## NETSCAN TOOLS
@app.route('/netscan_tools/')
def netscan_tools():
	return render_template('netscan_tools.html')

## IFCONFIG GET
@app.route('/ifconfig/')
def ifconfig():
    result = os.popen('ifconfig').readlines()
    out = ""
    for line in result:
    	if "flags" in line or "inet" in line:
    		out = out + line + "<br>"
    return render_template('netscan_tools.html', output=out)

## IFCONFIG POST
@app.route('/ifconfig/', methods=['POST'])
def ifconfig_post():
    text = request.form['text']
    processed_text = text.upper()
    return render_template('netscan_tools.html', output=out)

## PROGRAM
if __name__ == '__main__':
    app.run(debug=True)

