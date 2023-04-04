from pymongo import MongoClient


uri = 'mongodb+srv://information.butnodh.mongodb.net/'
uri_settings = '&'.join('='.join(i) for i in {
    'authSource': '%24external',
    'authMechanism': 'MONGODB-X509',
    'retryWrites': 'true',
    'w': 'majority',
}.items())

client = MongoClient(
    f'{uri}?{uri_settings}', tls=True,
    tlsCertificateKeyFile='authentication/X509-cert-2061371920645933716.pem'
)
