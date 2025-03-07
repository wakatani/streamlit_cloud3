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

def printQ(c):
  st.write("Q[",c,"]: ","ABCDEFG")

st.title("■■■ クイズのコーナー ■■■")

if 'counter' not in st.session_state:
  st.session_state['counter'] = 0

counter=st.session_state['counter']

if counter==0:
  print(counter)
  st.session_state['counter']+=1

elif counter%2==1:
  answer= st.radio(
    "Your answer is ",
    ["１", "２", "３", "４"],
    horizontal=True,
    index=None,
    #on_change=ANS,
  )
  if st.button('答え'):
    st.write("ZZZZ ",counter,"answer: ",answer)
    st.session_state['counter'] += 1

else:  
  if st.button('問題'):
    print(counter)
    st.session_state['counter'] += 1





  




