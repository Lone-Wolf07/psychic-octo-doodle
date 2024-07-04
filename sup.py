from selenium import webdriver

#start the session
driver = webdriver.Chrome()

#access website through url using the .get function
website_url = "https://en.wikipedia.org/wiki/Web_scraping"
driver.get(website_url)

#let the website load, we know my net sucks so...
driver.implicitly_wait(2)

#get the title 
title = driver.title
print(title)

soup = driver.page_source     #gives the html code (same thing that beautifulSoup does)

#stop the session 
driver.quit()
