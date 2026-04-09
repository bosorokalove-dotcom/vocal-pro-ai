import streamlit as st
from pedalboard import Pedalboard, Reverb, Chorus
import soundfile as sf

st.title("Audio Processor App")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    audio, samplerate = sf.read(uploaded_file)

    board = Pedalboard([
        Chorus(),
        Reverb(room_size=0.25)
    ])

    effected = board(audio, samplerate)

    output_file = "output.wav"
    sf.write(output_file, effected, samplerate)

    st.audio(output_file)
    st.success("Processed audio ready!")

