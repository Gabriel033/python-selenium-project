from zeep import Client

client = Client('https://ecs.syr.edu/faculty/fawcett/Handouts/cse775/code/calcWebService/Calc.asmx?WSDL')
result = client.service.Add(4, 5)

assert result == 9
print("The response from the soap request is: " + str(result))



import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 0,
    "title": "José Gabriel API Automation Testing",
    "dueDate": "2024-02-25T07:26:26.950Z",
    "completed": True
  }

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                         headers = header,
                         json = request_payload)

print(response.status_code)
print(response.json())