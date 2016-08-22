import jsonpickle
import newspaper
import elasticsearch
import hashlib
import certifi
import settings
import boto.sqs
from boto.sqs.message import Message
from datetime import datetime
from awses.connection import AWSConnection
from newspaper import Config, Article, Source

def tojson(article, source):
    doc = {
        'url': article.url,
        'source': str(source),
        'title': article.title,
        'authors': article.authors,
        'publish_date': str(article.publish_date),
        'fetch_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'top_image': article.top_image,
        'images': article.imgs,
        'movies': article.movies,
        'text': article.text,
        'summary': article.summary,
        'keywords': article.keywords,
        'meta_keywords': article.meta_keywords,
        'tags': list(article.tags),
        #'html': article.html,
        #'article_html': article.article_html,
    } 
    return doc

def createid(url):
    hash = hashlib.sha1(url)
    hash_val = hash.hexdigest()
    return str(hash_val)

es = elasticsearch.Elasticsearch(connection_class=AWSConnection,
                   region=settings.es_region,
                   host=settings.es_host,
                   access_key=settings.aws_user_key,
                   secret_key=settings.aws_user_secret)

sqs = boto.sqs.connect_to_region(
                settings.sqs_region,
                aws_access_key_id=settings.aws_user_key,
                aws_secret_access_key=settings.aws_user_secret)
queue = sqs.get_queue(settings.sqs_name)

config = Config()
config.memoize_articles = False

url = "http://cnn.com"

print('[INFO] Getting newspaper, url: ' + url)
news = newspaper.build(url=url, config=config)
print('[INFO] Success: newspaper built, size: ' + str(news.size()))

for article in news.articles:
    print("[INFO] Downloading article, url: " + article.url)
    
    # Newspaper: downloading, parsing, and doing the natural language processing
    article.download()
    article.parse()
    article.nlp()
    
    # Formatting json and article id
    article_body = jsonpickle.encode(tojson(article, url))
    article_id = createid(article.url)
    
    # ElasticSearch: Indexing article
    es.index(index=settings.es_newsindex , doc_type=settings.es_newsdoctype, id=article_id, body=article_body)
    
    # SQS: Creating the message and queuing message 
    m = Message()
    m.set_body("Analyze article: " + article_id)
    m.message_attributes = {
        "article_id": {
            "data_type": "String",
            "string_value": article_id
        },
        "article_url": {
            "data_type": "String",
            "string_value": article.url
        },
        "article_title": {
            "data_type": "String",
            "string_value": article.title
        },
        "timestamp": {
            "data_type": "String",
            "string_value": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "action": {
            "data_type": "String",
            "string_value": "analyze"
        }
    }
    queue.write(m)
    
    print('[INFO] Indexed and queued article, Title: ' + article.title)