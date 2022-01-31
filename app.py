import streamlit as st
import pickle
import pandas as pd

teams_batting = ['Royal Challengers Bangalore',
 'Mumbai Indians',
 'Sunrisers Hyderabad',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

teams_bowling = ['Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals', 'Sunrisers Hyderabad']

cities = ['Bangalore', 'Hyderabad','Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali']

pipe = pickle.load(open('pipe.pkl' , 'rb'))

st.title('IPL Win Probability Predictor')


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', teams_batting )
with col2:
    bowling_team = st.selectbox('Select the bowling team' , teams_bowling)

selected_city = st.selectbox('Select venue', cities)

target = st.number_input('Target' , max_value = 300)
col3 , col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score' , max_value = 300)

with col4:
    overs = st.number_input('Overs Completed' , max_value = 20)

with col5:
    wickets = st.number_input('wickets', max_value = 10)



if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 -(overs*6)
    wickets = 10 -wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")


image = "https://etimg.etb2bimg.com/photo/60371553.cms"
st.image(image)


