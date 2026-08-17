*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       https://potterapi-fedeperin.vercel.app

*** Test Cases ***
Get House Data Success
    [Documentation]    To verify get house data api will return correct data when index=3.
    Create Session    potter_api    ${BASE_URL}    verify=True
    ${response}=      GET On Session    potter_api    /en/houses    params=index=3    expected_status=200
    Status Should Be    200    ${response}
    ${json_body}=     Set Variable    ${response.json()}
    Should Be Equal As Strings    ${json_body['house']}      Slytherin
    Should Be Equal As Strings    ${json_body['emoji']}      🐍
    Should Be Equal As Strings    ${json_body['founder']}    Salazar Slytherin
    Should Be Equal As Strings    ${json_body['animal']}     Snake
    Should Be Equal As Integers   ${json_body['index']}      3
    ${colors}=        Get From Dictionary    ${json_body}    colors
    List Should Contain Value     ${colors}    green
    List Should Contain Value     ${colors}    silver

Get House Data But User Not Found
    [Documentation]    To verify get house data api from invalid index. The api will return 404 not found.
    Create Session    potter_api    ${BASE_URL}    verify=True
    ${response}=      GET On Session    potter_api    /en/houses    params=index=5    expected_status=404
    Status Should Be    404    ${response}
    ${json_body}=     Set Variable    ${response.json()}
    Should Be Equal As Strings    ${json_body['error']}    Invalid Index
