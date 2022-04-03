# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
# import dependencies   
import pandas as pd
import datetime as dt

### SCRAPE ALL FUNCTION ###
# The function bellow initializes the browser, creates a dictionary, ends the WebDriver and returns the scraped data.
# define this function as "scrape_all" and then initiate the browser.

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemisphere": hemisphere_photos(browser)
    }
    

    # Stop webdriver and return data
    browser.quit()
    return data


### TITLE AND PARAGRAPH FUNCTION ###

# DEFINE THE FUNCTION FOR THE NEWS TITLE AND PARAGRAPH
def mars_news(browser):
    # Assign the url and instruct the browser to visit it.
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # set up the HTML parser
    #Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

### FEATURED IMAGE ###

# DEFINE THE FUNCTION FOR THE FEATURED IMAGE
def featured_image(browser):
    # start getting our code ready to automate all of the clicks
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button, which is the second image with the tag 'button' so let's use index [1].
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    
    return img_url

### MARS FACTS ###

def mars_facts():
     # Add try/except for error handling
    try:
      # use 'read_html" to scrape the facts table into a dataframe
      df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
    except BaseException:
      return None

    # we assign columns to the new DataFrame for additional clarity.
    df.columns=['Description', 'Mars', 'Earth']

    # we're turning the Description column into the DataFrame's index. 
    df.set_index('Description', inplace=True)

     # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")


### HEMISPHERE PHOTOS ###

def hemisphere_photos(browser):
    url = 'https://marshemispheres.com/'

    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    # Convert the browser html to a soup object - for the 4 images on the main page
    html = browser.html 
    hemisphere_soup = soup(html, 'html.parser')


    # finding the tags to the 4 images.
    four_images = hemisphere_soup.find_all("div", class_="description")

    # CREATE A FOR LOOP to get the link for the 4 hemisphere images and their titles.
    # go to the main page
    # find the url for the first image page (browser.visit)
    # find the first image url 

    for images in four_images:
        # going into each page of the 4.
        browser.visit(url + images.find("a")["href"])
        # read each page.
        html = browser.html 
        current_picture_page = soup(html, 'html.parser')
        # getting the address for all the 4 full images.
        image_address = current_picture_page.find("div", class_="downloads").find("a")["href"]
        full_image_address = url + image_address
        # get the images' titles.
        titles = current_picture_page.find("h2", class_= "title").text
        hemispheres = {"img_url": full_image_address,
                        "title": titles}
        # append the hemispheres dictionary to the hemisphere_image_urls list.              
        hemisphere_image_urls.append(hemispheres)


    # 4. return the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
