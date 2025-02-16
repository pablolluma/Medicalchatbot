from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load the Pinecone API key from the .env file
load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Load the extracted data from the PDF file
extracted_data=load_pdf_file(data='Data/')
text_chunks=text_split(extracted_data)

# Download the Hugging Face embeddings
embeddings = download_hugging_face_embeddings()

# Create a Pinecone index with the specified name, dimension, metric, and spec.
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalchatbot"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

# before lauching the app we need to execute this file first.