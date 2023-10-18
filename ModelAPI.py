from fastapi import FastAPI, HTTPException
from ModelBERT import generate_embedding
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd
import os

app = FastAPI()

# Load the embeddings previously generated
offer_embeddings = np.load('offer_embeddings_sbert.npy')
offer_embeddings = offer_embeddings.reshape(len(offer_embeddings), -1)

# Load offers
offer_df = pd.read_csv(os.path.join("Datasets", "offer_retailer.csv"))
offers = offer_df['OFFER'].tolist()

print("Number of offers:", len(offers))
print("Number of embeddings:", len(offer_embeddings))

def get_top_offers_with_scores(query_embedding):
    # Calculate similarities with the offer embeddings
    similarities = cosine_similarity(query_embedding, offer_embeddings)
    
    # Diagnostic prints
    print("Shape of similarities:", similarities.shape)
    print("Similarities:", similarities)
    
    # Retrieve the indices and scores of the most relevant offers.
    top_indices = similarities[0].argsort()[-5:][::-1]
    
    print("Top indices:", top_indices)
    
    top_scores = similarities[0][top_indices]
    
    # Select and return the most relevant offers along with their scores.
    top_offers_with_scores = [{"Offer": offers[i], "Similarity_score": float(score)} for i, score in zip(top_indices, top_scores)]
    return top_offers_with_scores


@app.get("/search/{query}")
def get_relevant_offers(query: str):
    try:
        # Generate the embedding for the query.
        query_embedding = generate_embedding([query])
        return {"results": get_top_offers_with_scores(query_embedding)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
