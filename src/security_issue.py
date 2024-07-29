# Security issue ./scr/1-security-issue.py
def log_credentials_noncompliant():
    import boto3
    import logging
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key

    # Noncompliant: credentials are written to the logger.
    logging.info('Access key: ', access_key)
    logging.info('secret access key: ', secret_key)