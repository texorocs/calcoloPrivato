import streamlit as st
import math

#    risultato = math.atan(y/(y-w)) * math.tan(v')  # Formula segreta

import streamlit as st

st.set_page_config(page_title="Calcolatore Dinamico", layout="centered")

st.title("Calcolatore Dinamico")

# Inizializza lo stato per memorizzare il numero di campi
if "num_elementi" not in st.session_state:
    st.session_state.num_elementi = 2  # Parte da 2 elementi di default

# --- FORMULA SEGRETA ---
def calcolo_riservato(lista_valori):
    # La tua formula personalizzata su N elementi
    risultato = sum(lista_valori)
    return risultato

st.write("Inserisci i valori nei campi sottostanti:")

valori = []
# Genera i campi di input dinamicamente
for i in range(st.session_state.num_elementi):
    val = st.number_input(f"Valore {i + 1}", value=0.0, key=f"input_{i}")
    valori.append(val)

# Pulsanti per gestire i campi
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Aggiungi un altro valore"):
        st.session_state.num_elementi += 1
        st.rerun()

with col2:
    if st.session_state.num_elementi > 1 and st.button("➖ Rimuovi ultimo valore"):
        st.session_state.num_elementi -= 1
        st.rerun()

st.divider()

if st.button("Calcola Risultato"):
    output = calcolo_riservato(valori)
    st.success(f"**Risultato:** {output:.2f}")