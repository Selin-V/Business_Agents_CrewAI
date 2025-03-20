import yaml
import crewai
from agents.strategy_agent import StrategyAgent
from agents.marketing_agent import MarketingAgent
from agents.sales_agent import SalesAgent
from crewai import Task

# To initialize CrewAI agents
strategy_agent = StrategyAgent()
marketing_agent = MarketingAgent()
sales_agent = SalesAgent()

# Create a mapping for correct agent assignment
agent_mapping = {
    "strategy_agent": strategy_agent,
    "marketing_agent": marketing_agent,
    "sales_agent": sales_agent
}

# Load tasks from tasks.yaml
with open("tasks.yaml", "r") as file:
    tasks_data = yaml.safe_load(file)["tasks"]

# Convert tasks to CrewAI's Task format
tasks = [
    Task(
        name=task["name"],
        agent=agent_mapping[task["agent"]],  # Use mapping to get correct agent
        description=task["description"],
        expected_output=task["expected_output"]
    ) for task in tasks_data
]

# Initialize Crew
crew = crewai.Crew(
    agents=[strategy_agent, marketing_agent, sales_agent],
    tasks=tasks  # Correctly formatted task assignments
)

def run_agents():
    """Run CrewAI Business Agents"""
    print("🚀 Starting CrewAI Business Agents...")
    
    # Run the updated CrewAI execution method
    results = crew.kickoff()
    
    # Print output results
    for agent, result in zip(crew.agents, results):
        print(f"\n {agent.role} Output:\n{result}\n")

if __name__ == "__main__":
    run_agents()