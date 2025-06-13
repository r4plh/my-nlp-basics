from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model = "sentence_transformers/all-MiniLM-L6-v2")

text = "India is a country"

vector = embedding.embed_query(text)

