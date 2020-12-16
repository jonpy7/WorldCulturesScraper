"""
By Juan Peralta Web Scrapping Project: The followign script has the porpuse to learn a little bit more about each culture.

On first phase we are scrapping The World Cultures Encyclopedia to realize how many cultures and descritpions. 

"""
from app import db, Countries, CultureOfCountries, WorldCultures
from worldcultures import scrape, scrape_world_cult

url = "https://www.everyculture.com/"
webscraper = scrape(url)
world_cults = scrape_world_cult(url)

def dbloader():
# this function should run after scraping the web data to load it into db 
    # db.create_all()
    for country,description in webscraper.items():
        new_row = Countries(CountryName=country, CountryDescription=description)
        print(new_row)
        db.session.add(new_row)
        db.session.commit()    
        
        #return rows
    for culture,url in world_cults.items():
        new_row = WorldCultures(CultureCountryGroup=culture, CountryGroupURL=url)
        print(new_row)
        db.session.add(new_row)
        db.session.commit() 


if __name__ == '__main__':
    dbloader()