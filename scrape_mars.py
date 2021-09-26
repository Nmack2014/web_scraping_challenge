

import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager




#path = {"executable_path": "chromedriver.exe"}
path = {'executable_path': ChromeDriverManager().install()}
browser = Browser("chrome", **path, headless=False)

def scrape():

    #FEATURED IMAGE AQUISITION-------------------------------------------------
    url = "https://redplanetscience.com/"
    
    browser.visit(url)
    url_html = browser.html
    url_soup = BeautifulSoup(url_html, "html.parser")
    
    title = url_soup.find("div", class_="content_title").text
    paragraph = url_soup.find("div", class_="article_teaser_body").text
    
    url_html = browser.html
    
    url_soup = BeautifulSoup(url_html, "html.parser")
    
    
    
    
    
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)
    html_image = browser.html
    image_soup = BeautifulSoup(html_image, "html.parser")
    
    
    image_path = image_soup.find('img',class_='headerimage fade-in')
    
    
    
    
    featured_tag = image_path.get("src")
    
    
    featured_image_url = (image_url+featured_tag)
    
    #FACTS DATAFRAME CREATION ---------------------------------------------------
    facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)
    html_facts = browser.html
    facts_soup = BeautifulSoup(html_facts, "html.parser")
    
    
    fact_path = facts_soup.find('table',class_='table table-striped')
    
    
    facts = fact_path.text
    
    
    
    facts_df = pd.read_html(facts_url)[0]
    
    
    
    
    facts_df = facts_df.drop([2], axis=1)
    
    
    
    facts_df = facts_df.rename({0: "Metric", 1: "Quantity"}, axis=1)
    
    
    #------------------------------------------------------------------------
    
    #PLANET IMAGE AQUISITION-------------------------------------------------
    planet_list = {}
    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)
    hemisphere_html = browser.html
    hemisphere_soup = BeautifulSoup(hemisphere_html, "html.parser")
    
    
    
    links = hemisphere_soup.find_all("div",class_='item')
    
    planet_list["Cerberus"] = links[0].findChild("a")['href']
    planet_list["Schiaparelli"] = links[1].findChild("a")['href']
    planet_list["Syrtis Major"] = links[2].findChild("a")['href']
    planet_list["Valles Marineris"] = links[3].findChild("a")['href']
    
    
    
    
    cerberus_url = hemisphere_url + planet_list["Cerberus"]
    schiaparelli_url = hemisphere_url + planet_list["Schiaparelli"]
    syrtis_major_url = hemisphere_url + planet_list["Syrtis Major"]
    valles_marineris_url = hemisphere_url + planet_list["Valles Marineris"]
    
    
    image_list = {}
    browser.visit(cerberus_url)
    cerberus_html = browser.html
    cerberus_soup = BeautifulSoup(cerberus_html, "html.parser")
    
    
    
    links2 = cerberus_soup.find_all("img",class_='wide-image')
    
    
    
    image_list["Cerberus"] = hemisphere_url + links2[0].get('src')
    
    
    browser.visit(schiaparelli_url)
    schiaparelli_html = browser.html
    schiaparelli_soup = BeautifulSoup(schiaparelli_html, "html.parser")
    links3 = schiaparelli_soup.find_all("img",class_='wide-image')
    image_list["Schiaparelli"] = hemisphere_url + links3[0].get('src')
    
    
    browser.visit(syrtis_major_url)
    syrtis_major_html = browser.html
    syrtis_major_soup = BeautifulSoup(syrtis_major_html, "html.parser")
    links4 = syrtis_major_soup.find_all("img",class_='wide-image')
    image_list["Syrtis Major"] = hemisphere_url + links4[0].get('src')
    
    
    browser.visit(valles_marineris_url)
    valles_marineris_html = browser.html
    valles_marineris_soup = BeautifulSoup(valles_marineris_html, "html.parser")
    links5 = valles_marineris_soup.find_all("img",class_='wide-image')
    image_list["Valles Marineris"] = hemisphere_url + links5[0].get('src')
    
    #Appoend featured image to existing dict
    
    image_list["featured"] = featured_image_url
    
    #IMAGE LIST IS A DICTIONARY OF IMAGE URLS
    
    
    #converting fact df into dict and appending to image_list dict
    
    facts_dict = facts_df.to_dict()
    image_list["facts_table"] = facts_dict
    

    
    #RETURN NEEDED VALUES-----------------------------------------------------------------
    
    return image_list 
    

    browser.quit()





