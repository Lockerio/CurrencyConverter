class Converter:
    def convert(self, nominal1: int, value_in_RUB1: float, nominal2: int, value_in_RUB2: float, value: float = 1):
        currency_in_RUB1 = self.convert_currency_to_rub(nominal1, value_in_RUB1)
        currency_in_RUB2 = self.convert_currency_to_rub(nominal2, value_in_RUB2)

        multiplier = currency_in_RUB1 / currency_in_RUB2
        return multiplier * value


    @staticmethod
    def convert_currency_to_rub(nominal: int, value: float):
        if nominal == 1:
            return value
        return value / nominal
