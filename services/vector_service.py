from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Charger la base vectorielle persistée
def get_vector_context(query):
    db = Chroma(persist_directory="chroma_db", embedding_function=OpenAIEmbeddings())
    retriever = db.as_retriever()
    docs = retriever.get_relevant_documents(query)
    # Concatène le contenu des documents trouvés
    context = "\n".join([doc.page_content for doc in docs])
    return context