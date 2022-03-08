import bs4, requests

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(noStarchSoup.text[:500])


exampleFile = open('example.html')
examplsoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(examplsoup.text[:])
elems = examplsoup.select('#author')     # [<span id="author">Al Sweigart</span>]
print(elems)
print(elems[0])
# <span id="author">Al Sweigart</span>
print(elems[0].getText())
# Al Sweigart