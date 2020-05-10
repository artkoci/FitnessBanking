import warnings
warnings.filterwarnings("ignore")

from bunq.sdk.context.api_context import ApiContext
from bunq.sdk.context.api_environment_type import ApiEnvironmentType
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.generated.object_ import Pointer, Amount, NotificationFilter
from bunq.sdk.http.pagination import Pagination
from bunq.sdk.model.generated import endpoint

import json

with open('local-settings.json') as f:
    config = json.load(f)

CURRENCY = 'EUR'
PAYMENT_DESCRIPTION = 'Your hard earned KMs turned into £££'
ENVIRONMENT_TYPE = ApiEnvironmentType.PRODUCTION
API_KEY = config['bunq_api_key']
DEVICE_DESCRIPTION ='Shoe models'

def client(environment_type=ENVIRONMENT_TYPE,
           api_key=API_KEY,
           device_description=DEVICE_DESCRIPTION):
    apiContext = ApiContext.create(environment_type,
                                   api_key,
                                   device_description)
    apiContext.ensure_session_active()
    BunqContext.load_api_context(apiContext)


def make_payment(amount_euro, payment_description=PAYMENT_DESCRIPTION):
    if amount_euro > 0.0:
        endpoint.Payment.create(
            amount=Amount(str(amount_euro), CURRENCY),
            monetary_account_id=config['paying_monetary_accout_id'],
            counterparty_alias=Pointer(config['bunq_pointer_type'],
                                       config['receive_monetary_IBAN'],
                                       config['receive_user_name']),
            description=payment_description
        )
    else:
        print("No running distance to pay. Run more fatboy/girl! 🏃‍")


def get_account_balance():
    pagination = Pagination()
    pagination.count = 100

    saving_monetary_account_bank = endpoint.MonetaryAccountSavings.list(
        pagination.url_params_count_only).value

    for monetary_account_bank in saving_monetary_account_bank:
        if monetary_account_bank.description==config["receive_monetary_account_name"]:
            balance = float(monetary_account_bank.balance.value)
            return balance