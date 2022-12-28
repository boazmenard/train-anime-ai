"""This is an app"""
import streamlit as st
from helpers import generateWorkoutPlan

st.image("https://images.genius.com/4027d128a604c47448e3cca96814020d.300x220x66.gif")
st.title('TrainAnimeAI')
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.write(' ')
# with col2:
#     st.image("https://images.genius.com/4027d128a604c47448e3cca96814020d.300x220x66.gif")
#     st.title('TrainAnimeAI')
# with col3:
#     st.write(' ')

st.write('Train like your favorite anime character. Use the power of anime to achieve fitness immortality.')
anime_character = st.text_input("Enter Your Anime Muse:", placeholder="Sasuke Uchiha")
anime_title = st.text_input("Enter The Anime Title:", placeholder="Naruto")

if st.button("Get Workout Plan"):
    col4, col5 = st.columns(2)
    with col4:
        workout_plan = generateWorkoutPlan(anime_character, anime_title)
        st.header('Training Plan')
        st.write(workout_plan)
    with col5:
        st.header('Cosplay This Character')
