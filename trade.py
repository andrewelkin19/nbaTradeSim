from dataclasses import dataclass, field
from team import Team
from player import Player

@dataclass
class Trade:
    team_a: Team
    team_b: Team
    outgoing_a: list[Player]
    outgoing_b: list[Player]

    def validate(self):
        errors = []

        sal_out_a = sum(p.salary for p in self.outgoing_a)
        sal_out_b = sum(p.salary for p in self.outgoing_b)
        sal_in_a = sum(p.salary for p in self.outgoing_b)
        sal_in_b = sum(p.salary for p in self.outgoing_b)

        payroll_a_before = self.team_a.payroll
        payroll_b_before = self.team_b.payroll
        payroll_a_after = payroll_a_before - sal_out_a + sal_in_a
        payroll_b_after = payroll_b_before - sal_out_b + sal_in_b
