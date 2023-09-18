class Validator:
    @staticmethod
    def check_value(raw_value: str):
        """
        Checks user input value.
        :param raw_value: User input.
        :return: If value is correct, returns a tuple of float value and error message as None.
        If value is incorrect, returns a tuple of value as None and error message.
        """
        try:
            value = float(raw_value)

            if value < 0:
                return None, {"Error": f"Invalid value: {value}. Value must be positive."}
            return value, None

        except Exception:
            return None, {"Error": "Invalid type of value. Value must be float or integer."}

    @staticmethod
    def check_currency(currency_name: str, currencies: dict):
        """
        Checks if the currency exists.
        :param currency_name: Currency abbreviation.
        :param currencies: Available currencies.
        :return: If currency is existed, returns a tuple of currency nominal, value as float and error message as None.
        If currency isn`t existed, returns of currency nominal, value as None and error message.
        """
        if currency_name == "RUB":
            value = 1.0
            nominal = 1.0
        elif currency_name not in currencies:
            return None, None, {"Error": f"Invalid currency: {currency_name}. There is no such currency."}
        else:
            value = currencies[currency_name]["Value"]
            nominal = currencies[currency_name]["Nominal"]
        return nominal, value, None
