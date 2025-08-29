import streamlit as st

st.title("Prototipo Corporate AI — MVP")

st.text_input("Chi sei?")
st.text_area("Incolla qui il brief")
st.checkbox("Vuoi generare anche un’immagine AI?")
st.checkbox("Vuoi impaginare su Figma?")

if st.button("Lancia generazione"):
    st.write("🧠 Sto elaborando il tuo contenuto…")
    # Qui collegheremo GPT, Perplexity, Gemini e Figma