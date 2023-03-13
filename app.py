import streamlit as st
from PIL import Image




st.title(' _Welcome to my Projects Portfolio_ ')

with st.sidebar:
    image = Image.open("C:/Users/A.M. MUKTAR/my_portfolio/Images/IMG-20220413-WA0005.jpg")
    st.image(image)
    st.subheader("Interest")
    st.markdown("""
        - Football
        - Reading 
        - Cycling
    """)



col1, col2 = st.columns(2)
with col1:
    st.write("Name: Abubakar Muhammed Muktar")
    st.write("Status: Masters Student, Data Science & Analytics")
    st.write("School: EPITA")
with col2:    
    st.write("Strength: Serial learning, knowing I can always improve.")
    st.write("Favourite Quote: In God we trust, Everyone else bring data!")
st.header("Data Science and Engineering Project  Section")
with st.expander("PROJECT 1:  Fairly Used Car Prediction Platform"):
    st.subheader('Fairly Used Car Prediction Platform')
    st.write("This project is ...")
    st.markdown("""
    - Created a price estimation model for fairly used car using Linear Regression
    - Developed a web platform Using Streamlit and deployed the model as a service\n
    - Platform can predict take direct input from a user or take a csv file and run predictions on them\n
    - Used postgres to save user predictions and user can query past prediction from the database\n
    - Airflow to schedule data ingestion and prediction jobs\n
    - Used Grafana to monitor model and MLFlow for retraining.
    """)

    st.markdown("[Project CODE](https://github.com/sadiksmart0/Used-Car-ML)")
    video_file = open('C:/Users/A.M. MUKTAR/my_portfolio/videos/Fairly-used.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

with st.expander("PROJECT 2: Music Emotion Recognition and Recommendatation."):
    st.subheader('Music Emotion Recognition and Recommendatation')
    st.write("This project is ...")
    st.markdown("""
    - Collaborated and developed a state-of-the-art deep learning model using BERT and gensims Doc2Vec for recognizing song emotion and give recommendations based on that given lyrics, song title and artist name.
    - Deployed the model on Heroku and serve the it using FastApi.
    - Develop and deployed the app on streamlit.
    - Presented the work as part of our masters thesis.
    """)

    st.markdown("[Project CODE](https://github.com/anthonybassaf/music-mood-recognition)")
    video_file = open('C:/Users/A.M. MUKTAR/my_portfolio/videos/music-mood.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

with st.expander("PROJECT 3: Brain Tumor Segmentation"):
    st.subheader('Brain Tumor Segmentation')
    st.write("This project is ...")
    st.markdown("""
    - Created a deep learning model based on the U-net architecture to segment brain tumor images.
    - Used tensorflow in the implementation.
    - Engineered the data into desired format.
    - Evaluated model performance based on Dice loss
    """)

    st.markdown("[Project CODE](https://github.com/sadiksmart0/Image-seg)")
    video_file = open('C:/Users/A.M. MUKTAR/my_portfolio/videos/Fairly-used.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


with st.expander("PROJECT 4: Movie Recommendatation system."):
    st.subheader('Movie Recommendatation system.')
    st.write("This project is ...")
    st.markdown("""
    - Implemented a movie recommendation system for using the cosine similarity, users and movie rating.
    - Scrape the web for movie posters and details using BeautifulSoup
    - Built a streamlit app for the recommendation plaform
    - Employed TF-IDF for tokenization.
    """)
     
    st.markdown("[Project CODE](https://github.com/sadiksmart0/Movie-Recommender)")
    video_file = open('C:/Users/A.M. MUKTAR/my_portfolio/videos/movie-recommender.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

with st.expander("PROJECT 5: End-to-End Data Engineering Project using Kaggle YouTube Trending Dataset"):
    st.subheader('Movie Recommendatation system.')
    st.write("This project intends to manage, simplify, and analyze structured and semi-structured YouTube video data based on video categories and trending metrics in a secure manner.")
    st.markdown("""
    - Implement the data pipeline completely using AWS cloud.
    - Data Lake to hold raw ingested data using Amazon S3
    - Used AWS Lambda to preprocess the data to a parquet.
    - Data Warehouse to hold cleansed data in Amazon S3
    - Catalogue the data using AWS Glue.
    - Used Athena to query the data.
    - Used IAM to create rule and policies to allow access accross these tools
    - Used QuickSight to run analysis on our final data
    - Used cloudwatch to monitor all of the processes for easy tracking.
    """)
    image1 = Image.open("C:/Users/A.M. MUKTAR/my_portfolio/Images/pipeline.png")
    image2 = Image.open("C:/Users/A.M. MUKTAR/my_portfolio/Images/analytics.png")
    st.image(image1)
    st.image(image2)
    
    
st.header("Data Analysis Project  Section")
st.subheader('Pandas')
with st.expander("PROJECT 1: Analysis of Ligue 1 From 2010-2021"):
    st.subheader('Analysis of Ligue 1 From 2010-2021')
    st.write("This project intends to ...")
    st.markdown("""
    - Collaborated and developed a state-of-the-art deep learning model using BERT and gensims Doc2Vec for recognizing song emotion and give recommendations based on that given lyrics, song title and artist name.
    - Deployed the model on Heroku and serve the it using FastApi.
    - Develop and deployed the app on streamlit.
    - Presented the work as part of our masters thesis.
    """)
    # # st.image("https://static.streamlit.io/examples/dice.jpg")
    st.markdown("[Project CODE](https://github.com/sadiksmart0/DataVisualizationProject)")
  

with st.expander("PROJECT 1: Analysis of Google play Apps"):
    st.subheader('Analysis of Google play Apps')
    st.write("This project intends to ...")
    st.markdown("""
    - Collaborated and developed a state-of-the-art deep learning model using BERT and gensims Doc2Vec for recognizing song emotion and give recommendations based on that given lyrics, song title and artist name.
    - Deployed the model on Heroku and serve the it using FastApi.
    - Develop and deployed the app on streamlit.
    - Presented the work as part of our masters thesis.
    """)
    # # st.image("https://static.streamlit.io/examples/dice.jpg")
    st.markdown("[Project CODE](https://github.com/sadiksmart0/Android-App-Market/blob/main/Android%20App%20Market.ipynb)")
  

with st.expander("PROJECT 1: Analysis of Netflix movies"):
    st.subheader('Analysis of Netflix movies')
    st.write("This project intends to ...")
    st.markdown("""
    - Collaborated and developed a state-of-the-art deep learning model using BERT and gensims Doc2Vec for recognizing song emotion and give recommendations based on that given lyrics, song title and artist name.
    - Deployed the model on Heroku and serve the it using FastApi.
    - Develop and deployed the app on streamlit.
    - Presented the work as part of our masters thesis.
    """)
    # # st.image("https://static.streamlit.io/examples/dice.jpg")
    st.markdown("[Project CODE](https://github.com/sadiksmart0/Netflix-Movies/blob/main/Netflix-Movies.ipynb)")
   

with st.expander("PROJECT 1: Analysis of Nobel Prize Winners"):
    st.subheader('Analysis of Nobel Prize Winners')
    st.write("This project intends to ...")
    st.markdown("""
    - Collaborated and developed a state-of-the-art deep learning model using BERT and gensims Doc2Vec for recognizing song emotion and give recommendations based on that given lyrics, song title and artist name.
    - Deployed the model on Heroku and serve the it using FastApi.
    - Develop and deployed the app on streamlit.
    - Presented the work as part of our masters thesis.
    """)
    # # st.image("https://static.streamlit.io/examples/dice.jpg")
    st.markdown("[Project CODE](https://github.com/sadiksmart0/Nobel-Prize/blob/main/Nobel_Prize.ipynb)")
   
st.subheader('Tableau')
st.subheader('Dataiku')
