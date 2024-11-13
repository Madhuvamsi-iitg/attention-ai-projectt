# app.py
import streamlit as st
from crew import crew  # Importing the configured crew

# Streamlit app UI
st.title("AI Research Assistant")
st.write("This app helps retrieve, summarize, and answer questions about research papers.")

# Input for the research topic
topic = st.text_input("Enter a research topic:", "AI in healthcare")

# Run the process and display results
if st.button("Run Research"):
    st.write(f"Researching topic: {topic}...")
    try:
        # Trigger the process directly as in crew.py
        result = crew.kickoff(inputs={'topic': topic})
        st.write("Results:")
        st.write(result)
    except AttributeError as e:
        st.error(f"Attribute error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
