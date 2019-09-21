import unittest
from selenium import webdriver
from code import times_scraper
#from code.times_scraper import get_browser_firefox


class TimesHomePageTest(unittest.TestCase):

    def test_times_archive_page_url_load(self):
        ts = times_scraper.TimesScraper()
        browser = ts.get_browser()
        browser2 = ts.get_times_archive_home_page(browser)
        self.assertIn('', browser2.title)

if __name__ == '__main__': 
    unittest.main() 
