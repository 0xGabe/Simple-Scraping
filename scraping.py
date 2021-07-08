from urllib.request import urlopen

html = urlopen('http://testphp.vulnweb.com/')
print(html.read())
