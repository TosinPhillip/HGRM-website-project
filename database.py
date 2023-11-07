from pyairtable import Api
import os


# api_key is a general variable but the base_id is specifically for the HGRMSF base
# api_key = os.environ.get('AIRTABLE_API')
# base_id = os.environ.get('HGRMSF_BASE_ID')

api_key = 'patZeMBA4dNElLfbp.fb12b8d190b52d1abc53d92308dd292f3bbe760bee758ac4ba57ebbf7dfbf576'
base_id = 'app4a29GBUnVXWIBt'

# This is our callpoint
api = Api(api_key) # type: ignore



# This is the instance of the Articles table.
# Each article has tables [ID, Title, Text, Writers, Photo and Date]
Articles = api.table(base_id, 'Articles') # type: ignore

ITEMS_PER_PAGE=10

def load_articles_from_airtable(page):
    """Returns a list of dictionaries of articles in the table"""
    p = []
    for a in Articles.iterate(page_size=ITEMS_PER_PAGE):
        p.append(a)
    return p[page]


def load_article_from_airtable(id):
    """Pulls a specific article dictionary"""
    return Articles.get(id)


Media = api.table(base_id, 'Media')

def load_media():
    """Pulls a list of dictionaries of media in the table"""
    m = Media.all()
    return m
# def paginate(list_bunch=None, item_number=10):
#     """This function gets a list of items and an item number. It then returns the list in batches of item number"""
#     # bunch_length = len(list_bunch)
#     # number_of_pages = None
    
    



# x = Articles.get('recN8Y2TZ5sX33RZd')['fields']['Photo']
# # print(x[0]['thumbnails']['full']['url'])
# 