#
#
#
from math import exp
import json
from openai import OpenAI
import os
import random
import copy
import streamlit as st

#load_dotenv()

#
# APIキーは環境変数にセットしておく
#
client = OpenAI()

#

st.title("■■■ クイズのコーナー ■■■")

if 'counter' not in st.session_state:
  st.session_state['counter'] = 0

counter=st.session_state['counter']

if counter%2==0 and st.button('問題'):
  st.write("XXXX ",counter)
  st.session_state['counter'] += 1

def ANS():
  st.write("YYYY ",counter)

if (answer= st.radio(
  "Your answer is ",
  ["１", "２", "３", "４"],
  horizontal=True,
  index=None,
  #on_change=ANS,
)!= None):
  st.write("QQQQ ",counter, "answer= ",answer)

if counter%2 ==1 and st.button('答え'):
  st.write("ZZZZ ",counter)
  st.session_state['counter'] += 1


  




