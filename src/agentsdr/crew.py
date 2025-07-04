from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Agentsdr():   

    agents: List[BaseAgent]
    tasks: List[Task]
   
    @agent
    def sdr(self) -> Agent:
        return Agent(
            config=self.agents_config['sdr'], # type: ignore[index]
            reasoning=True,
            max_reasoning_attempts= 3,
            verbose=True
        )    
   
    @task
    def start_conversation(self) -> Task:
        return Task(
            config=self.tasks_config['start_conversation'], # type: ignore[index]            
        )

    @crew
    def crew(self) -> Crew:       

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True,            
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
