# RAG with Llama and Streamlit

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system powered by the **Llama** language model and deployed using **Streamlit**. The application allows users to input queries, retrieves relevant information from a knowledge base, and generates responses using Llama.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Advanced Configuration](#advanced-configuration)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)
10. [Contact](#contact)

---

## Overview

The RAG system combines the strengths of retrieval-based and generative models. It retrieves relevant documents or snippets from a knowledge base and uses the Llama language model to generate contextually accurate responses. This approach ensures both factual correctness and natural language fluency.

Streamlit is used to create an interactive web interface, making it easy for users to interact with the RAG system.

---

## Features

- **Retrieval-Augmented Generation**: Combines retrieval and generation for accurate and fluent responses.
- **Llama Integration**: Leverages the powerful Llama language model for text generation.
- **Streamlit Interface**: Provides an intuitive and user-friendly web interface.
- **Customizable Knowledge Base**: Easily integrate your own dataset or knowledge base.
- **Scalable Architecture**: Designed to handle large datasets and complex queries.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/aakash123254/Llama_RAG.git
   cd LLAMA
   ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    venv\Scripts\activate     # On Windows
    # source venv/bin/activate   # On Linux or MacOS
    pip install -r requirements.txt
    ```
3. Create required directories:
    ```bash
    mkdir models data
    ```
4. Download the Llama model weights and place them inside the models/ directory.

5. Run the application:
    ```bash 
    streamlit run app.py
    ```

# Usage
Open your browser and navigate to the URL displayed in the terminal (usually http://localhost:8501)

Enter your query in the input box and click Submit

The system will retrieve relevant information from the knowledge base and generate a response using Llama

View the results and continue interacting as needed

# Project Structure
```
    rag-llama-streamlit/
├── app.py                # Streamlit application entry point
├── requirements.txt      # List of Python dependencies
├── chatbot.py            # Directory for Llama model weights
├── vectors.py                 # Directory for knowledge base or dataset
├── logo.png
└── README.md             # Project documentation

```

# Contributing
We welcome contributions to improve this project! To contribute:

1. Fork the repository

2. Create a new branch:
```bash
    git checkout -b feature/YourFeatureName
```
3. Commit your changes:
```bash
    git commit -m "Add some feature"
```
4. Push to the branch:
```bash
    git push origin feature/YourFeatureName
```
5. Open a pull request
Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
🦙 Llama Team – For providing the powerful language model

🌟 Streamlit – For enabling rapid development of interactive web applications

🤝 Open-Source Community – For inspiration, tools, and continued support

For any questions or feedback, feel free to open an issue or contact the project maintainer.
Developer - Aakash Harwani
email: aakashharwani06@gmail.com

Happy coding! 🚀