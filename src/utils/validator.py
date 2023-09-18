class Validator:
    @staticmethod
    def check_value(raw_value):
        try:
            value = float(raw_value)

            if value < 0:
                return None, {"Error": f"Invalid value: {value}. Value must be positive."}
            return value, None

        except Exception:
            return None, {"Error": "Invalid type of value. Value must be float or integer."}

    @staticmethod
    def check_currency(currency_name: str, currencies: dict):
        if currency_name == "RUB":
            value = 1.0
            nominal = 1.0
        elif currency_name not in currencies:
            return None, None, {"Error": f"Invalid currency: {currency_name}. There is no such currency."}
        else:
            value = currencies[currency_name]["Value"]
            nominal = currencies[currency_name]["Nominal"]
        return nominal, value, None
