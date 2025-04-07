import streamlit as st
import time
import base64
import os
import requests
from vectors import EmbeddingsManager  # Import EmbeddingManager Class
from chatbot import ChatbotManager  # Import ChatbotManager class

# Qdrant Configuration
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "vector_db"

# Function to check if Qdrant is running
def check_qdrant():
    try:
        response = requests.get(f"{QDRANT_URL}/healthz")
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False

# Function to display the PDF of a given file
def displayPDF(file):
    """Reads and displays the uploaded PDF file in an iframe."""
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Initialize session_state variables
if 'temp_pdf_path' not in st.session_state:
    st.session_state['temp_pdf_path'] = None
if 'chatbot_manager' not in st.session_state:
    st.session_state['chatbot_manager'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'qdrant_ready' not in st.session_state:
    st.session_state['qdrant_ready'] = check_qdrant()

# Set page configuration
st.set_page_config(
    page_title="Document Buddy APP",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
with st.sidebar:
    st.image("logo.png", use_container_width=True)  # Fixed use_column_width deprecated warning
    st.markdown('### 📚 Your Document Assistant')
    st.markdown("---")

    # Navigation Menu
    menu = ["🏠 Home", "🤖 ChatBot", "📧 Contact"]
    choice = st.selectbox("Navigate", menu)

# Home Page
if choice == "🏠 Home":
    st.title("📄 Document Buddy App")
    st.markdown("""
        Welcome to **Document Buddy APP**! 🚀  
        **Built using Open Source Stack (Llama 3.2, BGE Embeddings, and Qdrant running locally in Docker)**  

        - **Upload Documents**: Easily upload your PDF documents.  
        - **Summarize**: Get concise summaries of your documents.  
        - **Chat**: Interact with your documents through our intelligent chatbot.  

        Enhance your document management experience with Document Buddy! 😊  
    """)

# Chatbot Page
elif choice == "🤖 ChatBot":
    st.title("🤖 Chatbot Interface (Llama 3.2 RAG 🦙)")
    st.markdown("---")

    # Qdrant Connection Check
    if not st.session_state['qdrant_ready']:
        st.error("⚠️ Qdrant is not running. Please start Qdrant and try again.")
        st.stop()

    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Column 1: File Uploader and Preview
    with col1:
        st.header("📂 Upload Document")
        uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
        if uploaded_file is not None:
            st.success("📄 File Uploaded Successfully!")
            st.markdown(f"**Filename:** {uploaded_file.name}")
            st.markdown(f"**File Size:** {uploaded_file.size} bytes")

            # Display PDF preview
            st.markdown("### 📖 PDF Preview")
            displayPDF(uploaded_file)

            # Save the uploaded file to a temporary location
            temp_pdf_path = f"temp_{uploaded_file.name}"
            with open(temp_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Store the temp_pdf_path in session state
            st.session_state['temp_pdf_path'] = temp_pdf_path

    # Column 2: Create Embeddings
    with col2:
        st.header("🧠 Embeddings")
        create_embeddings = st.checkbox("✅ Create Embeddings")
        if create_embeddings:
            if st.session_state['temp_pdf_path'] is None:
                st.warning("⚠️ Please upload a PDF first.")
            else:
                try:
                    # Initialize the EmbeddingManager
                    embedding_manager = EmbeddingsManager(
                        model_name="BAAI/bge-small-en",
                        device="cpu",
                        encode_kwargs={"normalize_embeddings": True},
                        qdrant_url=QDRANT_URL,
                        collection_name=COLLECTION_NAME
                    )

                    with st.spinner("🔄 Generating embeddings..."):
                        result = embedding_manager.create_embeddings(st.session_state['temp_pdf_path'])
                        time.sleep(1)  # To show the spinner
                    st.success(result)

                    # Initialize ChatbotManager after embeddings are created
                    if st.session_state['chatbot_manager'] is None:
                        st.session_state['chatbot_manager'] = ChatbotManager(
                            model_name="BAAI/bge-small-en",
                            device="cpu",
                            encode_kwargs={"normalize_embeddings": True},
                            llm_model="llama3.2:3b",
                            llm_temperature=0.7,
                            qdrant_url=QDRANT_URL,
                            collection_name=COLLECTION_NAME
                        )

                except Exception as e:
                    st.error(f"⚠️ An error occurred: {e}")

    # Column 3: Chatbot Interface
    with col3:
        st.header("💬 Chat with Document")

        if st.session_state['chatbot_manager'] is None:
            st.info("🤖 Please upload a PDF and create embeddings to start chatting.")
        else:
            # Display previous messages
            for msg in st.session_state['messages']:
                st.chat_message(msg['role']).markdown(msg['content'])

            # User Input
            if user_input := st.chat_input("Type your message here..."):
                # Display user message
                st.chat_message("user").markdown(user_input)
                st.session_state['messages'].append({"role": "user", "content": user_input})

                with st.spinner("🤖 Generating response..."):
                    try:
                        # Get chatbot response
                        answer = st.session_state['chatbot_manager'].get_response(user_input)
                        time.sleep(1)  # Simulate processing time
                    except Exception as e:
                        answer = f"⚠️ An error occurred while processing your request: {e}"

                # Display chatbot response
                st.chat_message("assistant").markdown(answer)
                st.session_state['messages'].append({"role": "assistant", "content": answer})

# Contact Page
elif choice == "📧 Contact":
    st.title("📬 Contact Us")
    st.markdown("""
        We'd love to hear from you! Whether you have a question, feedback, or want to contribute, feel free to reach out.  

        - **Email:** [developer@example.com](mailto:aakashharwani06@gmail.com) ✉️  
        - **GitHub:** [Contribute on GitHub](https://github.com) 🛠️  

        If you'd like to request a feature or report a bug, please open a pull request on our GitHub repository.  
        Your contributions are highly appreciated! 🙌  
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 Document Buddy App by Aakash Harwani. All rights reserved. 🛡️")
