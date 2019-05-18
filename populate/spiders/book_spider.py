from scrapy.spiders import SitemapSpider
from populate.items import EbookItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from datetime import date
import socket
import re


class BookSpider(SitemapSpider):
    name = "book"
    sitemap_urls = [
        "http://www.allitebooks.com/post-sitemap1.xml",
        "http://www.allitebooks.com/post-sitemap2.xml",
        "http://www.allitebooks.com/post-sitemap3.xml",
        "http://www.allitebooks.com/post-sitemap4.xml",
        "http://www.allitebooks.com/post-sitemap5.xml",
        "http://www.allitebooks.com/post-sitemap6.xml",
        "http://www.allitebooks.com/post-sitemap7.xml",
        "http://www.allitebooks.com/post-sitemap8.xml",
    ]
    # TODO add sitemap rules as regex
    # sitemap_urls = ['http://www.allitebooks.com/sitemap_index.xml']
    # sitemap_rules = [
    #                 ('/post-sitemap/', 'parse_book'),
    #                 ]

    def parse(self, response):

        l = ItemLoader(item=EbookItem(), response=response)

        # Primary Fields
        l.add_xpath("title", "//header/h1/text()", MapCompose(lambda i: i.strip()))
        # TODO add custom pipeline to append subtitle if key doesn't
        # l.add_xpath('subtitle',
        #        '//header/h4/text()',
        #        MapCompose(lambda i: i.strip()), default=' ')

        l.add_value("subtitle", "N/A")  # not all books have subtitles

        l.add_xpath(
            "image",
            '//img[contains(@class,"attachment-post-thumbnail")]/@src',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "author",
            '//div[contains(@class, "book-detail")]//dd[1]/a/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "isbin",
            '//div[contains(@class, "book-detail")]//dd[2]/text()',
            MapCompose(lambda i: i.strip(), lambda i: i.replace("-", "")),
        )
        l.add_xpath(
            "year",
            '//div[contains(@class, "book-detail")]//dd[3]/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "pages",
            '//div[contains(@class, "book-detail")]//dd[4]/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "language",
            '//div[contains(@class, "book-detail")]//dd[5]/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "file_size",
            '//div[contains(@class, "book-detail")]//dd[6]/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "file_format",
            '//div[contains(@class, "book-detail")]//dd[7]/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "category",
            '//div[contains(@class, "book-detail")]//dd[8]//a/text()',
            MapCompose(lambda i: i.strip()),
        )
        l.add_xpath(
            "description",
            '//div[contains(@class,"entry-content")]',
            MapCompose(
                lambda s: s.replace("\n", ""),
                lambda s: s.replace("\b", ""),
                lambda s: s.replace("\f", ""),
                lambda s: s.replace("\r", ""),
                lambda s: s.replace("\t", ""),
                lambda s: s.replace("\v", ""),
                lambda s: s.replace("\x00", ""),
                lambda i: i.strip(),
                # TODO check for other stray characters
            ),
        )
        l.add_xpath(
            "download_link",
            '//a[contains(@href,"file")]/@href',
            MapCompose(lambda s: s.replace(" ", "%20"), lambda i: i.strip()),
        )

        # TODO where to add Housekeeping Fields
        # l.add_value('url', response.url)
        # l.add_value('project', self.settings.get('BOT_NAME'))
        # l.add_value('spider', self.name)
        # l.add_value('server', socket.gethostname())
        # l.add_value('date', date.today())

        return l.load_item()
