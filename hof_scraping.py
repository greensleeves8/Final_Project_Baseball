# Import dependencies
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
import datetime as dt
import os

GOOGLE_CHROME_BIN = "heroku:/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "C:/Users/16504/.wdm/drivers/chromedriver/win32/88.0.4324.96/chromedriver.exe"

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

def scrape_all():
    # Initiate headless driver for deployment
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    browser = Browser("chrome", executable_path=CHROMEDRIVER_PATH, headless=True)
    news_title, news_post = hallNews(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_post,
        "news_image": news_image(browser),
        "featured_image": featured_image(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def hallNews(browser):

    # Setting up URL/Page visit
    url = 'https://baseballhall.org/news'
    browser.visit(url)

    # Delay for loading page
    browser.is_element_present_by_css("div.story-ref div.desc", wait_time=1)

    # Set up browser for news page scraping
    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one("div.content.clearfix div.story-ref")
        # First post title from HOF news page
        post_title = slide_elem.find("h2").get_text()
        # First post description from HOF news page
        post_desc = slide_elem.find("div", class_="desc").get_text()

    except AttributeError:
        return None, None

    return post_title, post_desc


# Scraping Article Images
def news_image(browser):
    # Setting up URL/Page visit
    url = 'https://baseballhall.org/news'
    browser.visit(url)

    # Delay for loading page
    browser.is_element_present_by_css("div.story-ref div.desc", wait_time=1)

    # Set up browser for news page scraping
    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one("div.content.clearfix div.story-ref")
        # Find the relative image url for articles page
        img_post_url = slide_elem.find('img').get('src')

    except AttributeError:
        return None

    return img_post_url


def featured_image(browser):
    # Setting up URL/Page visit
    url = 'https://collection.baseballhall.org/'
    browser.visit(url)

    # Delay for loading page
    browser.is_element_present_by_css(
        "div.big-hero-container div.frontpage-image-inner", wait_time=1)

    # Setting up browser for collections gallery
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        img_elem = img_soup.select_one(
            "div.big-hero-container div.frontpage-image-inner")

        # Acquire image URL from collection site's header
        img_url = img_elem.find('img').get('src')

    except AttributeError:
        return None
    img_url = f"https://collection.baseballhall.org/{img_url}"
    return img_url


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
