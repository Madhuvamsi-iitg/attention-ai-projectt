from crewai import Task
from tools import tool
from agents import researcher,summarizer,Question_Answering

research_task = Task(
  description=(
    """
    Perform keyword-based searches across platforms like Arxiv, Google Scholar, or IEEE on {topic}.
    Extract metadata (title, author, publication date, abstract, keywords) from retrieved papers.
    Rank or filter search results by relevance, publication date, or impact factor if available.
    Display a list of relevant papers with basic information for user selection.
    """
  ),
  expected_output='A comprehensive 3 paragraphs long report .',
  tools=[tool],
  agent=researcher,
)

# Writing task with language model configuration
summarise_task = Task(
  description=(
    '''
    Accept a selected paper (or list of papers) and extract key sections (abstract, methodology, results) on {topic}.
    Summarize the main contributions, objectives, and key findings of each paper.
    Create bullet points or short paragraphs for ease of reading.
    Provide additional options for summarizing specific sections or generating topic overviews from multiple papers.
    '''
  ),
  expected_output= "summarize the research papers briefly and exclusively.",
  tools=[tool],
  agent=summarizer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)

QA_task = Task(
    description=(
    '''
    Parse and understand user questions about selected research papers, such as methodology, results, or concepts on {topic}.
    Retrieve relevant sections from the paper(s) to generate accurate answers.
    Handle follow-up questions related to previous answers or other aspects of the research.
    Support more detailed questions involving images, charts, equations, or other complex data representations.
    '''
    ),
    expected_output= "proper and relevant answers to all the questions. search from internet",
    tools=[tool],
    agent= Question_Answering,
     

)

