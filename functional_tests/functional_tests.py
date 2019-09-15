from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://epaper.timesgroup.com/TOI/TimesOfIndia/indialogin.aspx")
assert '' in browser.title
browser.close()

