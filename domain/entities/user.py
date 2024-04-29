from core.domain.entity import Entity

class User(Entity):
    def __init__(self, fund, withdraw_limit, statement, withdraws, WITHDRAW_LIMITE):
        self.__fund = fund
        self.__withdraw_limit = withdraw_limit
        self.__statement = statement
        self.__withdraws = withdraws
        self.__withdraw_limite = WITHDRAW_LIMITE
        super().__init__()