import streamlit as st
import model as md
import seaborn as sns
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
st.title("Fruit Quality Predictor")

st.divider()
st.subheader("Data Frame")
st.write("4000 Rows and 8 Columns:")
st.dataframe(md.data)

st.divider()
st.title("Visualising the Data")
st.write("Comparing it with the Quality of Apple")
fig=sns.pairplot(md.data,hue="Quality")
st.pyplot(fig)
