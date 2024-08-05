# beautifulsoap4

## How to use
```python
# install
> pip install beautifulsoup4

# import module.
import requests
from bs4 import BeautifulSoup as bs

# make an requests.
URL = "http://httpbin.org"
response = requests.get(URL)

soup = bs(response.text, "html.parser")
result = soup.find("title")
print(result)
print(result.text)
```

## The basics

### ■ selecters
- `soup.find('p')` : Finds the first occurrence of a tag with the specified name.
```python    
`soup.find('p', limit=2) # get the first 2.
`soup.find('p', 'users') # get 'p' with option 'users'
`soup.find('p', class_='users') # get 'p' with option 'users'
`soup.find('p', attrs ={'class':'users'}) # get 'p' with option 'users'
`soup.find(id = 'welcome')
```
- `soup.find_all('p')` : Finds all occurrences of a tag with the specified name.
```python    
`soup.find_all(attrs={'attribute_name': 'attribute_value'})
```
- `soup.select('.my_div')` : Uses CSS selectors to find elements.

- soup.select_one('.my_div')
- soup.select('.my_div')
```python
result = soup.select_one('#my_div.bold.blue') # chaining이 가능하다.
```
#### CSS selectors
~ : 를 포함
```python
target_p = soup.select('p.target ~ p')
```
^ : 으로 시작 
```python
https_links = soup.select('a[href^="https://"]')  
```
$ : 으로 끝나는 
```python
jpg_images = soup.select('img[src$=".jpg"]')
```
* : 를 포함하는
```python
fruit_links = soup.select('a[href*="apple"]')
```

### ■ filder and extract
1. 다음과 같이 계속해서 범위를 좁혀 나갈 수 있다. 
```python
result = soup.find('p')
result2 = result.find('div') 

# 다음과 같이 체이닝이 가능하다.
result = soup.find('p').find('div')
```
2. 원하는 요소를 잡았다면, text등을 추출할 수 있다.
```python
result.text # 태그 내의 텍스트만 추출
result.httrs
result.attrs['option_name'] # 태그 내의 옵션을 추출할 수 있다.
```

### ■ Navigator
- `parent`: Accesses the parent element.
- `children`: Accesses all child elements.
- `next_sibling`: Accesses the next sibling element.
- `previous_sibling`: Accesses the previous sibling element.

### ■ etc.
- `get_text()`: Extracts text from an element.
- `string`: Extracts the string content of an element.
- `attrs`: Accesses element attributes as a dictionary.

