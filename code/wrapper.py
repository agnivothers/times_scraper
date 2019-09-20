from code import times_scraper

def main():
    ts = times_scraper.TimesScraper()
    print(type(ts))
    print(ts)
    ts.greeting("Agniv Rivu")
    a = ts.get_browser_firefox()
    a = ts.get_times_archive_home_page(a)
    print(a)
if __name__=="__main__":
  main()


