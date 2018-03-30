from google_trends_scraper.google_trends_scraper import GoogleTrendsScraper

gts = GoogleTrendsScraper("It Is Wednesday My Dude", "2018-03-01", "2018-03-14", seconds_delay=30)

results = gts.scrape()

print(results)