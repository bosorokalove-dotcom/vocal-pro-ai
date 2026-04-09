import streamlit as st
from pedalboard import Pedalboard, Compressor, HighPassFilter, HighShelfFilter, Gain, NoiseGate
import soundfile as sf
import io

# Configuração visual do App
st.set_page_config(page_title="VocalPro AI", page_icon="🎙️")

st.title("🎙️ VocalPro AI")
st.subheader("Mixagem Profissional de Voz")

# Upload
uploaded_file = st.file_uploader("Arraste o seu áudio aqui", type=["wav", "mp3"])

if uploaded_file is not None:
    data, samplerate = sf.read(uploaded_file)
    st.audio(uploaded_file, format='audio/wav')

    if st.button("✨ Iniciar Mixagem"):
        with st.spinner("Refinando a sua voz..."):
            # Cadeia de sinal profissional (O segredo da qualidade)
            board = Pedalboard([
                NoiseGate(threshold_db=-40), # Remove ruído de fundo
                HighPassFilter(cutoff_frequency_hz=100), # Limpa graves desnecessários
                Compressor(threshold_db=-18, ratio=4), # Estabiliza o volume
                HighShelfFilter(cutoff_frequency_hz=8000, gain_db=5), # Dá brilho (Air)
                Gain(gain_db=2) # Ajuste final de volume
            ])

            vocal_mixado = board(data, samplerate)

            buffer = io.BytesIO()
            sf.write(buffer, vocal_mixado, samplerate, format='WAV')
            buffer.seek(0)

            st.success("Mixagem finalizada!")
            st.audio(buffer, format='audio/wav')
            st.download_button(label="📥 Baixar Áudio Profissional", data=buffer, file_name="vocal_final_pro.wav", mime="audio/wav")
