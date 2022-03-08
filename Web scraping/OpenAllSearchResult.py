import requests, sys, webbrowser, bs4
print('Sreaching.......')
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
# res will hold the website link
res.raise_for_status()  # if the is any error occurs
soup = bs4.BeautifulSoup(res.text, 'html.parser')  #res.text will hold the content of that web page
linkElems = soup.select('.package-snippet') # this holds the link which is in the form of .package-snippet pattern
numopen = min(5, len(linkElems)) # this will hold the minimum integer value either 5 or the length of that list which is less than 5


for i in range(numopen): # loops for 5 times or less than that
    urlTooepn = 'https://pypi.org'+ linkElems[i].get('href')  # it will take links one by one
    print('Opening ',urlTooepn)
    webbrowser.open(urlTooepn)
