"""
By Juan Peralta Web Scrapping Project: The followign script has the porpuse to learn a little bit more about each culture.

On first phase we are scrapping The World Cultures Encyclopedia to realize how many cultures and descritpions. 

"""
# set up your scraping below
import requests
from bs4 import BeautifulSoup

worldcultures = []
Urls = []
culture_countries = [] #Countries Names
culture_desc = []

def scrape(url):
    # url = "https://www.everyculture.com/"
    req = requests.get(url)
    cont = req.text
    soup = BeautifulSoup(cont, 'lxml')
    lst = soup.findAll('h2')[2:]

    #Get first level details and print them
    for item in lst:
        worldcultures.append(item.text)
        Urls.append(url+item.a['href'])
    
    #Get second level details from URLs collected in first level
    for u in Urls:
        response = requests.get(u)
        content = response.text
        sp = BeautifulSoup(content,'lxml')
        h2s = sp.find_all('h2')
        descs = sp.find_all('p')
        for idx,h2 in enumerate(h2s):
            culture_countries.append(h2.text[1:-1])
            culture_desc.append(descs[idx].text)

    countrs_n_descript = {countr:dscript for kc,countr in enumerate(culture_countries[1:]) for kd,dscript in enumerate(culture_desc[1:]) \
                if kc == kd}
    return countrs_n_descript # Return the dictionary

def scrape_world_cult(url):
    req = requests.get(url)
    cont = req.text
    soup = BeautifulSoup(cont, 'lxml')
    lst = soup.findAll('h2')[2:]

    #Get first level details and print them
    for item in lst:
        worldcultures.append(item.text)
        Urls.append(url+item.a['href'])
    
    world_cults = {culture_grp:url for ck,culture_grp in enumerate(worldcultures) for uk,url in enumerate(Urls) if ck==uk}
    return world_cults