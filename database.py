from pyairtable import Api


# api_key is a general variable but the base_id is specifically for the HGRMSF base
api_key = 'patZeMBA4dNElLfbp.fb12b8d190b52d1abc53d92308dd292f3bbe760bee758ac4ba57ebbf7dfbf576'
base_id = 'app4a29GBUnVXWIBt'

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
    if len(Articles.get(id)) == 0:
        return None
    else:
        return Articles.get(id)

