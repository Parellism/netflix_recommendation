import streamlit as st
import pickle
from PIL import Image, ImageOps

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://www.dolby.com/siteassets/xf-site/blocks/hero/netflix-gradient.png");
background-size: cover;
}
</style>
"""

img = Image.open('netflix-o.png')
st.set_page_config(
    page_title='Recommendflix',
    page_icon=img,
    layout="wide"
)

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['Title'].values

st.markdown(page_bg_img, unsafe_allow_html=True)
st.header(":red[NETFLIX] Movies Recommender System")

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

def resize_with_padding(image_path, desired_size=(300, 450)):
    image = Image.open(image_path)
    image = ImageOps.fit(image, desired_size, Image.LANCZOS, centering=(0.5, 0.5))
    return image

if st.button("Show Recommendation"):
    movie_name = recommend(select_movie)
    cols = st.columns(5)
    for i in range(min(len(movie_name), len(cols))):
    with cols[i]:
        st.text(movie_name[i])
        sanitized_movie_name = movie_name[i].replace(":", "").replace("?", "")
        poster_path = f"poster/{sanitized_movie_name}.jpg"
        poster = resize_with_padding(poster_path)
        st.image(poster, use_column_width=True)


    
#    col1,col2,col3,col4,col5 = st.columns(5)
#    with col1:
#        st.text(movie_name[0])
#        sanitized_movie_name = movie_name[0].replace(":", "").replace("?", "")
#        poster_path = f"poster/{sanitized_movie_name}.jpg"
#        poster = resize_with_padding(poster_path)
#        st.image(poster, use_column_width=True)
        #st.image(f"poster/{movie_name[0]}.jpg", use_column_width=True)
#    with col2:
#        st.text(movie_name[1])
#        sanitized_movie_name = movie_name[1].replace(":", "").replace("?", "")
#        poster_path = f"poster/{sanitized_movie_name}.jpg"
#        poster = resize_with_padding(poster_path)
#        st.image(poster, use_column_width=True)
       #st.image(f"poster/{movie_name[0]}.jpg", use_column_width=True)
#    with col3:
#        st.text(movie_name[2])
#        sanitized_movie_name = movie_name[2].replace(":", "").replace("?", "")
#        poster_path = f"poster/{sanitized_movie_name}.jpg"
#        poster = resize_with_padding(poster_path)
#        st.image(poster, use_column_width=True)
#        #st.image(f"poster/{movie_name[0]}.jpg", use_column_width=True)
#    with col4:
#        st.text(movie_name[3])
#        sanitized_movie_name = movie_name[3].replace(":", "").replace("?", "")
#        poster_path = f"poster/{sanitized_movie_name}.jpg"
#        poster = resize_with_padding(poster_path)
#        st.image(poster, use_column_width=True)
        #st.image(f"poster/{movie_name[0]}.jpg", use_column_width=True)
#    with col5:
#        st.text(movie_name[4])
#        sanitized_movie_name = movie_name[4].replace(":", "").replace("?", "")
#        poster_path = f"poster/{sanitized_movie_name}.jpg"
#        poster = resize_with_padding(poster_path)
#        st.image(poster, use_column_width=True)
        #st.image(f"poster/{movie_name[0]}.jpg", use_column_width=True)
