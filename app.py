import streamlit as st
import pandas as pd
import pickle
import numpy as np

movie_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_list)
similarity = pickle.load(open('similarity_matrix.pkl','rb'))


def recommend(movie_name):
    l=[]
    movie_index = movies[movies['title'] == movie_name].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])),reverse=True , key=lambda x:x[1])[1:6]
    for i in movies_list:
        l.append(movies.iloc[i[0]].title)
    return l






st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Enter the movie name',movies['title'].values)
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)







