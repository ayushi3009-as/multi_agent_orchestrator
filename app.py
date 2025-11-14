import streamlit as st
from orchestrator import Orchestrator
from tools.doc_reader import read_pdf, read_docx, read_txt

st.title("🧠 Multi-Agent Document & Web Intelligence")

orch = Orchestrator()
uploaded_text = None

file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if file:
    if file.type == "application/pdf":
        uploaded_text = read_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        uploaded_text = read_docx(file)
    else:
        uploaded_text = read_txt(file)

query = st.text_input("Ask a question:")

if st.button("Run"):
    response = orch.route(query, uploaded_text)
    st.write("### Response:")
    st.write(response)
