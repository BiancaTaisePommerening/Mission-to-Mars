# Mission-to-Mars

## Project Overview

Web scraping with HTML/CSS


The purpose of this project is to perform web scraping on the Mission to mars website and 


## Web Scraping Methods

- Chrome Developer Tools were use to identify HTML components.

- Python script was written using Splinter was used to automate the browser.

- BeautifulSoup, another Python library, was used to extract the data. 

- The NoSQL database MongoDB was used to store the scraped data.

- Flask was used to create the Mission to Mars web applycation, containning a button that executes the scraping code and updates the page with newest data.

- HTML and CSS were used to customize the web application.

- Bootstrap was used to give the web application extra polish.


### **Mars News**
![mars_news](./Resources/mars_news.png)


### **Featured Mars Image** 

![featured_mars_image](./Resources/featured_mars_image.png)



### **Mars Facts**

![mars_facts](./Resources/mars_facts.png)

### **Mars Hemispheres Images**


![mars_hemispheres_1](./Resources/mars_hemispheres_1.png)

![mars_hemispheres_2](./Resources/mars_hemispheres_2.png)


### **Styling the Web Application**

A few extra modifications were done at the end of the project using a Bootstrap stylesheet and also some inline CSS as well.

- Using Bootstrap stylesheet:

    - Color of the Scrape Button was changed from blue to white.
    - Mars facts table was modified to be "table responsive" so it would adjust according to the size of the screen of the device been used - (the other sections were already altered to be responsive earlier on the project).
    - Mars Facts Table was styled to have outer borders and color alternating rows by adding **class="table table-bordered table-striped"** inside its table tag.
    - Mars Facts title was adjusted to be centered by adding **class="text-center"** inside its opening heading tag.

- Using Inline CSS:

    - The page's background color was modyfied to light orange, by adding **style= "background-color:rgba(255, 166, 0, 0.404)**
    - The jumbotron's background color was chnaged to orange.
    - The Scrape Button's text color was chnaged to orange.