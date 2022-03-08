# Project: Downloading All XKCD Comics

import requests, os, bs4
url = 'https://xkcd.com'   # starting url or front page url of the website
os.makedirs('xkcd', exist_ok=True)  # here create the directory and store the comics in ./xkcd

while not url.endswith('#'): # url if it ends with '#' then loop will break
    # TODO: Download the page. ====>  which doownloads first page of comic website
    print('Downloading page %s' %url)   # will get the first front page first and then prev
    res = requests.get(url)  # get the content of web page mentioned url
    res.raise_for_status() # if there is any error

    # TODO: Find the URL of the comic image.   ===> this is to find the only one image url present in that first comic page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')  # create beautiful soup and paas the content of requested site
    comicElem = soup.select('#comic img')   # pattern for searching a url that has comic image

    if comicElem == []:
        print('Could not find comic image')
    else:
        # TODO: Download the image.
        comicUrl = 'https:'+ comicElem[0].get('src')  # you will get url comivElem[0] we have only one url
        res = requests.get(comicUrl)  # downloading
        res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    # first we have to open the file every you want to download so create the file object
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)))
    # it will creates and open that file in xkcd folder which we have created
    # file name will be the base name
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # TODO: Get the Prev button's url
    prevLink = soup.select('a[rel = "prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done')
