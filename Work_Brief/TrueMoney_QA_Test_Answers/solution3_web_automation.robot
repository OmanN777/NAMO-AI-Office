*** Settings ***
Library           SeleniumLibrary
Suite Setup       Set Selenium Implicit Wait    5 seconds
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            http://the-internet.herokuapp.com/login
${BROWSER}        chrome
${VALID_USER}     tomsmith
${VALID_PASS}     SuperSecretPassword!
${INVALID_PASS}   Password!
${INVALID_USER}   tomholland

*** Test Cases ***
Login Success
    [Documentation]    To verify that a user can login successfully when they put a correct username and password.
    Open Browser To Login Page
    Input Username    ${VALID_USER}
    Input Password    ${VALID_PASS}
    Click Login Button
    Verify Success Message    You logged into a secure area!
    Click Logout Button
    Verify Success Message    You logged out of the secure area!

Login Failed - Password Incorrect
    [Documentation]    To verify that a user can login unsuccessfully when they put a correct username but wrong password.
    Open Browser To Login Page
    Input Username    ${VALID_USER}
    Input Password    ${INVALID_PASS}
    Click Login Button
    Verify Error Message    Your password is invalid!

Login Failed - Username Not Found
    [Documentation]    To verify that a user can login unsuccessfully when they put a username that did not exist.
    Open Browser To Login Page
    Input Username    ${INVALID_USER}
    Input Password    ${INVALID_PASS}
    Click Login Button
    Verify Error Message    Your username is invalid!

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    The Internet
    Element Should Be Visible    id=username

Input Username
    [Arguments]    ${username}
    Input Text    id=username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id=password    ${password}

Click Login Button
    Click Button    css=button[type="submit"]

Click Logout Button
    Click Element    css=a.button[href="/logout"]

Verify Success Message
    [Arguments]    ${expected_msg}
    Wait Until Element Contains    id=flash    ${expected_msg}

Verify Error Message
    [Arguments]    ${expected_msg}
    Wait Until Element Contains    id=flash    ${expected_msg}
