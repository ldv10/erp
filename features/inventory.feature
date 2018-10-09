Feature: Check Inventory
In order to generate a bill
As a manager
I want to check if I can deliver the order checking the inventory


Scenario: Out of inventory
Given we have no inventory
When checked existence
Then we refuse the request

Scenario: Got inventory
Given we got product
When checked existence
Then we refuse the request

