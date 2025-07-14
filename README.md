# AI MediBot: Medical QA Chatbot

AI MediBot is an open-source, retrieval-augmented chatbot designed to answer medical questions using credible, domain-specific documents. Built with Python, LangChain, Hugging Face, FAISS, and Streamlit, it allows users to interactively query a knowledge base constructed from trusted medical PDFs. The bot only answers using the provided knowledge base, ensuring reliability and transparency.

## Features

- **Retrieval-Augmented Generation (RAG):** Combines semantic search with a large language model (LLM) for grounded, context-aware answers.
- **Custom Knowledge Base:** Easily ingest medical textbooks, guidelines, or any PDF documents.
- **Open-Source & Local:** Runs fully on your machine with no proprietary API lock-in.
- **Streamlit UI:** Simple chat interface for real-time interaction.
- **Credible Answers Only:** The bot refuses to answer if the information is not found in the supplied documents.

## Architecture Overview

1. **Data Ingestion:** Load and extract text from PDF files using `PyPDFLoader` and `DirectoryLoader`.
2. **Text Chunking:** Split large documents into overlapping chunks for context preservation using `RecursiveCharacterTextSplitter`.
3. **Embeddings:** Convert text chunks into semantic vectors with `sentence-transformers/all-MiniLM-L6-v2`.
4. **Vector Storage:** Store embeddings in a FAISS vector database for fast similarity search.
5. **LLM Integration:** Use a Hugging Face-hosted LLM (e.g., Mistral-7B-Instruct) to generate answers based on retrieved context.
6. **Streamlit UI:** Provide an interactive frontend for users to ask questions and receive answers with source references.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-medibot.git
cd ai-medibot
```

### 2. Environment Setup

- **Python 3.9+** recommended.
- Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Hugging Face API Token

- Sign up at [Hugging Face](https://huggingface.co/).
- Create a new access token with "read" permissions.
- Add your token to a `.env` file in the project root:

```
HF_TOKEN="your_huggingface_token"
```

### 4. Prepare Your Data

- Place your medical PDF files in the `data/` directory.

### 5. Build the Vector Store

Run the following script to process PDFs, split text, create embeddings, and build the FAISS vector store:

```bash
python Memory_For-LLM.py
```

### 6. Start the Chatbot

To launch the Streamlit interface:

```bash
streamlit run Bot.py
```

Or, for command-line interaction:

```bash
python Memory_to_LLM.py
```

## Usage

- Open the Streamlit app in your browser.
- Enter your medical question in the chat box.
- The bot will respond with an answer based strictly on the ingested documents and display the relevant source excerpts.

## Project Structure

| File/Folder           | Description                                      |
|-----------------------|--------------------------------------------------|
| `Bot.py`              | Streamlit-based chat UI for the bot              |
| `Memory_to_LLM.py`    | Command-line QA interface                        |
| `Memory_For-LLM.py`   | Script to ingest PDF data and build vector store |
| `data/`               | Directory for your PDF documents                 |
| `vectorstore/`        | Stores the FAISS vector database                 |
| `.env`                | Environment variables (e.g., Hugging Face token) |
| `requirements.txt`    | Python dependencies                              |

## Key Technologies

- **LangChain:** Framework for building LLM-powered apps.
- **Hugging Face Transformers:** Access to open-source LLMs and embedding models.
- **FAISS:** Fast vector similarity search for document retrieval.
- **Streamlit:** Rapid web app development for Python.

## Customization

- **Add More PDFs:** Place additional medical PDFs in `data/` and rerun `Memory_For-LLM.py`.
- **Change LLM:** Edit the `HUGGINGFACE_REPO_ID` in the scripts to use a different Hugging Face model.
- **Prompt Engineering:** Modify `CUSTOM_PROMPT_TEMPLATE` for different answer styles or constraints.

## Example Workflow

1. User uploads medical PDFs.
2. Run `Memory_For-LLM.py` to index the knowledge base.
3. Start the chatbot with Streamlit.
4. Ask: *"What are the symptoms of diabetes?"*
5. The bot retrieves the most relevant excerpts and generates an answer, citing the source.

## Limitations

- **Not a substitute for professional medical advice.**
- Answers are limited to the content of the ingested documents.
- Requires sufficient GPU/CPU for embedding and LLM inference.

## License

This project is open-source and free to use for educational and non-commercial purposes.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Hugging Face](https://huggingface.co/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
