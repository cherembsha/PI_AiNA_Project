# -*- coding: utf-8 -*-
"""AiNA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ESgyugW5-CnT9EbxCb3Q_cV4gelIQVfK

Модель определяет позитивную, нейтральную или негативную эмоцию содержит в себе текст.

Группа: Груздев Илья, Касимов Тимерхан.
"""

!pip install transformers sentencepiece

!pip install -q streamlit

import streamlit as st

from transformers import pipeline
model = pipeline(model="seara/rubert-tiny2-russian-sentiment")

def Em_T(x):
  model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
  return model(x)

st.title('Определить настроение по тексту')

st.warning('Чтобы остановить программу напишите "стоп"')

inp = st.text_input('Введите фразу, а я определю ваше настроение: ')

x = Em_T(inp)[0]
acc = round(x['score'] * 100, 3)

st.text(f'Я уверена на {acc}%')

if x['label'] == 'negative':
  st.error('У вас плохое настроение')
elif x['label'] == 'positive':
  st.success('У вас хорошее настроение')
else:
  st.warning('У вас нейтральное настроение')

#print('Стоп-слово --> стоп')

#while True:
#  inp = str(input('Напиши фразу, а я определю твое настроение --> '))
#  print('-'*10)
#  if inp.lower() == 'стоп':
#    print('Программа остановлена')
#    break
#  x = Em_T(inp)[0]

#  acc = round(x['score'] * 100, 3)
#  print('Я уверена на', acc ,'%')

#  if x['label'] == 'negative':
#    print('У вас плохое настроение :~(')
#  elif x['label'] == 'positive':
#    print("У вас хорошее настроение :~)")
#  else:
#    print("У вас нейтральное настроение -_-")
#  print('-'*10)