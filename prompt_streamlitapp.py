from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Llama Chat", page_icon="🦙")
st.title("🦙 Fawad's Research Assistant")
st.caption("Open-source model served via Hugging Face Inference Providers")


@st.cache_resource
def get_model():
   
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
    )
    return ChatHuggingFace(llm=llm)


model = get_model()

# session_state keeps the chat history alive across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Re-render the full conversation so far
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input box pinned at the bottom of the page
user_input = st.chat_input("Ask Llama something...")

if user_input:
    # Show and store the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get and show the model's reply
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = model.invoke(user_input)
            st.write(result.content)

    st.session_state.messages.append({"role": "assistant", "content": result.content})