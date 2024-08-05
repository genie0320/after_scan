# Request

## How to use
```python
# install requests
> pip install requests

# import module.
import requests

# make an requests.
URL = "http://httpbin.org"

response = requests.get(URL + "/get")

print(response.status_code)
print(response.text)
```

## The basics

### ■ Type of Request.
- get : Retrieves data from a specified resource.
- post : Sends data to a server to create a new resource.
- put : Updates an existing resource on the server.
- delete : Removes a specified resource from the server.

### ■ Common Status Code Categories.
#### 200-level Success:
`200` OK: The request was successful.     
`201` Created: The request has been fulfilled and resulted in a new resource being created.  
`204` No Content: The request was successful, but there is no content to return.   

#### 300-level Redirection:
`301` Moved Permanently: The requested resource has been permanently moved to a new location.     
`302` Found: The requested resource has been temporarily moved to a new location.     
`304` Not Modified: The client has data about the resource, and it hasn't been modified since the last request.   

#### 400-level Client Error:
`400` Bad Request: The server cannot or will not process the request due to an apparent client error.  
`401` Unauthorized: The request requires user authentication.     
`403` Forbidden: The server understood the request but refuses to fulfill it.  
`404` Not Found: The requested resource could not be found but may be available in the future.   

#### 500-level Server Error:
`500` Internal Server Error: A generic error message, often indicating a server-side issue.  
`503` Service Unavailable: The server is currently unable to handle the request.