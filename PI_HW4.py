#Группа 1, Максимова Н.В.

from transformers import pipeline
import streamlit as st

st.title("Перевод текста с русского на французский")

translator = pipeline("translation_ru_to_fr", "Helsinki-NLP/opus-mt-ru-fr")
st.text = 'Перевод для предложения: "Это совсем непросто!"'
text = "Это совсем непросто!"
st.write("Перевод: ", translator(text))
