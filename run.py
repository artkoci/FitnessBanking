import bunq_client
import Strava

NEW_SHOE_PRICE = 110.00
SHOE_REPLACE = 600.00
EURO_PER_KM_CONST = NEW_SHOE_PRICE / SHOE_REPLACE

bunq_client.client()

def running_debt()-> float:
    """
    Calculates distance left to pay
    :return: amount to be paid
    """
    distance_paid = bunq_client.get_account_balance()
    distance_ran = Strava.main()
    distance_to_euro = distance_ran * EURO_PER_KM_CONST
    distance_leftover_EUR = round(distance_to_euro - distance_paid, 2)

    return distance_leftover_EUR


def main():
    bunq_client.make_payment(amount_euro=running_debt())


if __name__ == '__main__':
    main()