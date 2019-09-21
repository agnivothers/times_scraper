import unittest
from selenium import webdriver
from code import times_scraper



class TimesHomePageTest(unittest.TestCase):

    def setUp(self):
        ts = times_scraper.TimesScraper()
        self.ts = ts # Learning Python Testing, Pg. 88 How to use objects created in setUP method by other methods

    def test_times_archive_page_url_load(self):
        browser = self.ts.get_browser()
        browser = self.ts.get_times_archive_home_page(browser)
        self.assertIn('', browser.title)
    """
    def test_login_credentials(self):
        (username,password) = self.ts.get_login_credentials()
        self.assertEqual(username,"Username","The username did not match")
        self.assertEqual(password, "Password", "The password did not match")
    """
if __name__ == '__main__': 
    unittest.main() 
