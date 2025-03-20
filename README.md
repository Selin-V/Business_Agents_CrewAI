# CrewAI Business Agents - Simplified Version

Welcome to the simplified version of the **Business Agents** in the **CrewAI** framework. This version provides a basic setup for business agents like **Strategy**, **Marketing**, and **Sales**, with corresponding tasks and operations for each. 

### Requirements

Before you begin, make sure to set up the following environment:

1. **Python** (preferably version 3.8 or above).
2. **pip** (for managing Python packages).

### Getting Started

#### 1. Setting up the Environment

To set up your development environment, it’s recommended to create a **virtual environment** and install the required packages.

#### 2. Adding Your API Key

In order to use the AI agents, you’ll need to add your API key for the **Large Language Model (LLM)** that you want to use (e.g., OpenAI’s GPT-3 or GPT-4). Here’s how to set it up:

- **Method 1: Using `.env` File**
  
  The easiest way is to add your API key to a `.env` file. This file should be placed in the root of the project directory. Add the following line to it:

  ```bash
  OPENAI_API_KEY=your_api_key_here
  ```

  **Note**: Make sure to replace `your_api_key_here` with your actual API key from the LLM provider.

#### 3. Running the Project

Once your environment is set up and the API key is added, you can run the `main.py` script to execute the agents and see their results.

#### 4. Customizing the Agents

This setup includes three basic agents:

1. **StrategyAgent** - Handles strategic tasks like long-term planning and resource management.
2. **MarketingAgent** - Focuses on marketing-related tasks such as analyzing trends, creating campaigns, and engagement strategies.
3. **SalesAgent** - Handles tasks like sales reports, generating outreach emails, and improving sales pipelines.

You can customize these agents and add more by following the pattern in the existing agents (e.g., **StrategyAgent**, **MarketingAgent**, **SalesAgent**).

#### 5. Task Configuration

Tasks are loaded from the `tasks.yaml` file. This YAML file defines the different tasks the agents will perform. Each task includes:

- **name**: The task’s name.
- **agent**: The agent responsible for the task (strategy, marketing, or sales).
- **description**: A description of what the task involves.
- **expected_output**: The expected result of the task.

You can modify `tasks.yaml` to change the tasks or add new ones.

### Conclusion

This is a simplified version of the **Business Agents** in **CrewAI**, designed to help you get started with business automation using AI agents. By following the instructions above, you can set up the environment, add your API key, and customize the agents for your needs.

### Learning Process and AI Tools

I am currently in the learning process and have utilized AI tools to assist with the development of these business agents. These tools provided valuable insights and guidance throughout the process, helping to speed up the learning curve and development time. Feel free to ask any questions if you need further clarification on any aspect of the project!
