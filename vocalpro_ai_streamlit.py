
import streamlit as st
from pedalboard import Pedalboard, Compressor, HighPassFilter, HighShelfFilter, Gain, NoiseGate
import soundfile as sf
import io

st.set_page_config(page_title="VocalPro AI", page_icon="🎙️")

st.title("🎙️ VocalPro AI")
st.write("Suba sua voz e clique no botão para mixar profissionalmente.")

# Upload
uploaded_file = st.file_uploader("Escolha um arquivo de áudio", type=["wav", "mp3"])

if uploaded_file is not None:
    # Mostra o player do áudio original
    st.audio(uploaded_file, format='audio/wav')
    
    # BOTÃO QUE ESTÁ FALTANDO:
    if st.button("✨ Iniciar Mixagem Profissional"):
        with st.spinner("Processando áudio..."):
            # Lendo o áudio
            data, samplerate = sf.read(uploaded_file)
            
            # Criando a mixagem
            board = Pedalboard([
                NoiseGate(threshold_db=-40),
                HighPassFilter(cutoff_frequency_hz=100),
                Compressor(threshold_db=-18, ratio=4),
                HighShelfFilter(cutoff_frequency_hz=8000, gain_db=5),
                Gain(gain_db=2)
            ])

            vocal_mixado = board(data, samplerate)

            # Preparando para download
            buffer = io.BytesIO()
            sf.write(buffer, vocal_mixado, samplerate, format='WAV')
            buffer.seek(0)

            st.success("Mixagem concluída!")
            st.audio(buffer, format='audio/wav')
            
            # BOTÃO DE DOWNLOAD
            st.download_button(
                label="📥 Baixar Áudio Final",
                data=buffer,
                file_name="vocal_mixado.wav",
                mime="audio/wav"
            )
