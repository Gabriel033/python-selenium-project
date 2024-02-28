*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${navegador}  Chrome
${pagina}  https://gmail.com/
${usuario}  correo@gmail.com
${pass}  password_inventada

*** Test Cases ***
Ingresar cuenta de correo en gmail
    Open Browser    ${pagina}   ${navegador}
    Input Text    id:identifierId   ${usuario}
    Click Element    xpath://*[@id="identifierNext"]//button[1]
    Sleep    10s
    Input Text    name:Passwd   ${pass}
    Click Element    xpath://*[@id="passwordNext"]//button[1]
    Sleep    10s
    Close Browser

*** Keywords ***