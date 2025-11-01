# Setup Instructions

## Quick Start Guide

Follow these steps to get your RAG API running on any machine.

---

## Step 1: Prerequisites

### Windows Users
Before installing dependencies, install **Microsoft Visual C++ Build Tools**:
1. Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Install with "Desktop development with C++" workload
3. Restart your computer

### macOS Users
Install `onnxruntime` separately:
```bash
conda install onnxruntime -c conda-forge
```

---

## Step 2: Clone and Setup

1. **Clone this repository** (or download the ZIP):
   ```bash
   cd langchain-rag-tutorial
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```
   
3. **Activate the virtual environment**:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install "unstructured[md]"
   ```

---

## Step 3: Configure Environment

1. **Copy the environment template**:
   ```bash
   copy env.example .env
   ```
   (Mac/Linux: `cp env.example .env`)

2. **Edit `.env`** and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```
   Get your key from: https://platform.openai.com/api-keys

---

## Step 4: Ingest Data into Vector Store

1. **Open the Jupyter notebook**:
   ```bash
   jupyter notebook Chroma_ingestion.ipynb
   ```

2. **Run all cells** in the notebook (Cell → Run All)
   - This loads your markdown files from `data/books/`
   - Splits them into chunks
   - Creates a Chroma vector database in `chroma_fresh/`

3. **Verify success**: You should see "Saved 217 chunks to chroma_fresh."

---

## Step 5: Run the API

1. **Start the FastAPI server**:
   ```bash
   uvicorn rag_api:app --reload
   ```

2. **Test the API**:
   - Open browser: http://127.0.0.1:8000/docs
   - Click "POST /query"
   - Try it out with: `{"question": "Did Alice fall through the earth?"}`

---

## Step 6: (Optional) Expose with Ngrok for Custom GPT

1. **Install ngrok**: https://ngrok.com/download

2. **Start ngrok** in a new terminal:
   ```bash
   ngrok http 8000
   ```

3. **Copy the HTTPS URL** (e.g., `https://abc123.ngrok-free.app`)

4. **Use this URL** when configuring your Custom GPT Actions (see OpenAI GPTs documentation)

---

## Troubleshooting

### "Module not found" errors
- Make sure you activated your virtual environment
- Reinstall: `pip install -r requirements.txt`

### Chroma database issues
- Delete `chroma_fresh/` folder
- Re-run `Chroma_ingestion.ipynb`

### API won't start
- Check if port 8000 is already in use
- Restart your terminal/kernel

### OpenAI API errors
- Verify your API key in `.env` is correct
- Check you have credits on your OpenAI account

---

## Project Structure

```
langchain-rag-tutorial/
├── data/
│   └── books/              # Your markdown files go here
├── chroma_fresh/           # Generated vector DB (gitignored)
├── rag_api.py              # FastAPI server
├── rag_service.py          # RAG query logic
├── Chroma_ingestion.ipynb  # Data ingestion notebook
├── Query_data_2.ipynb      # Notebook for testing queries
├── requirements.txt        # Python dependencies
├── env.example            # Environment variable template
└── SETUP.md               # This file
```

---

## Next Steps

- Add more documents to `data/books/`
- Customize the prompt in `rag_service.py`
- Deploy to a cloud server (Render, Heroku, etc.)
- Integrate with your Custom GPT using the ngrok URL

