# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:57:11 2020

@author: tomcs
"""

from flask_auth import hello

def test_hello():
    assert hello() == "hello"