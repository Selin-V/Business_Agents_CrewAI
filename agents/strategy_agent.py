from crewai import Agent

class StrategyAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Strategy & Branding Expert",
            goal="Develop and refine business branding, ensuring a strong, authentic presence.",
            backstory="A highly experienced branding strategist with a deep understanding of market positioning and brand messaging.",
            verbose=True
        )