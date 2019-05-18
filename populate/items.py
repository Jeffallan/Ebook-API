from scrapy.item import Item, Field


class EbookItem(Item):

    title = Field()
    subtitle = Field()
    image = Field()
    author = Field()
    isbin = Field()
    year = Field()
    pages = Field()
    language = Field()
    file_size = Field()
    file_format = Field()
    category = Field()
    description = Field()
    download_link = Field()

    # Hosekeeping fields
    # url = Field()
    # project = Field()
    # spider = Field()
    # server = Field()
    # date = Field()