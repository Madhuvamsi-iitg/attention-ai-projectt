from crewai import Crew,Process
from tasks import research_task,summarise_task,QA_task
from agents import researcher,summarizer,Question_Answering

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[researcher,summarizer,Question_Answering],
    tasks=[research_task,summarise_task,QA_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)