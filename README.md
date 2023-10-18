# NLPOfferSearchTool

## Overview
The Offer Searcher is a comprehensive tool designed to efficiently fetch and display relevant retail offers based on user input. By leveraging the power of Natural Language Processing (NLP), specifically the Sentence-BERT model, the system can semantically understand and match offers even when the user's query doesn't match the offer text exactly.

## Features
**Semantic Search**:  Allows users to search for offers using natural language queries. Whether you're looking for a specific product, brand, category, or retailer, the tool intelligently fetches the most relevant offers.

**Interactive UI**: Built with Streamlit, the user interface provides a dynamic way to input search criteria and instantly view the results in a tabulated format. Additionally, it displays insightful visualizations about the top categories and their distribution.

**Scalable Backend**: The FastAPI backend ensures rapid response times and can be easily scaled to handle a larger volume of requests. It interfaces with the Sentence-BERT model to generate embeddings and compute semantic similarities.

**Data Driven**: Utilizes datasets containing information about brands, categories, and offers to provide a wide range of results tailored to the user's needs.

## Use Cases
Retail companies can use this tool to guide their customers to the most relevant promotional offers.
Market researchers can quickly find offers related to specific categories or brands.
Regular users can explore and find the best deals based on their preferences.


## Streamlit UI
With the search for "soup" offers

<p align="center">
  <img src="https://github.com/SleepWalKer09/NLPOfferSearchTool/assets/44912298/d02dfd30-90df-44fa-8c25-5f43e8ad3091">
</p>
