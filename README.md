# Kella.AI | Intelligent E-Commerce Assistant

Kella.AI is a high-performance shopping assistant engineered to streamline the online retail experience. Developed with a focus on modern web standards and machine learning, this project demonstrates the integration of a PyTorch-based NLP backend with a responsive, interactive frontend.

![Kella App Preview](static/images/app_preview.png)

## Project Overview

This application serves as a comprehensive e-commerce interface where users can interact with an intelligent agent to search for products, check order statuses, and receive instant support. The system is built on a Flask architecture, ensuring robust communication between the client-side interface and the server-side inference engine.

### Core Enhancements

*   **Architecture & Design**: The platform features a completely redesigned UI utilizing a glassmorphism aesthetic, custom gradient systems, and responsive layouts.
*   **Interactive Experience**: implemented a custom particle network background using HTML5 Canvas for a dynamic visual layer.
*   **Expanded NLP Capabilities**: The underlying model has been significantly expanded to handle over 35 distinct intent categories, ranging from complex logistics queries to casual conversation.

## Technical Stack

*   **Backend Framework**: Python (Flask)
*   **Machine Learning**: PyTorch (Neural Network for Intent Classification), NLTK (Natural Language Toolkit)
*   **Frontend**: HTML5, CSS3 (Custom Design System), JavaScript (ES6+), HTML5 Canvas

## Setup & Deployment

1.  **Environment Setup**:
    Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment.
    ```bash
    pip install flask torch torchvision nltk
    ```

2.  **Model Training**:
    The chatbot model must be trained on the intent dataset before running.
    ```bash
    python train.py
    ```
    *This generates the `data.pth` model file.*

3.  **Launch Application**:
    Start the Flask development server:
    ```bash
    python app.py
    ```

4.  **Access**:
    Navigate to `http://127.0.0.1:5000` in your web browser.

## Developer Credits

**Enhanced & Developed by Oussama Aslouj**

This project represents a significant evolution of standard chatbot implementations, pushing the boundaries of what's possible with meaningful UI/UX design and practical AI integration.
