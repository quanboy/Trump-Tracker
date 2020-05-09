import requests
import json, operator
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='24c82007b3984a03acfafa571aed921b')

top_headlines = newsapi.get_top_headlines(q='trump',
                                      language='en',
                                      country= "us"
                                         )
headline = top_headlines['articles'][0]['title']

print (headline)
