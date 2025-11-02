import streamlit as st
from openai import AzureOpenAI

# -----------------------------
# 🔑 Azure OpenAI Configuration
# -----------------------------
AZURE_ENDPOINT = "Your Azure Endpoint"
API_KEY = "Your API Key"
DEPLOYMENT_NAME = "gpt-4o"
API_VERSION = "2025-01-01-preview"

# Initialize client
client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION
)

# -----------------------------
# 🎵 Streamlit UI
# -----------------------------
st.set_page_config(page_title="Music Data Analyst Agent", page_icon="🎧")

st.title("🎧 Music Data Analyst Agent")
st.write("Ask questions about your music data (Songs, Albums, Artists, Records, Listeners, and Users).")

# User input box
user_query = st.text_area("Enter your question:", placeholder="e.g., Which artist has the most albums?")

# When user clicks 'Ask'
if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Analyzing your question..."):
            try:
                response = client.chat.completions.create(
                    model=DEPLOYMENT_NAME,
                    messages=[
                        {"role": "system", "content": "You are a Music Data Analytics Assistant. You help analyze data from Songs.csv, Albums.csv, Artists.csv, Records.csv, Listeners.csv, and Users.csv."},
                        {"role": "user", "content": user_query}
                    ]
                )

                answer = response.choices[0].message.content
                st.success("✅ Response:")
                st.write(answer)

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("Please type a question before clicking Ask.")
