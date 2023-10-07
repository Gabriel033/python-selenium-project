from behave.__main__ import main

tags = ("Escenario_01")

if __name__ == '__main__':
    main("-f allure_behave.formatter:AllureFormatter -o reports/ -f pretty --no-capture --no-color -k --tags "+str(tags)+"")