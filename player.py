class Player:

    def __init__(self,
                 name: str,
                 salary: int,
                 years_left: int,
                 guaranteed: bool = True,
                 base_yr_comp: bool = False, #Base-year compensation flag
                 sign_and_trade: bool = False,
                 two_way: bool = False
                 ):
        self.name = name
        self.salary = salary
        self.years_left = years_left
        self.guaranteed = guaranteed
        self.base_yr_comp = base_yr_comp
        self.sign_and_trade = sign_and_trade
        self.two_way = two_way