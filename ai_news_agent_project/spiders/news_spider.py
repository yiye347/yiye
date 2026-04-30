import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"

    start_urls = [
        "https://news.ycombinator.com/"
    ]

    def parse(self, response):
        titles = response.css(".titleline a::text").getall()
        links = response.css(".titleline a::attr(href)").getall()

        for title, link in zip(titles, links):
            yield {
                "title": title,
                "link": link
            }
