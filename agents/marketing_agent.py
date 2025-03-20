from crewai import Agent

class MarketingAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Marketing & Digital Strategy Expert",
            goal="Develop and implement digital marketing strategies for business growth.",
            backstory="A marketing strategist with a strong background in digital campaigns, audience engagement, and data-driven insights.",
            verbose=True
        )