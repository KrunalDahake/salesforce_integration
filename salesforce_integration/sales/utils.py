from simple_salesforce import Salesforce
from salesforce_integration.settings import SALESFORCE_USERNAME, SALESFORCE_SECURITY_TOKEN, SALESFORCE_PASSWORD, SALESFORCE_DOMAIN

def login():
    return Salesforce(
        username=SALESFORCE_USERNAME,
        password=SALESFORCE_PASSWORD,
        security_token=SALESFORCE_SECURITY_TOKEN,
        domain=SALESFORCE_DOMAIN
    )