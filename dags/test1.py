convert, no-ip, svc-ssh-office, svc-web-google-lb


from airflow import DAG
from airflow.contrib.operators.mysql_to_gcs import MySqlToGoogleCloudStorageOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'palo',
    'start_date': datetime(2019, 4, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('mysql_to_bq_tbloffers2', default_args=default_args)


slack_msg="AHOJ"


slack_notify =  SlackWebhookOperator(
    task_id='slack_notify',
    http_conn_id='slack_connection',
    webhook_token='T0ABU3TUZ/B6CS9G4FK/W0zhCF783PcDLb0VezElnoqK',
    message=slack_msg,
    channel='#webhook-default',
    username='airflow',
    icon_emoji=None,
    link_names=False,
    dag=dag)

for
counter = 0
if tablerowcount > 5000

export = MySqlToGoogleCloudStorageOperator(
    task_id='extract_tbloffers',
    mysql_conn_id='mysql_1111',
    google_cloud_storage_conn_id='google_cloud_storage_default',
    sql='SELECT * FROM profesia_test.tblOffers where offer_id > $COUNTER order by offer_id asc limit 1000  ',

    bucket='nada-test-profesia-data',
    filename='palo/tbloffers2.json',
    schema_filename='palo/schemas/tbloffers2.json',
    dag=dag)


load = GoogleCloudStorageToBigQueryOperator(
            task_id="load_tbloffers",
            bigquery_conn_id='bigquery_default',
            google_cloud_storage_conn_id='google_cloud_storage_default',
            bucket='nada-test-profesia-data',
            destination_project_dataset_table="nada_transfer1.tbloffers",
            source_objects=["palo/tbloffers2.json"],
            schema_object="palo/schemas/tbloffers2.json",
            source_format='NEWLINE_DELIMITED_JSON',
            create_disposition='CREATE_IF_NEEDED',
            write_disposition='WRITE_TRUNCATE',
            project_id='test-data-profesia-sk',
            dag=dag)
			
load.set_upstream(export)

slack_notify.set_upstream(load)


CREATE TABLE `heartbeat` (
  `id` int(11) NOT NULL,
  `ts` datetime NOT NULL,
  PRIMARY KEY (`id`)
) 

