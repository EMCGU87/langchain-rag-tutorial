import os
from typing import Dict, List
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Must match your Chroma_ingestion.ipynb
CHROMA_PATH = "chroma_fresh"

# Reuse the same embedding model as ingestion
embedding_function = OpenAIEmbeddings(
    api_key=os.environ.get("OPENAI_API_KEY"),
    model="text-embedding-3-small",
)

# Open the persisted vector store
db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_function,
)

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def rag_query(question: str, similarity_threshold: float = 0.5) -> Dict:
    results = db.similarity_search_with_relevance_scores(question, k=3)
    if not results or results[0][1] < similarity_threshold:
        return {"response": None, "sources": [], "found": False}

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(
        context=context_text, question=question
    )

    llm = ChatOpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        model="gpt-4o-mini",
    )
    ai_msg = llm.invoke(prompt)
    response_text = getattr(ai_msg, "content", str(ai_msg))

    sources: List[str] = [doc.metadata.get("source") for doc, _ in results]
    return {"response": response_text, "sources": sources, "found": True}