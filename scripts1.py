# https://github.com/Bynder/bynder-python-sdk

from bynder_sdk import BynderClient
import configparser

config = configparser.ConfigParser()
config.read('bynder.ini')

base_url=config.get('BYNDER_TOKENS', 'base_url'),
consumer_key=config.get('BYNDER_TOKENS', 'consumer_key'),
consumer_secret=config.get('BYNDER_TOKENS', 'consumer_secret'),
token=config.get('BYNDER_TOKENS', 'token'),
token_secret=config.get('BYNDER_TOKENS', 'token_secret')

bynder_client = BynderClient(
    base_url=base_url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    token=token,
    token_secret=token_secret
)

asset_bank_client = bynder_client.asset_bank_client

media_list = asset_bank_client.media_list()
print(media_list)

media_list = asset_service.media_list({
        'limit': 2,
        'type': 'image'
    })
print(media_list)

"""
asset_bank_client:
All the Asset Bank related calls, provides information and access to Media management.

    brands()
    media_list(query)
    media_info(media_id, query)
    meta_properties()
    tags()
    media_download_url()
    set_media_properties(media_id, query)
    delete_media(media_id)
    create_usage(itegration_id, asset_id, query)
    usage(query)
    delete_usage(integration_id, asset_id, query)
    upload_file(file_path, brand_id, media_id, query)
"""


"""
collection_client:
All the collection related calls.

    collections(query)
    collections_info(collection_id)
    create_collection(name, query)
    delete_collection(collection_id)
    collection_media_ids(collection_id)
    add_media_to_collection(collection_id, media_ids)
    remove_media_from_collection(collection_id, meedia_ids)
    share_collection(collection_id, collection_option, recipients, query)
"""