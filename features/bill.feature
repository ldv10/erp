Feature: Generate Bill

Scenario: Generate a Bill 
Given We could generate bills
When an order is requested
Then we print the bill
