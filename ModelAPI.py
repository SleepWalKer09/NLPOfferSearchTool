from fastapi import FastAPI, HTTPException
from ModelBERT import generate_embedding
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd
import os

app = FastAPI()

# Cargar los embeddings previamente generados
offer_embeddings = np.load('offer_embeddings_sbert.npy')
offer_embeddings = offer_embeddings.reshape(len(offer_embeddings), -1)


# Cargar las ofertas
offer_df = pd.read_csv(os.path.join("Datasets", "offer_retailer.csv"))
offers = offer_df['OFFER'].tolist()

print("Number of offers:", len(offers))
print("Number of embeddings:", len(offer_embeddings))

def get_top_offers_with_scores(query_embedding):
    # Calcular las similitudes con los embeddings de las ofertas
    similarities = cosine_similarity(query_embedding, offer_embeddings)
    
    # Impresiones de diagnóstico
    print("Shape of similarities:", similarities.shape)
    print("Similarities:", similarities)
    
    # Obtener los índices y scores de las ofertas más relevantes
    top_indices = similarities[0].argsort()[-5:][::-1]
    
    # Más impresiones de diagnóstico
    print("Top indices:", top_indices)
    
    top_scores = similarities[0][top_indices]
    
    # Seleccionar y devolver las ofertas más relevantes junto con sus scores
    top_offers_with_scores = [{"Offer": offers[i], "Similarity_score": float(score)} for i, score in zip(top_indices, top_scores)]
    return top_offers_with_scores


@app.get("/search/{query}")
def get_relevant_offers(query: str):
    try:
        # Generar el embedding para la consulta
        query_embedding = generate_embedding([query])
        return {"results": get_top_offers_with_scores(query_embedding)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
