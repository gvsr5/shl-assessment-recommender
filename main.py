
import streamlit as st
from recommender import get_recommendations

st.set_page_config(page_title="SHL Assessment Recommender")
st.title("SHL Assessment Recommender")

query = st.text_area("Enter job description or query:", height=150)

if st.button("Recommend Assessments"):
    if query.strip():
        results = get_recommendations(query)
        st.write("### Recommended Assessments:")
        st.table(results)
    else:
        st.warning("Please enter a valid query.")
