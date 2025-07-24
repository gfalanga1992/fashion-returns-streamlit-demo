import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Carica la chiave API da file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def customer_agent(input_cliente):
    prompt = f"""Classifica la motivazione del reso tra:
    - 'difettoso'
    - 'taglia errata'
    - 'cambio idea'
    - 'altro'
    Testo: \"{input_cliente}\"
    Rispondi con una sola categoria."""
    return ask_gpt(prompt)

def product_agent(descrizione):
    prompt = f"""Valuta lo stato del prodotto:
    - 'prodotto difettoso'
    - 'prodotto accettabile'
    Descrizione: \"{descrizione}\""""
    return ask_gpt(prompt)

def logistics_agent():
    return "Ritiro programmato con DHL. Tracking: 123ABC."

def decision_agent(motivo, stato):
    prompt = f"""Motivo: {motivo}\nStato: {stato}
Approvare o rifiutare il reso? Rispondi con 'Approvato' o 'Rifiutato' + motivazione."""
    return ask_gpt(prompt)

st.set_page_config(page_title="Gestione Resi Fashion", page_icon="🔁")
st.title("🔁 Sistema Intelligente Gestione Resi")

cliente_input = st.text_area("✍️ Inserisci la richiesta del cliente")
prodotto_input = st.text_area("📄 Descrizione del prodotto")

if st.button("▶️ Avvia Analisi"):
    with st.spinner("🧠 Customer Agent in corso..."):
        motivo = customer_agent(cliente_input)
        st.success(f"Motivazione rilevata: {motivo}")

    with st.spinner("🔎 Product Agent in corso..."):
        stato = product_agent(prodotto_input)
        st.success(f"Stato prodotto: {stato}")

    with st.spinner("🚚 Logistics Agent..."):
        logistica = logistics_agent()
        st.success(logistica)

    with st.spinner("⚖️ Decision Agent..."):
        decisione = decision_agent(motivo, stato)
        st.success(f"Decisione finale: {decisione}")
