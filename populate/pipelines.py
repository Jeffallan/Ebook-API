import requests
import os
from scrapy.exceptions import DropItem


class RequiredFields(object):

    def process_item(self, item, spider):

        required_fields = ['author', 'category']

        if all(field in item for field in required_fields):
            return item
        else:
            raise DropItem("***********************MISSING AUTHOR OR CATEGORY***********************")

#class DefaultValue(object):
#
#    def process_item(self, item, spider):
#        pass

class PopulateAPI(object):
    
    def process_item(self, item, spider):

        base = 'http://' + os.environ.get('API_HOST') + ':' + os.environ.get('API_PORT') + '/api/'
        search_category = 'categories/?search='
        search_author = 'authors/?search='
        author_ids = []
        category_ids = []
        author = item['author']
        category = item['category']

        for a in author:
            print("\n\nsearching for " + a + "\n\n")
            s_author = requests.get(base + search_author + a)
            if s_author.json()['results'] == []:
                p_author = requests.post(base + 'authors/', data = {'author': a})
                author_ids.append(p_author.json()['id'])
            else:
                author_ids.append(s_author.json()['results'][0]['id'])

        for c in category:
            print("\n\nsearching for " + c + "\n\n")
            #c.replace('&', '%26') ?
            s_cat = requests.get(base + search_category + c)
            if s_cat.json()['results'] == []:
                p_cat = requests.post(base + 'categories/', data = {'category': c})
                category_ids.append(p_cat.json()['id'])
            else:
                category_ids.append(s_cat.json()['results'][0]['id']) # add [0]

        data = {
                'isbin': item['isbin'], 
                'title': item['title'], 
                'subtitle': item['subtitle'], 
                'image_url': item['image'], 
                'year': item['year'], 
                'language': item['language'],
                'file_size': item['file_size'], 
                'file_format': item['file_format'],
                'description': item['description'], 
                'download_link': item['download_link'],
                'author': author_ids, 
                'category': category_ids
                }

        r = requests.post(base + 'books/', data=data)

        if r.ok:
            print("\n\n**************************SUCCESS**************************\n\n")
        else:
            print("\n\n*******************************ERROR***************************\n\n")
            raise DropItem(r.text)
            print("\n\n*******************************ERROR***************************\n\n")

        return item