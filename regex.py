import re

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

import re

text = "abbb a ab aaaa"
matches = re.findall(r'ab*', text)
print(matches)

import re

text = "ab abb abbb abbbb"
matches = re.findall(r'ab{2,3}', text)
print(matches)

import re

text = "hello_world test_string Invalid_Word"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)

import re

text = "Hello World TEST Python"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)

import re

text = "a123b axxb a---b ab ac"
matches = re.findall(r'a.*?b', text)
print(matches)

import re

text = "Hello, world. Python is cool"
result = re.sub(r'[ ,.]', ':', text)
print(result)

text = "hello_world_test"

parts = text.split("_")
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print(camel)

import re

text = "HelloWorldPython"
result = re.findall(r'[A-Z][^A-Z]*', text)
print(result)

import re

text = "helloWorldPython"
snake = re.sub(r'([A-Z])', r'_\1', text).lower()
print(snake)

