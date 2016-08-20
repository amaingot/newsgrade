import json
import jsonpickle
import newspaper
import elasticsearch
from datetime import datetime
from newspaper import Config, Article, Source

def tojson(article, source):
    doc = {
        'url': article.url,
        'source': source,
        'title': article.title,
        'authors': article.authors,
        'publish_date': article.publish_date,
        'fetch_date': datetime.now(),
        'top_image': article.top_image,
        'images': article.imgs,
        'movies': article.movies,
        'text': article.text,
        'summary': article.summary,
        'keywords': article.keywords,
        'meta_keywords': article.meta_keywords,
        'tags': article.tags,
        'html': article.html,
        'article_html': article.article_html,
    } 
    return doc



es = elasticsearch.Elasticsearch()
config = Config()
config.memoize_articles = False

url = "http://cbs.com"

print('[INFO] Getting newspaper, url: ' + url)
news = newspaper.build(url)
print('[INFO] Success: newspaper built, size: ' + str(news.size()))

for article in news.articles:
    print("[INFO] Downloading article, url: " + article.url)
    article.download()
    article.parse()
    article.nlp()
    print(article.title)
    es.index(index='news', doc_type='article', body=tojson(article, url))
    print('[INFO] Indexed article, Title: ' + article.title)


