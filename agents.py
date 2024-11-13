from crewai import Agent,LLM
from tools import tool


from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import os
#call the gemini models
llm = ChatGroq(model="groq/gemma-7b-it",
                             verbose=True,
                             temperature=0.5,
                             groq_api_key =os.getenv("GROQ_API_KEY"))

#Ccreating a researcher agent with memory and verbose mode

researcher = Agent(
    role="Senior Researcher",
    goal= 'Efficiently locate and retrieve relevant research papers on {topic}',
    verbose=True,
    memory = True,
    backstory = (
        "Driven by curiosity and you are eager to learn and find new things from different research papers and articles, eager to "
        " explore and share knowledge that could change the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

summarizer = Agent(
    role = "Summarizes papers to provide concise overviews.",
    goal = " Generate concise summaries of research papers to help users quickly understand the main contributions, methodologies, and results on {topic}",
    verbose= True,
    memory= True,
    backstory = (
        "Summarize long texts and provide concise bullet points or abstracts."
         "Highlight key findings, methods, and future directions from the papers."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

Question_Answering = Agent(
    role = "Provides answers to user-specific questions about the content of selected papers.",
    goal = "Answer user-specific questions related to the content of one or more selected research papers on   {topic}",
    verbose= True,
    memory= True,
    backstory = (
        "You are an expert and professional in answering all the user asked questions properly and relevantly."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

