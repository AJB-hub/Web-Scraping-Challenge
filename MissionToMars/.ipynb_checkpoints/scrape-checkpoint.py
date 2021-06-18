#Web Scraping
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import typing



#Connection Function
def connect(url:str) -> str:
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    #Page URL
    browser.visit(url)
    
    #Soup Creation
    html = browser.html
    cout = BeautifulSoup(html, 'html.parser')
    
    #Exit Browser
    browser.quit()

    return cout


def scrape() -> dict:
    
    scrapeDict = {}
    
    
    #First Link ---------------------------------------------------------------------------------
    
    url = 'https://redplanetscience.com/'
    soup = connect(url)

    d = {'news_title': soup.find_all('div', class_ = 'content_title')[0].text,
         'news_p': soup.find_all('div', class_ = 'article_teaser_body')[0].text
    }
    scrapeList.append(d)
    
    #Second Link ---------------------------------------------------------------------------------
    
    url = 'https://spaceimages-mars.com/'
    soup = connect(url)

    featured_url = soup.find_all('img', class_ = 'headerimage fade-in')[0]['src']
    
    d = {'image_url': url + featured_url}
    
    scrapeList.append(d)
    
    #Third Link ---------------------------------------------------------------------------------
    
    url = 'https://galaxyfacts-mars.com/'

    mars_df = pd.read_html(url)[1]
    
    d = {'mars_table': mars_df.to_html()}
    
    scrapeList.append(d)
    
    #Fourth Link ---------------------------------------------------------------------------------
    url = 'https://marshemispheres.com/'

    soup = connect(url)

    #scrape all relative paths
    rel_path_list = soup.find_all('a', class_ = 'itemLink product-item')
    html_path = [path['href'] for path in rel_path_list]

    #remove duplicates
    html_path = list(set(html_path))

    #remove blank paths
    temp_html = []
    for path in html_path:
        if path[0] != '#':
            temp_html.append(path)
    html_path = temp_html

    #Append url to relative path
    html_path = [url + path for path in html_path]

    #Visit each url and pull the image url and title
    image_path = []
    for path in html_path:
        image_dict = {}
        #try:
        #visit each path and load html
        soup = connect(path)

        #find relevant data from html soup
        title_text = soup.find_all('h2', class_='title')[0].text
        img_url = url + (soup.find_all('a')[3]['href'])

        #add data to list dict obj 
        image_dict['title'] = title_text[0:len(title_text)-9]
        image_dict['img_url'] = img_url 
        image_path.append(image_dict)       

    d = {'hemi_info': image_path}
    
    scrapeList.append(d)
    
    return scrapeList
    
    
    
    
    
    
    
    
    
    
    

