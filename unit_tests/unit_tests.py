import unittest
from selenium import webdriver
from code import times_scraper



class TimesHomePageTest(unittest.TestCase):

    def setUp(self):
        ts = times_scraper.TimesScraper()
        self.ts = ts

    def test_times_archive_page_url_load(self):
        browser = self.ts.get_browser()
        browser = self.ts.get_times_archive_home_page(browser)
        self.assertIn('', browser.title)


if __name__ == '__main__': 
    unittest.main() 
