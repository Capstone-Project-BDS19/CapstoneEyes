Feature: Capstone System Log-In Form

    Background: Open login screen
        Given Launch Chrome browser for login
        When Open system homepage for login
        And User clicks the Login button 

    Scenario: User has not had account so must create one
        When Click on Register now
        Then User shall be redirected to signup screen
    
    Scenario Outline: User logs in with valid credentials
        When Enter email "<email>", password "<password>"
        And Click on Login button
        Then User shall be redirected to the Homepage

        Examples:
            | email                 | password     |
            | nhilai1105@gmail.com  | yennhi12345  | 


    Scenario Outline: User logs in with unregistered email id
        When Enter email "<email_login>", password "<password_login>"
        And Click on Login button
        Then User shall receive an error message notifying the email has not been registered

        Examples:
            | email                      | password     |
            | nhi.bs19bds003@spjain.org  | yennhi12345  | 


    Scenario Outline: User logs in with incorrect password
        When Enter email "<email>", password "<password>"
        And Click on Login button
        Then User shall receive an error message notifying the password is incorrect

        Examples:
            | email                 | password     |
            | nhilai1105@gmail.com  | yennhi1234   | 


    Scenario Outline: User leaves blanks when logging in
        When Enter email "<email>", password "<password>"
        And Click on Login button
        Then User shall receive an error message notifying them they must fill in required details

        Examples:
            | email                 | password |
            | nhilai1105@gmail.com  | ""       | 

        Examples:
            | email     | password     |
            | ""        | yennhi1234   | 
