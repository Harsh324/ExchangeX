from exchange import exchange_functions


class TestExchange():

    def __init__(self) -> None:
        pass

    def test_convert(self):
        assert exchange_functions.Exchange.convert() == 80.24

    def test_parse_api(self):
        pass

