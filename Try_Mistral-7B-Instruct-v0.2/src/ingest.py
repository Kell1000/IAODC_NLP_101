from pathlib import Path
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss

from src.config import configure

DATA_DIR = Path("data/example-1")
INDEX_DIR = "storage"

def build_index():
    configure()

    documents = SimpleDirectoryReader(DATA_DIR).load_data()

    # FAISS vector store
    dimension = 384
    faiss_index = faiss.IndexFlatL2(dimension)
    vector_store = FaissVectorStore(faiss_index=faiss_index)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    index.storage_context.persist(persist_dir=INDEX_DIR)

    print("Index built and saved.")
