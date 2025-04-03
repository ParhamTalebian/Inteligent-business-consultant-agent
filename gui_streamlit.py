import streamlit as st
from llm_interface import LLMInterface
from retrieval_engine import RetrievalEngine
from business_plan_generator import BusinessPlanGenerator
from document_reader import DocumentReader
from memory_manager import MemoryManager

API_KEY = "cf695d0e05061568bad485126184ca88a09340cd8540ec31deee936b83914c1a"
llm = LLMInterface(api_key=API_KEY)
retrieval_engine = RetrievalEngine()
business_plan_generator = BusinessPlanGenerator()
doc_reader = DocumentReader()
memory_manager = MemoryManager()

st.title("💡 مشاور هوشمند کسب‌وکار")

question = st.text_input("🔍 سوال خود را وارد کنید:")

if st.button("📩 ارسال"):
    if question.strip():
        with st.spinner("⏳ در حال پردازش..."):
            response = llm.ask(question)
            st.success("✅ پاسخ دریافت شد!")
            st.write("💬 **پاسخ:**")
            st.write(response)

            relevant_data = retrieval_engine.search(question)
            st.write("📂 **اطلاعات مرتبط:**")
            st.write(relevant_data)

            memory_manager.save_conversation(question, response)

            business_plan = business_plan_generator.generate_business_plan(response)
            st.write("📋 **طرح کسب‌وکار:**")
            st.write(business_plan)

    else:
        st.warning("⚠️ لطفاً یک سوال وارد کنید!")

uploaded_file = st.file_uploader("بارگذاری فایل (PDF/Word):", type=["pdf", "docx", "txt"])
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        content = doc_reader.read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        content = doc_reader.read_docx(uploaded_file)
    else:
        content = doc_reader.read_text_file(uploaded_file)

    st.write("📄 **محتوای فایل بارگذاری‌شده:**")
    st.write(content)
