*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${navegador}  Chrome
${pagina}  https://gmail.com/
${usuario}  correo@gmail.com
${pass}  password_inventada

*** Test Cases ***
Ingresar cuenta de correo en gmail
    Abrir_correo
    Ingresar_a_correo
    Cerrar_Navegador


*** Keywords ***
Abrir_correo
    Open Browser    ${pagina}   ${navegador}

Ingresar_a_correo
    Input Text    id:identifierId   ${usuario}
    Click Element    xpath://*[@id="identifierNext"]//button[1]
    Sleep    10s
    Input Text    name:Passwd   ${pass}
    Click Element    xpath://*[@id="passwordNext"]//button[1]
    Sleep    10s

Cerrar_navegador
    Close Browser