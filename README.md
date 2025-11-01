# RAG Tutorial with FastAPI & LangChain

A complete Retrieval-Augmented Generation (RAG) pipeline that creates a searchable vector database from documents and exposes it via a REST API, ready for integration with Custom GPTs.

## Features

✅ **Document Ingestion**: Load markdown documents and chunk them for semantic search  
✅ **Vector Storage**: Persist embeddings in Chroma DB for fast retrieval  
✅ **REST API**: FastAPI endpoint to query your knowledge base  
✅ **Custom GPT Ready**: Expose via ngrok for OpenAI GPT Actions integration  
✅ **Interactive Notebooks**: Easy development and testing with Jupyter

---

## Quick Start

**For detailed setup instructions, see [SETUP.md](SETUP.md)**

1. **Clone and install**:
   ```bash
   pip install -r requirements.txt
   pip install "unstructured[md]"
   ```

2. **Configure environment**:
   - Copy `env.example` to `.env`
   - Add your OpenAI API key

3. **Ingest data**:
   ```bash
   jupyter notebook Chroma_ingestion.ipynb  # Run all cells
   ```

4. **Run the API**:
   ```bash
   uvicorn rag_api:app --reload
   ```

5. **Test**: Open http://127.0.0.1:8000/docs

---

## Project Structure

- **`rag_api.py`** - FastAPI server with `/query` endpoint  
- **`rag_service.py`** - Core RAG pipeline (retrieve + generate)  
- **`Chroma_ingestion.ipynb`** - Data ingestion notebook  
- **`Query_data_2.ipynb`** - Query testing notebook  
- **`data/books/`** - Your markdown documents  
- **`chroma_fresh/`** - Generated vector database

---

## Integrate with Custom GPT

1. Start ngrok: `ngrok http 8000`
2. Copy the HTTPS URL
3. Add as an Action in your Custom GPT (see OpenAI documentation)

---

## Tutorial Video

Original tutorial: [RAG+Langchain Python Project: Easy AI/Chat For Your Docs](https://www.youtube.com/watch?v=tcqEUSNCn8I)

---

## Requirements

- Python 3.10+
- OpenAI API key
- Windows: Microsoft C++ Build Tools
- macOS: `conda install onnxruntime -c conda-forge`
