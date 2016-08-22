# AWS User
aws_username = "newsgrade"
aws_user_arn = "arn:aws:iam::785737117780:user/newsgrade"
aws_user_key = "AKIAI2ODIREQJFIENNMA"
aws_user_secret = "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"

# AWS ElasticSearch
es_arn = "arn:aws:es:us-west-2:785737117780:domain/newsgrade"
es_host = "search-newsgrade-t4pnjg5kef3ozua5zewycmjvii.us-west-2.es.amazonaws.com"
es_endpoint = "https://" + es_host
es_region = "us-west-2"
kb_endpoint = "http://search-newsgrade-t4pnjg5kef3ozua5zewycmjvii.us-west-2.es.amazonaws.com/_plugin/kibana/"
es_newsindex = "news"
es_newsdoctype = "article"

# AWS SQS (Simple Queuing System)
sqs_endpoint = "https://sqs.us-west-2.amazonaws.com/785737117780/newsgrade-queue"
sqs_name = "newsgrade-queue"
sqs_region = "us-west-2"
sqs_arn = "arn:aws:sqs:us-west-2:785737117780:newsgrade-queue"

# AWS Database (Postgres)
db_arn = "arn:aws:rds:us-west-2:785737117780:db:newsgrade"
db_endpoint = "newsgrade.cruvslizqrbe.us-west-2.rds.amazonaws.com"
db_port = "3306"
db_region = "us-west-2"
db_name = "newsgradedb"
db_username = "newsgrade"
db_password = "9k$Pd8hT1%lt"
db_vpc = "vpc-6b8da40f"