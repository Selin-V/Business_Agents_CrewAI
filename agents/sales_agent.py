from crewai import Agent

class SalesAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Sales & Revenue Expert",
            goal="Create and refine sales strategies to maximize business revenue.",
            backstory="A sales expert with a deep knowledge of revenue optimization, customer acquisition, and business expansion strategies.",
            verbose=True
        )