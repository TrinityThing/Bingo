from pony import orm

db = orm.Database()
db.bind(
    provider='postgres',
    user='ppzlghqmclthps',
    password='34ca5fb72f30f09b3713a9af1b65da2b1da657d29095cfc37fd4c772a8648f70',
    host='ec2-54-220-0-91.eu-west-1.compute.amazonaws.com',
    database='d9qdmq2bc3vjpj')
