from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
# I'll try
# hf download TheBloke/Mistral-7B-Instruct-v0.2-GGUF mistral-7b-instruct-v0.2.Q4_K_M.gguf --local-dir models

LLM_PATH = "models/mistral.gguf"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def configure():
    llm = LlamaCPP(
        model_path=LLM_PATH,
        temperature=0.1,
        max_new_tokens=512,
        context_window=4096,
        model_kwargs={
            "n_threads": 6,
        },
    )

    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)

    Settings.llm = llm
    Settings.embed_model = embed_model
