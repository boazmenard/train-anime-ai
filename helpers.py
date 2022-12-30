"""All the helpers for the app."""
import os
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generateWorkoutPlan(anime_character, anime_title):
    if not bool(anime_character.strip()) or not bool(anime_title.strip()):
        return "Please enter the anime character AND where they're from and try again 👍"

    prompt = f'''
    Give me a weekly workout and diet plan that will give me the body of the anime character below. I want the exercises, sets, and reps and breakfast, lunch, dinner, and snacks. I do not want to workout longer than 1 hour each day that I workout.
    Anime Character: {anime_character} from the anime {anime_title}/n
    '''
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=650
    )
    return response.choices[0].text
