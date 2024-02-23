*** Settings ***
Library    RequestsLibrary
Library   DependencyLibrary
Suite Teardown    Delete All Sessions

*** Variables ***
${TARGET}    http://app-test-my-app.127.0.0.1.nip.io

*** Test Cases ***
Get a pet
    [Documentation]    Test GET a pet endpoint
    [Tags]    GET    test:retry(5)

    Create Session    my_pet_api    ${TARGET}

    Wait Until Keyword Succeeds    3 times    0.5 sec    Get pet and validate response

*** Keywords ***
Get pet and validate response
    [Documentation]    GET a pet using the app endpoint
    ...                The answer should be a pet (dog, cat, bird)

    ${response}=    GET On Session   my_pet_api    /pet
    Should Be Equal As Strings    ${response.status_code}    200

    Should Be True    '${response.content}'=='Dog' or '${response.content}'=='Cat' or '${response.content}'=='Bird'