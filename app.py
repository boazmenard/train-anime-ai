"""This is an app"""
import streamlit as st
from helpers import generateWorkoutPlan

st.image("https://images.genius.com/4027d128a604c47448e3cca96814020d.300x220x66.gif")
st.title('🏋️ TrainAnimeAI')
with st.expander("Exercise Disclaimer -- PLEASE READ"):
    st.write("""
The exercises provided here are for educational and entertainment purposes only, and is not to be interpreted as a recommendation for a specific treatment plan, product, or course of action. Exercise is not without its risks, and this or any other exercise program may result in injury. They include but are not limited to: risk of injury, aggravation of a pre-existing condition, or adverse effect of over-exertion such as muscle strain, abnormal blood pressure, fainting, disorders of heartbeat, and very rare instances of heart attack. To reduce the risk of injury, before beginning this or any exercise program, please consult a healthcare provider for appropriate exercise prescription and safety precautions. The exercise instruction and advice presented are in no way intended as a substitute for medical consultation. I disclaim any liability from and in connection with this program. As with any exercise program, if at any point during your workout you begin to feel faint, dizzy, or have physical discomfort, you should stop immediately and consult a physician.
""")

with st.expander("How it works 👇"):
    st.write("1. Input the anime character and what anime they're from. Don't leave either blank.")
    st.write("2. Watch the magic.")
    st.write("We use GPT-3 to take the anime character and title to construct a prompt to get you the workout and diet plan. It's a quick and dirty build so look past any faults/errors, just shoot me a message!")
    

with st.sidebar:
    st.header("About this app")
    st.write("Just to reiterate, this app is NOT health or medical advice. Please consult your physician before taking part in any exercise.")
    st.write("If you love anime & fitness (also cosplay), sometimes you dream about working out like your favorite character(s), this quick little app helps you do just that.")
    st.header("Built With:")
    st.markdown("""
    * [Streamlit](https://streamlit.io)
    * [OpenAI](https://openai.com)
    """)
    st.header("Support")
    st.markdown("""
    If you thought this was cool/fun, support me here
    * Follow me on [twitter](https://twitter.com/bomenardco)
    * [Buy me a coffee](https://www.buymeacoffee.com/bomenardco)
    """)

st.write('Train like your favorite anime character. Use the power of anime to achieve fitness immortality.')
anime_character = st.text_input("Enter Your Anime Muse:", placeholder="Sasuke Uchiha")
anime_title = st.text_input("Enter The Anime Title:", placeholder="Naruto")

if st.button("Get Workout Plan"):
    workout_plan = generateWorkoutPlan(anime_character, anime_title)
    st.header('Training Plan')
    st.write(workout_plan)
