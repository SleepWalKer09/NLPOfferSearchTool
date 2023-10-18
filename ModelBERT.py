from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import os

# Cargar el modelo SBERT
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def generate_embedding(text):
    """Generate a SBERT embedding for the user text."""
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding

def generate_and_save_embeddings():
    """Generate and save SBERT embeddings for the offers."""
    offer_df = pd.read_csv(os.path.join("Datasets", "offer_retailer.csv"))
    
    # Generate embeddings for each offer
    offers = offer_df['OFFER'].tolist()
    offer_embeddings = [generate_embedding(offer) for offer in offers]
    #offer_embeddings = [np.squeeze(generate_embedding(offer)) for offer in offers]
    print("offers: ",len(offers))
    print("offer_embeddings: ",len(offer_embeddings))
    
    np.save('offer_embeddings_sbert.npy', offer_embeddings)

if __name__ == "__main__":
    generate_and_save_embeddings()
    print("Embeddings generated and saved!")

#offers:  384
#offer_embeddings:  384