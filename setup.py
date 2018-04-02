from distutils.core import setup

setup(
    name="google_trends_scraper",
    packages=["google_trends_scraper"],  # this must be the same as the name above
    version="0.0.7",
    description="Google Trends Scraper makes scraping data from Google Trends incredibly easy, even formatting results as a Pandas Data Frame",
    long_description="Google Trends Scraper makes scraping data from Google Trends incredibly easy, even formatting results as a Pandas Data Frame.",
    author="Greg Hilston",
    author_email="Gregory.Hilston@gmail.com",
    url="https://github.com/GregHilston/Google-Trends-Scraper",  # use the URL to the github repo
    download_url="https://github.com/GregHilston/Google-Trends-Scraper/tarball/v0.0.7",
    keywords=["google", "trends", "scraper", "data", "dataset", "dataframe"],  # arbitrary keywords
    classifiers=[],
    install_requires=[
        "pandas",
        "selenium",
    ],
)
