#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: leonel
"""

from behave import *

@given('we could generate bills')
def step_impl(context):
    pass

@when('an order is requested')
def step_impl(context):
    assert True is not False
    
@then('we print the bill')
def step_impl(context):
    assert context.failed is False
