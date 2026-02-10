from llama_index.core import StorageContext, load_index_from_storage
from src.config import configure

INDEX_DIR = "storage"

def ask(question: str):
    configure()

    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    return response
