from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# Charge la clé OpenAI depuis le fichier API_KEY
with open("API_KEY", "r") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()

# 1. Charger un document local
loader = TextLoader("data/context.txt", encoding="utf-8")
documents = loader.load()

# 2. Split en petits chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# 3. Convertir en vecteurs et indexer dans Chroma
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings, persist_directory="chroma_db")

# 4. Créer la chaîne RAG
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    retriever=retriever,
    return_source_documents=True
)

# 5. Poser une question de test
query = "Explique-moi le sujet du document."
result = qa_chain({"query": query})

print("\nRéponse:")
print(result["result"])

print("\nSources:")
for doc in result["source_documents"]:
    print(doc.metadata)