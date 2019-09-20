from selenium import webdriver


class TimesScraper:

    def greeting(self,name):
        print("Hello! ",name)

    def get_browser(self):
        browser = webdriver.Chrome()
        return(browser)
    def get_times_archive_home_page(self,browser):
        browser.get("https://epaper.timesgroup.com/TOI/TimesOfIndia/indialogin.aspx")
        return(browser)

