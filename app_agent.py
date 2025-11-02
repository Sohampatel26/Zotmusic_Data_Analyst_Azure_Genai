import streamlit as st
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder
import time

# ---------------------------------
# ⚙️ Azure Agent Configuration
# ---------------------------------
AZURE_ENDPOINT = "Your endpoint"
AGENT_ID = "your agent ID"

# Initialize the Azure Project client
project = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=AZURE_ENDPOINT
)

# ---------------------------------
# 🎨 Streamlit UI
# ---------------------------------
st.set_page_config(page_title="🎧 Music Data Analyst Agent", page_icon="🎶")
st.title("🎧 Music Data Analyst Agent")
st.write("Ask questions about your Fabric music data (Songs, Albums, Artists, Listeners, etc.).")

# Input box
user_query = st.text_area("Enter your question:", placeholder="e.g., What are the top 5 genres by play count?")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Running your query through Azure Agent..."):
            try:
                # Create a new conversation thread
                thread = project.agents.threads.create()

                # Post user's message
                project.agents.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content=user_query
                )

                # Start and process the run
                run = project.agents.runs.create_and_process(
                    thread_id=thread.id,
                    agent_id=AGENT_ID
                )

                # Wait for the run to complete (since some take time)
                while run.status not in ["completed", "failed"]:
                    time.sleep(2)
                    run = project.agents.runs.get(thread_id=thread.id, run_id=run.id)

                # Display output
                if run.status == "failed":
                    st.error(f"Run failed: {run.last_error}")
                else:
                    messages = project.agents.messages.list(
                        thread_id=thread.id,
                        order=ListSortOrder.ASCENDING
                    )
                    for message in messages:
                        if message.text_messages:
                            role = "🧠 Agent" if message.role == "assistant" else "👤 You"
                            st.markdown(f"**{role}:** {message.text_messages[-1].text.value}")

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("Please enter a question before clicking Ask.")
