class Converter:
    def convert(self, nominal1: int, value_in_RUB1: float, nominal2: int, value_in_RUB2: float, value: float = 1):
        """
        Converts the amount of one currency to another currency.
        :param nominal1: Currency 1 nominal.
        :param value_in_RUB1: Currency 1 value.
        :param nominal2: Currency 2 nominal.
        :param value_in_RUB2: Currency 2 value.
        :param value: Amount of 1 currency.
        :return: The value of a quantity of currency in a currency 2.
        """
        currency_in_RUB1 = self.convert_currency_to_rub(nominal1, value_in_RUB1)
        currency_in_RUB2 = self.convert_currency_to_rub(nominal2, value_in_RUB2)

        multiplier = currency_in_RUB1 / currency_in_RUB2
        return multiplier * value

    @staticmethod
    def convert_currency_to_rub(nominal: int, value: float):
        """
        Converts the currency nominal to one.
        :param nominal: Currency nominal.
        :param value: Currency value in RUB.
        :return: Converted currency nominal.
        """
        if nominal == 1:
            return value
        return value / nominal
