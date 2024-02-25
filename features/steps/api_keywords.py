from zeep import Client
import requests
from behave import *
import json

from features.steps.web_keywords import obtain_parameters_data


####################################################################################
###########            REST API Steps                   ############################
####################################################################################

@step(u'execute get method with the url "{url}" the header "{header_file}" and body "{body_file}" that are located in the path "{dir_path}" and validate the status code in "{status}"')
def execute_get_method_with_url_header_and_body(context, url, header_file, body_file, dir_path, status):
    if "|:|" in url:
        url = obtain_parameters_data(url)
    else:
        url = url

    if "|:|" in header_file:
        header_file = obtain_parameters_data(header_file)
    else:
        header_file = header_file

    if "|:|" in body_file:
        body_file = obtain_parameters_data(body_file)
    else:
        body_file = body_file

    if "|:|" in dir_path:
        dir_path = obtain_parameters_data(dir_path)
    else:
        dir_path = dir_path

    with open(dir_path + header_file) as file:
        header = json.load(file)
    with open(dir_path + body_file) as file:
        body = json.load(file)

    response = requests.get(url, headers = header, json = body)
    try:
        assert str(response.status_code) == str(status)
    except:
        raise Exception("The API status code is " + str(response.status_code))

@step(u'execute post method with the url "{url}" the header "{header_file}" and body "{body_file}" that are located in the path "{dir_path}" and validate the status code in "{status}"')
def execute_post_method_with_url_header_and_body(context, url, header_file, body_file, dir_path, status):
    if "|:|" in url:
        url = obtain_parameters_data(url)
    else:
        url = url

    if "|:|" in header_file:
        header_file = obtain_parameters_data(header_file)
    else:
        header_file = header_file

    if "|:|" in body_file:
        body_file = obtain_parameters_data(body_file)
    else:
        body_file = body_file

    if "|:|" in dir_path:
        dir_path = obtain_parameters_data(dir_path)
    else:
        dir_path = dir_path

    with open(dir_path + header_file) as file:
        header = json.load(file)
    with open(dir_path + body_file) as file:
        body = json.load(file)

    response = requests.post(url, headers = header, json = body)
    try:
        assert str(response.status_code) == str(status)
    except:
        raise Exception("The API status code is " + str(response.status_code))

@step(u'execute put method with the url "{url}" the header "{header_file}" and body "{body_file}" that are located in the path "{dir_path}" and validate the status code in "{status}"')
def execute_put_method_with_url_header_and_body(context, url, header_file, body_file, dir_path, status):
    if "|:|" in url:
        url = obtain_parameters_data(url)
    else:
        url = url

    if "|:|" in header_file:
        header_file = obtain_parameters_data(header_file)
    else:
        header_file = header_file

    if "|:|" in body_file:
        body_file = obtain_parameters_data(body_file)
    else:
        body_file = body_file

    if "|:|" in dir_path:
        dir_path = obtain_parameters_data(dir_path)
    else:
        dir_path = dir_path

    with open(dir_path + header_file) as file:
        header = json.load(file)
    with open(dir_path + body_file) as file:
        body = json.load(file)

    response = requests.put(url, headers = header, json = body)
    try:
        assert str(response.status_code) == str(status)
    except:
        raise Exception("The API status code is " + str(response.status_code))

####################################################################################
###########            SOAP API Steps                   ############################
####################################################################################

@step(u'from the WSDL "{WSDL}" do the operator ADD with the first value "{num_1}" and the second value "{num_2}" and validate that the result must be "{resultado_esperado}"')
def from_the_wsdl_do_the_ADD_with_the_first_value_and_the_second_value(context, WSDL, num_1, num_2, resultado_esperado):
    if "|:|" in WSDL:
        WSDL = obtain_parameters_data(WSDL)
    else:
        WSDL = WSDL

    client = Client(WSDL)
    result = client.service.Add(num_1, num_2)

    assert str(resultado_esperado) == str(result)


@step(u'from the WSDL "{WSDL}" do the operator "{operator}" with the first value "{num_1}" and the second value "{num_2}" and validate that the result must be "{resultado_esperado}"')
def from_the_wsdl_do_the_operator_with_the_first_value_and_the_second_value(context, WSDL, operator, num_1, num_2, resultado_esperado):
    if "|:|" in WSDL:
        WSDL = obtain_parameters_data(WSDL)
    else:
        WSDL = WSDL

    client = Client(WSDL)
    if operator.upper() == "ADD":
        result = client.service.Add(num_1, num_2)
    elif operator.upper() == "SUBTRACT":
        result = client.service.Subtract(num_1, num_2)
    else:
        raise Exception("Operación no existe en el WSDL")

    assert str(resultado_esperado) == str(result)