from wordcloud import WordCloud
import streamlit as st
import pandas as pd
import requests
import os
import matplotlib.pyplot as plt



API_ENDPOINT = "http://localhost:8000/search"

brands_df = pd.read_csv(os.path.join("Datasets", "brand_category.csv"))
categories_df = pd.read_csv(os.path.join("Datasets", "categories.csv"))
offers_df = pd.read_csv(os.path.join("Datasets", "offer_retailer.csv"))

unique_brands = brands_df['BRAND'].unique().tolist()
unique_categories = categories_df['PRODUCT_CATEGORY'].unique().tolist()
unique_retailers = offers_df['RETAILER'].unique().tolist()

# Group by the category, sum the RECEIPTS, and get the top 6 categories
top_categories = brands_df.groupby("BRAND_BELONGS_TO_CATEGORY")["RECEIPTS"].sum().nlargest(5)


st.title("Offer Searcher 🏷️💲")
st.write("---")  # Line separator
st.subheader("Discover relevant offers based on your input! 🕵️‍♂️🛍️")
st.write("You can search by product, category, brand, or retailer.")
user_input = st.text_input("📣 Enter your search:", placeholder="e.g. Amazon, Coffee, SUBWAY")

if st.button("Search"):
    # Build the parameters for the API based on user selections
    response = requests.get(f"{API_ENDPOINT}/{user_input}")
    if response.status_code == 200:
        data = response.json()
        if "results" in data:
            results = data["results"]
            if results:
                results_df = pd.DataFrame(results)
                st.table(results_df)
            else:
                st.warning("No results found for the given input.")
        else:
            st.error(f"Unexpected response format: {data}")
    else:
        st.error(f"Error in the request: {response.status_code} - {response.text}")




st.subheader("Top 5 Categories by Receipts")
st.write("Below are the categories with the highest number of receipts, providing insights into the most popular shopping preferences among users.")
fig, ax = plt.subplots(figsize=(10, 5))
top_categories.plot(kind='barh', ax=ax, color='green')
ax.set_xlabel('Number of Receipts')
ax.set_ylabel("Category")
ax.invert_yaxis()  # To display the category with the highest receipts at the top
st.pyplot(fig)

st.subheader("Categories Word Cloud")
st.write("Explore the word cloud to gauge the prominence of different product categories. The size of each word corresponds to its frequency or popularity in the dataset.")
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(categories_df['PRODUCT_CATEGORY']))
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt.gcf())