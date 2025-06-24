from player import Player
class Team:

    SALARY_MIN = 139183000
    SALARY_CAP = 154647000
    FIRST_APRON = 195946000
    SECOND_APRON = 207825000

    def __init__(self, name, city, roster: list[Player]):
        self.name = name
        self.city = city
        self.roster = roster

    @property
    def payroll(self) -> int:
        return sum(p.salary for p in self.roster)
    
    def can_add_players(self, count: int) -> bool:
        return len(self.roster) + count <= 15 # Max of 15 players
    
    def incoming_salary_limit(self) -> int:
        """
         0-6.5M outgoing: 175% + 100K
        6.5-7.5M:        175% + 250K
        7.5M-29M:        125% + 100K
        >29M:            110% + 100K
        First/Second-apron hard caps apply.
        """

