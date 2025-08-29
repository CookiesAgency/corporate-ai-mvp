import streamlit as st

st.title("Prototipo Corporate AI — MVP")

nome = st.text_input("Chi sei?")
brief = st.text_area("Incolla qui il brief")

if st.button("Genera contenuti"):
    st.write(f"Ciao {nome}, il tuo brief è stato ricevuto.")
    st.write("✨ Sto generando i contenuti… (placeholder)")
    