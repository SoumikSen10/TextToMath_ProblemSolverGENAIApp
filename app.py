import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#from langchain.chains import LLMChain, LLMMathChain
from langchain_community.utilities import WikipediaAPIWrapper

from langchain_core.runnables import RunnableLambda
#from langchain.agents import initialize_agent, AgentType, Tool
#from langchain.callbacks import StreamlitCallbackHandler

# --------------------------------------------------
# Streamlit Setup
# --------------------------------------------------
st.set_page_config(
    page_title="Text to Math Problem Solver and Data Search Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Text to Math Problem Solver using Meta AI's LLaMA")

# --------------------------------------------------
# API Key Input
# --------------------------------------------------
groq_api_key = st.sidebar.text_input("Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API Key to continue")
    st.stop()

# --------------------------------------------------
# LLM
# --------------------------------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# --------------------------------------------------
# Wikipedia Tool (Runnable)
# --------------------------------------------------
wiki = WikipediaAPIWrapper()

wikipedia_tool = RunnableLambda(
    lambda q: wiki.run(q)
)

# --------------------------------------------------
# Math Tool (LLM-based, no LLMMathChain)
# --------------------------------------------------
math_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
Solve the following math problem step by step and return only the final answer.

Question:
{question}

Answer:
"""
)

math_chain = math_prompt | llm | StrOutputParser()

# --------------------------------------------------
# Reasoning Tool (LLMChain)
# --------------------------------------------------
reasoning_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are an expert reasoning assistant.

Solve the user's question step by step and provide a clear,
point-wise explanation.

Question:
{question}

Answer:
"""
)

reasoning_chain = reasoning_prompt | llm | StrOutputParser()

# --------------------------------------------------
# Simple Router Logic (Agent Replacement)
# --------------------------------------------------
def route_question(question: str) -> str:
    question_lower = question.lower()

    if any(word in question_lower for word in ["calculate", "+", "-", "*", "/", "how many", "total"]):
        return math_chain.invoke({"question": question})

    if any(word in question_lower for word in ["who", "what", "when", "where", "wikipedia"]):
        return wikipedia_tool.invoke(question)

    return reasoning_chain.invoke({"question": question})

# --------------------------------------------------
# Chat History
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm a math and reasoning assistant. Ask me anything 😊"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# --------------------------------------------------
# User Input
# --------------------------------------------------
question = st.text_area(
    "Enter your question:",
    "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. "
    "Then I buy a dozen apples and 2 packs of blueberries. "
    "Each pack contains 25 blueberries. "
    "How many total pieces of fruit do I have?"
)

# --------------------------------------------------
# Generate Response
# --------------------------------------------------
if st.button("Find my answer"):
    if question.strip():

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.chat_message("user").write(question)

        with st.spinner("Thinking..."):
            response = route_question(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.chat_message("assistant").write(response)
     
    else : 
        st.warning("Please enter a question")