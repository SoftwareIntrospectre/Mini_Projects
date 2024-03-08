'''
    following along with this to learn: https://realpython.com/python-web-scraping-practical-introduction/
'''

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

# print(page)

html_bytes = page.read()
# print(html_bytes)

html = html_bytes.decode("utf-8")
# print(html)
 

title_index = html.find("<title>")
print(title_index)


start_index = title_index + len("<title>")
print(start_index)


end_index = html.find("</title>")
print(end_index)

# extract the title from between the start and end index (Python list slicing)
title = html[start_index:end_index]
print(title)