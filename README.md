# AskLaw - Moroccan Labor Law Chatbot

## Overview

AskLaw is an advanced chatbot designed to provide legal consultations on Moroccan labor law. Leveraging state-of-the-art technologies, including the LLaMA 3 language model and Flask for the web interface, AskLaw delivers precise and contextually relevant responses to users' legal inquiries. This project aims to simplify access to labor law information and support legal research.

## Features

### Interactive Consultation
- **Legal Query Responses**: Provides precise answers to user questions about Moroccan labor law, based on the latest legal texts and interpretations.
- **Contextual Understanding**: Utilizes advanced natural language processing (NLP) techniques to understand and respond appropriately to diverse legal queries.

### User Profiles and History
- **User Profiles**: Stores user information and preferences to tailor responses and enhance the interaction experience.
- **Consultation History**: Allows users to view and review their past interactions and consultations for better tracking and reference.

### Consultation Summaries
- **Summary Generation**: Automatically generates concise summaries of legal consultations, making it easier for users to understand and retain key information.

### Usage Statistics
- **Analytics**: Monitors and reports on usage metrics such as query frequency, response accuracy, and user engagement, aiding in ongoing improvement and system optimization.

## Technology Stack

- **Backend**: Django
  - A high-level Python web framework that facilitates rapid development and clean, pragmatic design. Handles application logic, data management, and backend services.
- **Frontend**: Flask
  - A lightweight Python framework used to build the web interface for the chatbot, providing a seamless user experience.
- **Language Model**: LLaMA 3
  - Meta’s latest language model, known for its advanced capabilities in understanding and generating human-like text.
- **Database**: Chroma
  - A vector database used for storing and querying large amounts of legal text data, enabling efficient retrieval of relevant information.
- **API Integration**: ChatGroq
  - Optimizes interaction with the LLaMA 3 model for improved response times and accuracy.
- **Retrieval-Augmented Generation (RAG)**:
  - **Integration**: Combines retrieval of relevant legal documents with generation of responses to enhance accuracy and context.
  - **Functionality**: Retrieves pertinent documents from a database and uses them to generate precise and contextually relevant answers to legal queries.

## Installation

### Prerequisites

Before setting up the AskLaw application, ensure you have the following installed:

- **Python 3.x**: Python is required for running both the backend and frontend components. Download and install Python from [python.org](https://www.python.org/).
- **MySQL**: A relational database system for managing user data and application state. Install MySQL from [mysql.com](https://www.mysql.com/).
- **pip**: Python’s package installer for managing project dependencies.

### Steps

1. **Clone the Repository**:
   - To get the latest version of the AskLaw project, clone the repository from GitHub:
     ```sh
     git clone https://github.com/yourusername/asklaw.git
     cd asklaw
     ```

2. **Install Dependencies**:
   - Install all required Python packages listed in `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```

3. **Set Up the Database**:
   - Configure the `settings.py` file with your MySQL database credentials. Edit the database settings section to include your MySQL database information.
   - Apply migrations to set up the database schema and create necessary tables:
     ```sh
     python manage.py migrate
     ```

4. **Run the Application**:
   - Start the Django development server to run the application locally:
     ```sh
     python manage.py runserver
     ```
   - The application will be accessible at `http://localhost:8000` in your web browser.

## Usage

1. **Access the Application**:
   - Open your web browser and navigate to `http://localhost:8000` to interact with the AskLaw chatbot.

2. **Ask Questions**:
   - Type your legal queries related to Moroccan labor law into the chat interface to receive responses.

3. **View Consultation History**:
   - Log in to your profile to review past consultations and summaries.

## API Endpoints

- **/ask**: Endpoint for submitting legal queries to the chatbot.
  - **Method**: POST
  - **Description**: Submits a legal question and receives a response from the chatbot.
- **/history**: Endpoint for retrieving consultation history.
  - **Method**: GET
  - **Description**: Retrieves a list of past consultations for the logged-in user.
- **/summary**: Endpoint for generating summaries of consultations.
  - **Method**: GET
  - **Description**: Provides a summary of a specific consultation based on user request
