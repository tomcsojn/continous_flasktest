# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:34:23 2019

@author: Tamas
"""

import numpy as np
import pandas as pd
from flask import Flask,request,g
import re
import os
import sys
import json
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(script_dir)

users = {'username': ['user1','admin'],'pass': ['pass1','pass2']}
users = pd.DataFrame(users)

@app.route('/',methods=['GET'])
def hello():
    return "hello"
#password required
@app.route('/secure',methods=['GET'])
@auth.login_required
def security():
    return "$hello$"+g.username
#get password from dataframe with plain text
@auth.verify_password
def verify_password(username, password):
    if(users[users.eq(username).any(1)].empty):
        return False
    else:
        g.username = username
        return (users[users.eq(username).any(1)]['pass']==password)[1]
    
        

#%%Main
if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port=5000)