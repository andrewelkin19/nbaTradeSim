class Team:

    SALARY_MIN = 139183000
    SALARY_CAP = 154647000
    FIRST_APRON = 195946000
    SECOND_APRON = 207825000

    def __init__(self, name, city, roster, totalSalary):
        self.name = name
        self.city = city
        self.roster = roster
        self.totalSalary = totalSalary

    def trade(self, otherTeam):

