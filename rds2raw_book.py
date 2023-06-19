import logging
import traceback
import boto3

from project.common.db_utils import create_connection, fetch_data_by_sql, create_binary_from_list_data
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    try:
        logger.info(f"EVENT: {event}")
        logger.info(f"CONTEXT: {context}")
        connection = create_connection()

        query_str_sql = "select * from book_store"
        results = fetch_data_by_sql(connection, query_str_sql)

        csv_binary = create_binary_from_list_data(results)

        client = boto3.client('s3')
        client.put_object(
            Body=csv_binary.read(), 
            Bucket='ai4e-ap-southeast-1-dev-s3-data-landing',
            Key='khanghoang/book_test.csv'
        )

        connection.close()
    except Exception as ex:
        logger.error(f'FATAL ERROR: {ex} %s')
        logger.error('TRACEBACK:')
        logger.error(traceback.format_exc())
