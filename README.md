

# 🎧 Music Data Analyst Agent — Azure OpenAI + Streamlit

## 🧠 Overview
This project demonstrates how to build a **GenAI-powered data analytics assistant** using **Azure AI Foundry**, **Code Interpreter Actions**, and **Streamlit**.

The agent is connected to Azure’s GPT-4o deployment and can reason over tabular datasets (e.g., songs, artists, listeners, and records) uploaded to the Code Interpreter sandbox in Azure AI Foundry.  
It is wrapped in a Streamlit web app that provides a chat-style interface for interactive data exploration.

---

## ⚙️ Architecture

**Components:**
1. **Azure AI Foundry Project (`tablesummarizer_genai`)**
   - Hosts the agent (“Music Data Analyst Agent”).
   - Includes Code Interpreter actions and uploaded datasets (`Songs.csv`, `Albums.csv`, `Artists.csv`, `Listeners.csv`, etc.).
   - Handles reasoning, data analysis, and summarization.

2. **Azure GPT-4o Deployment**
   - Serves as the underlying model for the agent.

3. **Streamlit Web App**
   - Provides a front-end interface for chatting with the agent via the Azure Agent Runtime API.

4. **Authentication**
   - Uses Azure CLI (`az login`) for secure authentication with the Azure SDK (via `DefaultAzureCredential`).

---

## 🪜 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
````

### 2️⃣ Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> **If you don’t have a requirements file yet**, create one with:
>
> ```bash
> streamlit
> azure-ai-projects
> azure-identity
> ```

### 4️⃣ Login to Azure

Make sure you’re authenticated locally so `DefaultAzureCredential()` can pick up your session:

```bash
az login
az account show
```

---

## 🧩 Run the App

```bash
streamlit run app_agent.py
```

This will start a local Streamlit server at
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 💬 Usage

Once the web app is open:

1. Type a question such as:

   * “Show top 10 artists by total plays.”
   * “Summarize the distribution of genres.”
   * “Which artist has the highest average listener count?”
2. The app sends your query to the **Azure Agent runtime**, which:

   * Executes Python inside the Code Interpreter.
   * Reads your uploaded CSVs.
   * Returns a summarized, human-readable answer or chart.

---

## 🧠 How It Works

* The Streamlit app calls the **Azure Agent Runtime** (`AIProjectClient`) using the agent ID:

  ```
  asst_5Ph42af2PPvZ6kuhFiuyj0uW
  ```
* The agent runs your question inside its **Code Interpreter sandbox**.
* Results are streamed back to the Streamlit UI.

---

## 🧰 Tech Stack

| Layer          | Technology                                                 |
| -------------- | ---------------------------------------------------------- |
| Frontend       | Streamlit                                                  |
| AI/LLM         | Azure OpenAI (GPT-4o)                                      |
| Orchestration  | Azure AI Foundry Agent Runtime                             |
| Authentication | Azure CLI + DefaultAzureCredential                         |
| Data           | CSVs stored in Azure AI Foundry’s Code Interpreter sandbox |

---

## 🛡️ Security Notes

* **Do not store or commit API keys** — all authentication uses Azure CLI sessions.
* Ensure your Azure account has access to the same subscription as your Foundry project.
* The app does not store any user queries or results by default.

---

## 🧩 Future Improvements

* ✅ Connect live to Fabric Lakehouse SQL endpoint.
* 🔍 Add persistent chat history in Streamlit.
* 📊 Add chart/visualization rendering in the chat UI.
* ☁️ Deploy Streamlit app to Azure App Service or Azure Container Apps.

---

## 🏁 Example Output

**Prompt:**

> "Join Songs.csv and Records.csv to find the top 5 most played artists."

**Agent Response:**

```
Top 5 artists by total play count:
1. Taylor Swift — 42,531 plays
2. Coldplay — 38,904 plays
3. Ed Sheeran — 35,881 plays
4. Billie Eilish — 33,742 plays
5. Drake — 32,004 plays
```

---

## 🧾 License

This project is licensed under the **MIT License** — feel free to use and modify with credit.

```

---

Would you like me to add a `requirements.txt` section at the end of this README (with working pinned versions for Azure AI SDK and Streamlit)? That’s best practice when submitting or sharing this repo.
```
