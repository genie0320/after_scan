from altair import param
import requests

URL = "http://httpbin.org"

# response = requests.get(URL + "/get")

# print(response.status_code)
# print(response.text)

# response = requests.post(URL + "/post")

# print(URL + "/post")
# print(response.status_code)
# print(response.text)

# response = requests.put(URL + "/put")

# print(response.status_code)
# print(response.text)

# response = requests.delete(URL + "/delete")

# print(response.status_code)
# print(response.text)

# with Data *******************************************************
# method 01 : use params (better)
# params = {"data01": "genie", "data02": "nyanya"}
# response = requests.get(URL + "/get", params=params)

# method 02 : manipulate URL itself.
# URL = "http://httpbin.org/get?data1=genie&data2=nyanya"
# response = requests.get(URL)

# with Header *****************************************************
headers = {"Content-Type": "application/json; charset=utf-8", "test": "test"}
response = requests.get(URL + "/get", headers=headers)

# etc. ************************************************************
data = {"data01": "genie", "data02": "nyanya"}
response = requests.post(URL + "/post", headers=headers, data=data)

print(response.status_code)
print(response.text)
