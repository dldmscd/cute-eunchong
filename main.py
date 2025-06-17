st.title("🧑‍🎨 메이크업 룩 스타일링")

lip_color = st.color_picker("💋 립 컬러 선택")
eye_shadow = st.color_picker("👁️ 아이섀도우 색상 선택")
blush = st.color_picker("🥰 블러셔 색상 선택")

st.write("✅ 당신의 오늘의 메이크업 조합:")
st.markdown(f"- 💄 립: `{lip_color}`")
st.markdown(f"- 👁️ 아이섀도우: `{eye_shadow}`")
st.markdown(f"- 🥰 블러셔: `{blush}`")

if st.button("룩 완성!"):
    st.balloons()
    st.success("✨ 메이크업 완성! 친구들과 공유해보세요.")
