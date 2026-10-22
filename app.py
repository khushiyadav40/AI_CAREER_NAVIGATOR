import pickle
import os
import pandas as pd
import streamlit as st

from Career_Navigator import CAREERS, ALL_SKILLS, skill_gap

st.set_page_config(page_title="AI Career Navigator", page_icon="🎯")
st.title("🎯 AI Career Navigator")
st.write("Discover careers, identify skill gaps, and plan your learning.")

if not os.path.exists("models/career_model.pkl"):
    st.warning("Please run: python train_model.py")
    st.stop()

with open("models/career_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/features.pkl", "rb") as f:
    features = pickle.load(f)

name = st.text_input("Your Name")
education = st.selectbox("Education", ["B.Tech", "BCA", "B.Sc", "Other"])
year = st.selectbox("Study Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
skills = st.multiselect("Your Skills", ALL_SKILLS)
interest = st.selectbox("Career Interest", ["No Preference"] + list(CAREERS))

if st.button("Recommend Career"):
    if not skills:
        st.warning("Please select at least one skill.")
    else:
        X = pd.DataFrame(
            [{s: int(s in skills) for s in features}],
            columns=features
        )
        prediction = model.predict(X)[0]
        career = interest if interest != "No Preference" else prediction

        st.subheader("Recommended Career")
        st.success(prediction)
        st.write(CAREERS[prediction]["skills"])

        st.subheader("Skill Gap Analysis")
        available, missing = skill_gap(career, skills)

        st.write("**Skills you have:**", ", ".join(available) or "None")
        st.write("**Skills to learn:**", ", ".join(missing) or "None")

        st.subheader("Learning Path")
        for i, step in enumerate(CAREERS[career]["path"], 1):
            st.write(f"{i}. {step}")

        st.subheader("Suggested Internships")
        for role in CAREERS[career]["internships"]:
            st.write("- " + role)

        st.caption(
            "Internship roles are suggestions, not confirmed vacancies. "
            "The model uses demonstration data and is not validated "
            "for real-world career predictions."
        )
