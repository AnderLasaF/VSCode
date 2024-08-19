#The principle of TDD is to write the tests before writing the code. We are going to see the benefits with the following class
#TDD consists of 5 steps:
#1: Write tests
#2: Run the tests (they should all fail. This means that we are adding a new feature)
#3: Write the simplest code so that the tests pass
#4: Make all tests pass (inlcuding old tests)
#5: Refactor and improve the code
#This process is also called Red-Green-Refactor. 
"""
Very advanced Employee management system.
"""
from dataclasses import dataclass


@dataclass
class Employee:
    """Basic representation of an employee."""

    name: str
    employee_id: int
    pay_rate: float = 100.0
    hours_worked: float = 0.0
    employer_cost: float = 1000.0
    commission: float = 100.0
    contracts_landed: int = 0

    @property
    def has_commission(self) -> bool:
        """Whether the employee has a commission."""
        return self.commission > 0

    def compute_payout(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.pay_rate * self.hours_worked + self.employer_cost
        if self.has_commission:
            payout += self.commission * self.contracts_landed
        return payout