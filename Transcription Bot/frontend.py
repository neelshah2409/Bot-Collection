import requests
import streamlit as st
def main():
    st.title('Real-time Voice Transcription')
    audio_file = st.file_uploader('Upload an audio file', type=['wav', 'mp3'])

    if audio_file is not None:
        files = {'audio': audio_file}
        response = requests.post('http://localhost:5000/transcribe', files=files)
        transcribed_text = response.text
        st.header('Transcription Result')
        st.write(transcribed_text)

if __name__ == '__main__':
    main()
