# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
# import pandas
import pandas as pd


# set your executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

### TITLE AND PARAGRAPH ###

# DEFINE THE FUNCTION FOR THE NEWS TITLE AND PARAGRAPH
def mars_news(browser):
    # Assign the url and instruct the browser to visit it.
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
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
    url = 'https://spaceimages-mars.com'
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
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

### MARS FACTS ###

def mars_facts():
     # Add try/except for error handling
    try:
      # use 'read_html" to scrape the facts table into a dataframe
      df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
      return None


    # we assign columns to the new DataFrame for additional clarity.
    df.columns=['description', 'Mars', 'Earth']

    # we're turning the Description column into the DataFrame's index. 
    df.set_index('description', inplace=True)

     # Convert dataframe into HTML format, add bootstrap
    return df.to_html()




# quite the browser so it doesn't keep running.
browser.quit()
