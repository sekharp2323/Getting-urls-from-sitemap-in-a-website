import scrapy

class MySpider(scrapy.Spider):
    name = 'e'
    start_urls = ['a.com', 'b.com']

    def parse(self, response):
        # Extracting all URLs within the specified HTML element
        urls = response.css('.kwayy-html-sitemap-post-list a::attr(href)').extract()

        # Loop through each URL
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        # Extracting text content from the page
        text_content = response.css('::text').extract()

        # Combining the text content into a single string
        full_text = ' '.join(text_content).strip()

        # Saving the stripped text to a file
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(f'URL: {response.url}\n')
            f.write(full_text + '\n\n')

# To run the spider, use the following command in the terminal:
# scrapy runspider your_spider_file.py
