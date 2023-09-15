from pyairtable import Api
import os


# api_key is a general variable but the base_id is specifically for the HGRMSF base
api_key = os.environ.get('AIRTABLE_API')
base_id = os.environ.get('HGRMSF_BASE_ID')

# This is our callpoint
api = Api(api_key)



# This is the instance of the Articles table.
# Each article has tables [ID, Title, Text, Writers, Photo and Date]
Articles = api.table(base_id, 'Articles')

def load_articles_from_airtable():
    """Returns a list of dictionaries of articles in the table"""
    return Articles.all()


def load_article_from_airtable(id):
    """Pulls a specific article dictionary"""
    return Articles.get(id)


# x = Articles.get('recN8Y2TZ5sX33RZd')['fields']['Photo']
# # print(x[0]['thumbnails']['full']['url'])
# print(x)


