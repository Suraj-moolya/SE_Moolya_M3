Feature: XX PLCSimulator

@test0002b
Scenario Outline: Start PLC Simulator
When I Run PLC Simulator
And I click on Start button on PLC Simulator
Examples:
  | SlNo. |
  | 1     | 
  
@test0002b
Scenario Outline: Change port number of simulator to 503 
When I change port number of simulator to 503
And I click on Start button on PLC Simulator
Examples:
  | SlNo. |
  | 1     |
