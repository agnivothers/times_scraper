from selenium import webdriver


class TimesScraper:

    def greeting(self,name):
        print("Hello! ",name)

    def get_browser_firefox(self):
        browser = webdriver.Firefox()
        return(browser)
    def get_times_archive_home_page(self,browser):
        browser.get("https://epaper.timesgroup.com/TOI/TimesOfIndia/indialogin.aspx")
        return(browser)