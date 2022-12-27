"""This is an app"""
import streamlit as st
from helpers import generateWorkoutPlan

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.title('TrainAnimeAI')
    # st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.write(' ')

#st.title('TrainAnimeAI')

anime_character = st.text_input("Enter Your Anime Muse:", placeholder="Sasuke Uchiha")
anime_title = st.text_input("Enter The Anime Title:", placeholder="Naruto")

if st.button("Get Workout Plan"):
    workout_plan = generateWorkoutPlan(anime_character, anime_title)
    st.write(workout_plan)
