#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:20:15 2018

@author: leonel
"""

from behave import *

@given('we have no inventory')
def step_impl(context):
    pass

@when('checked existence')
def step_impl(context):
    assert True is not False
    
@then('we refuse the request')
def step_impl(context):
    assert context.failed is False
    
@given('we got product')
def step_impl(context):
    pass