import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=4fcf7af3bbcf1cdb4598066485a155dd".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path  


def recommend(movie):
    index = new_data[new_data['original_title'] == movie].index[0]
    distances = similarity[index]
    rec_mov_names = []
    rec_mov_post = []
    most_similar_movies = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    for i in most_similar_movies:
        movie_id = new_data.iloc[i[0]].id
        rec_mov_names.append(new_data.iloc[i[0]].original_title)
        rec_mov_post.append(fetch_poster(movie_id))
    print(rec_mov_post)
    return rec_mov_names , rec_mov_post

new_data = pickle.load(open('final-movie.pkl','rb'))
similarity = pickle.load(open('final-similarity.pkl','rb'))

st.header('Movie Recommender')

movie_list = new_data['original_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names , recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
