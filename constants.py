# MongoDB login
# noinspection SpellCheckingInspection
CERTIFICATE_FILEPATH = 'authentication/X509-cert-2061371920645933716.pem'
URI = 'mongodb+srv://information.butnodh.mongodb.net/'
URI_SETTINGS = '&'.join('='.join(i) for i in {
    'authSource': '%24external',
    'authMechanism': 'MONGODB-X509',
    'retryWrites': 'true',
    'w': 'majority',
}.items())

# MongoDB database constants
DATABASE_NAME = 'eurovision'
