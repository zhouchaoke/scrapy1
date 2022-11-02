import scrapy
from demo2.items import SchoolbagItem
from bs4 import UnicodeDammit
from scrapy.selector import Selector
class MySpider(scrapy.Spider):
    name = "mySpider"
    key = '%CA%E9%B0%FC'
    source_url = 'http://search.dangdang.com/'
    # url = source_url + "?key=" + key
    # start_urls = [url]

    def start_requests(self):
        url = MySpider.source_url + "?key=" + MySpider.key
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        try:
            dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            # selector = scrapy.Selector(text=data)
            selector =Selector(text=data)
            lis = selector.xpath("//div[@dd_name='普通商品区域']/ul[@class='bigimg']/li")
            for li in lis:
                picture = li.xpath("./p[@class='name']/a/@href").extract_first()
                price = li.xpath("./p[@class='price']/span/text()").extract_first()
                title = li.xpath("./p[@class='name']/a/@title").extract_first()
                hot_word = li.xpath("./p[@class='name']/p[@class='search_hot_word']/text()").extract_first()
                comment = li.xpath("./p[@class='star']/a[@name='itemlist-review']/text()").extract_first()
                publisher = li.xpath("./p[@class='link']/a[@name='itemlist-shop-name']/text()").extract_first()

                item = SchoolbagItem()
                item["picture"] = picture.strip() if title else ""
                item["price"] = price.strip() if title else ""
                item["title"] = title.strip() if title else ""
                item["hot_word"] = hot_word.strip() if title else ""
                item["comment"] = comment.strip() if title else ""
                item["publisher"] = publisher.strip() if title else ""
                yield item
        except Exception as err:
            print(err)

