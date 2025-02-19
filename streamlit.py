import streamlit as st
import pickle
import sklearn
st.title("Jamboree Eduction Preidctions")
col1, col2 = st.columns(2)
Gre = col1.slider("Select GRE Score", 0, 340, 0)
Tofel = col2.slider("Select TOFEL Score", 0, 120, 0)
sop = col1.slider("Select SOP Score", 0.0, 5.0, 0.0)
lor = col2.slider("Select LOR Score", 0.0, 5.0, 0.0)
cgpa = col1.slider("Select CGPA Score", 0, 10, 0)
Univeristy_rating = col2.slider("Select University Rating", 0, 5, 0)
research = st.radio(
    "Select Research Experience",
    ["***Yes***", "***No***"],
    index=None,horizontal=True
)
research = 1 if research == "Yes" else 0
with open("Jamboree_Admission_model.pkl", "rb") as file:
    model = pickle.load(file)
#out = model.predict([[Gre, Tofel, sop, lor, cgpa, Univeristy_rating, research]])
if st.button("Predict"):
    out = model.predict([[Gre, Tofel, sop, lor, cgpa, Univeristy_rating, research]])
    st.write("Your chances of getting admission in Jamboree is ", out[0])
# completed
