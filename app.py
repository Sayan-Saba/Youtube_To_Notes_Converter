import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() ##Load all the environment variables
import google.generativeai as genai
genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

from youtube_transcript_api import YouTubeTranscriptApi

prompt ="""You are a youtube video summarizer. You will be taking the transcript text and write the main points given. 
The summary should be in a detaileed manner but shouldn't be too long or too less somewhere in the middle where all the necessary content and important points are covered in the output.
The transcript text will be appended here : """

##Getting the transcript data from Youtube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript =" "
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    
    except Exception as e:
        raise e
    
#Getting the summary based on prompt from google gemini pro
def generate_video_notes(transcript_text, prompt):
    
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text


st.title("Youtube Video to Notes")
youtube_link = st.text_input("Enter the youtube video link: ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img/youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
if st.button("Get Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        notes = generate_video_notes(transcript_text, prompt)
        st.markdown("## Notes: ")
        st.write(notes)
    
    
    
