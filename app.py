import streamlit as st
import pickle
from PIL import Image

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://www.dolby.com/siteassets/xf-site/blocks/hero/netflix-gradient.png");
background-size: cover;
}
</style>
"""

img = Image.open('netflix-o.png')
theme = {
    "base": "dark",
    "primaryColor": "#e50914",
    "backgroundColor": "#040000",
    "secondaryBackgroundColor": "#2f0909"
}
st.set_page_config(
    page_title='Recommendflix',
    page_icon=img,
    layout="wide"
)

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['Title'].values

st.markdown(page_bg_img, unsafe_allow_html=True)
st.header("Netflix Movies Recommender System")
select_movie = st.selectbox("Select movie", movies_list)

def recommend(movie):
    film_req = movies[movies['Title']==movie].index[0]
    recommendations = sorted(list(enumerate(similarity[film_req])), reverse=True, key=lambda vector: (vector[1], movies.iloc[vector[0]]['Score']))
    recommendations = [(idx, score) for idx, score in recommendations if idx != film_req]
    movie_recommendation = []
    for i in recommendations[0:10]:
        similarity_score = i[1]
        film_index = i[0]
        if similarity_score > 0:
            movie_recommendation.append(movies.iloc[film_index].Title)
    return movie_recommendation

if st.button("Show Recommendation"):
    movie_name = recommend(select_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
