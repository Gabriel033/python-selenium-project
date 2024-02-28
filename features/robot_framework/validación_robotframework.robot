*** Settings ***
# Se deben de agregar 2 espacios después de la etiqueta Library
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Visit google
    # Hay que tener indentación de 4 espacios. Los pasos se indican
    # con palabras en inglés. No se usa código, se utilizan enunciados.
    # Se colocan 4 espacios después de colocar el step a ejecutar.
    # Se colocan 3 espacios después de poner la URL, para indicar el driver.
    # para emular una tecla del teclado de la computadora, se ocupa código ASCII
    Open Browser    https://www.google.com/   Chrome
    Input text    xpath://*[@name='q']   nintendo
    Sleep   5s
    Press Key    name:q   \\13
    Sleep   10s
    close browser

*** Keywords ***