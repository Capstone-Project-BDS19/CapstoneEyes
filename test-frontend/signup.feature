Feature: Capstone System Sign-Up Form

    Background: Open signup screen
        Given Launch any browser
        When Open system home page 
        And User presses the Signup button 
    
    Scenario: User clicks create your account with valid credentials
        When Enter email "<email>", username "<username>", password "<password>", and repeatPassword "<repeatPassword>"
        And Click on Create your account button
        Then User shall be redirected to the Login page

        Examples:
            | email                   | username         | password     | repeatPassword  |
            | straykids2503@jyp.com   | straykids2503    | Straykids123 | Straykids123    | 
        
        Examples:
            | email                        | username          | password     | repeatPassword  |
            | capstoneproject123@spj.org   | capstone123       | fighting123  | fighting123     | 

    
    Scenario: User signs up using an existing email
        When Enter email "<email>", username "<username>", password "<password>", and repeatPassword "<repeatPassword>"
        And Click on Create your account button
        Then User shall receive an error message notifying them email id must be unique 

        Examples:
            | email                   | username         | password     | repeatPassword  |
            | nhilai1105@gmail.com    | nhilai0000       | Straykids123 | Straykids123    | 

    
    Scenario: User signs up using an existing username
        When Enter email "<email>", username "<username>", password "<password>", and repeatPassword "<repeatPassword>"
        And Click on Create your account button
        Then User shall receive an error message notifying them username must be unique 

        Examples:
            | email                   | username         | password     | repeatPassword  |
            | nhilai0212@gmail.com    | nhilai           | Straykids123 | Straykids123    | 

    
    Scenario: User signs up but repeating password incorrectly
        When Enter email "<email>", username "<username>", password "<password>", and repeatPassword "<repeatPassword>"
        And Click on Create your account button
        Then User shall receive an error message notifying them they repeated password incorrectly

        Examples:
            | email                   | username         | password     | repeatPassword  |
            | nhilai0212@gmail.com    | nhilai2003       | Straykids123 | staykids123     | 

    Scenario: User signs up but using short password
        When Enter email "<email>", username "<username>", password "<password>", and repeatPassword "<repeatPassword>"
        And Click on Create your account button
        Then User shall receive an error message notifying them they password must have at least 8 characters

        Examples:
            | email                   | username         | password  | repeatPassword  |
            | nhilai0212@gmail.com    | nhilai2003       | skz123    | skz123          | 


    
