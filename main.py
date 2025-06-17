import random
import streamlit as st

st.title("🎨 랜덤 컬러 팔레트 챌린지")

def random_colors(n=5):
    return ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(n)]

colors = random_colors()
st.write("🎯 이번 팔레트는 이 색상들이야!")
for c in colors:
    st.color_picker("색상", value=c, key=c)

look_name = st.text_input("이 색상으로 만든 메이크업 룩의 이름은?")
if look_name:
    st.success(f"💄 멋진 이름이야: {look_name}!")
