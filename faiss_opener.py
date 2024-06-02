from langchain.vectorstores import FAISS
import faiss

vectorstore = faiss.load_faiss_index("index.faiss")
print(vectorstore)