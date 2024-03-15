Feature: BDD

    @API_Testing_01
    Scenario: Test SOAP and REST API
        Given execute get method with the url "data_api_testing.json|:|url_get_method" the header "header_example_01.json" and body "body_example_01.json" that are located in the path "data_api_testing.json|:|dir_path" and validate the status code in "200"
        And execute post method with the url "data_api_testing.json|:|url_get_method" the header "header_example_02.json" and body "body_example_02.json" that are located in the path "data_api_testing.json|:|dir_path" and validate the status code in "200"
        And execute put method with the url "data_api_testing.json|:|url_get_method" the header "header_example_03.json" and body "body_example_03.json" that are located in the path "data_api_testing.json|:|dir_path" and validate the status code in "405"
        And from the WSDL "data_api_testing.json|:|wsdl" do the operator ADD with the first value "15" and the second value "3" and validate that the result must be "18"

        # Actividad a realizar --- ¿Cómo parametrizar el step para que sea posible agregar el método ADD y SUBTRACT en un solo step?:
        And from the WSDL "data_api_testing.json|:|wsdl" do the operator "ADD" with the first value "5" and the second value "8" and validate that the result must be "13"
        And from the WSDL "data_api_testing.json|:|wsdl" do the operator "SUBTRACT" with the first value "5" and the second value "8" and validate that the result must be "-3"


        # Actividad --- construir un escenario outline para ejecutar 5 operaciones de suma y 5 operaciones de resta. Provocar que 2 operaciones de suma sean incorrectas y que
        # 2 operaciones de resta sean incorrectas.

    @API_Testing_Actividad
    Scenario Outline: Validación masiva de SOAP API
        Given ...

    Examples:
        | operacion |   num_1   |   num_2   | resultado_esperado |
        | ADD       |   1       |   10      |   11               |