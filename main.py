from pymongo import MongoClient
from pandas import read_csv

import constants


client = MongoClient(
    f'{constants.URI}?{constants.URI_SETTINGS}', tls=True,
    tlsCertificateKeyFile=constants.CERTIFICATE_FILEPATH
)


def csv_to_database(mongo_client: MongoClient, csv_filepath: str) -> None:
    db = mongo_client[constants.DATABASE_NAME]
    collection = db[csv_filepath.split('/')[-1].split('.')[0]]

    df = read_csv('data/2023.csv')
    collection.insert_many(df.to_dict('records'))


if __name__ == '__main__':
    csv_to_database(client, 'data/2023.csv')
