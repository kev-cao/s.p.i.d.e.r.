import pyotp
import robin_stocks
import robin_stocks.robinhood as r

class RobinhoodAPI:

    def __init__(self, username, password, mfa_key):
        """
        Connects to the Robinhood API.

        Params:
        - username (string) : The login username for the account.
        - password (string) : The login password for the account.
        - mfa_key (string) : The multifactor authentication key for the account.
        """
        totp = pyotp.TOTP(mfa_key).now()
        login = r.login(username, password, mfa_code=totp) 

    def get_doge_price(self):
        """
        Gets the current ask price for DOGE.

        Returns:
        - (float) : The asking price for DOGE stock.
        """
        info = r.crypto.get_crypto_quote('DOGE')
        return float(info['ask_price'])

    def get_buying_power(self):
        """
        Gets the buying power of the connected account.

        Returns:
        - (float) : The buying power of the account.
        """
        return float(r.profiles.load_account_profile('buying_power'))

    def limit_purchase_doge_by_price(self, amountInUSD):
        """
        Purchases a set monetary amount of DOGE crypto with limits on crypto price.

        Params:
        - amountInUSD (float) : The amount of DOGE to purchase, in USD.
        """
        if amountInUSD > self.get_buying_power():
            raise ValueError('You are attempting a purchase that exceeds your buying power.')

        doge_price = self.get_doge_price()
        shares = amountInUSD // doge_price
        r.orders.order_buy_crypto_limit('DOGE', shares, doge_price + .002)
