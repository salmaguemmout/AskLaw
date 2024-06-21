import streamlit as st
import ollama
from langchain_openai import OpenAI
from groq import Groq
from helpers.set_page_icons import page_icon  
from Management.compare_texts import chercher_similarite_commerce  
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="AskLaw - Conseiller en droit commercial",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

def extract_model_names(models_info: list) -> tuple:
    """
    Extracts the model names from the models information.

    :param models_info: A dictionary containing the models' information.

    Return:
        A tuple containing the model names.
    """
    return tuple(model["name"] for model in models_info["models"])

def main():
    """
    The main function that runs the application.
    """
    page_icon("📚")

    # Apply CSS for styling
    st.markdown("""
        <style>
        body {
            background-color: #FFF8DC; /* Cornsilk background */
        }
        .header-title {
            color: #3B82F6; /* Light Blue */
            font-size: 36px;
        }
        .header-subtitle {
            color: #1E3A8A; /* Dark Blue */
            font-size: 24px;
        }
        .description {
            color: #4B5563; /* Dark Grey */
            font-size: 16px;
        }
        .stButton > button {
            background-color: #FFD700; /* Yellow */
            color: #000000; /* Black */
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #FFC107; /* Darker Yellow */
        }
        .feature-list {
            color: #1E3A8A; /* Dark Blue */
            font-size: 18px;
        }
        .chat-section {
            color: #1E3A8A; /* Dark Blue */
            font-size: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Header Section
    st.markdown("<h1 class='header-title'>Bienvenue à AskLaw - Conseiller en Droit</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='header-subtitle'>Votre conseiller juridique alimenté par l'IA</h2>", unsafe_allow_html=True)
    st.markdown("<p class='description'>AskLaw est un chatbot alimenté par l'intelligence artificielle conçu pour fournir des conseils juridiques spécifiques au droit commercial marocain. Il aide les utilisateurs à obtenir des réponses précises et rapides sur diverses questions liées à la création et à la gestion d'entreprises, les obligations fiscales, les contrats commerciaux, et plus encore.</p>", unsafe_allow_html=True)

    # Main Options
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 class='feature-list'>Fonctionnalités</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='feature-list'>
        <li><b>Consultation Interactive</b> : Posez des questions spécifiques sur le droit commercial marocain et obtenez des réponses contextualisées.</li>
        <li><b>Historique des Discussions</b> : Affichage des messages précédents entre l'utilisateur et le chatbot pour une consultation continue.</li>
        <li><b>Résumé des Consultations</b> : Vue d'ensemble des consultations récentes et des réponses en attente.</li>
        <li><b>Profil Utilisateur</b> : Affichage des informations et de l'avatar de l'utilisateur.</li>
        <li><b>Statistiques</b> : Présentation des statistiques d'utilisation, comme le nombre de consultations effectuées.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Primary Call-to-Action
    st.markdown("<hr>", unsafe_allow_html=True)
    st.button("Commencer la Discussion", key="cta_button", help="Cliquez pour commencer à discuter avec AskLaw")

    client = ChatGroq(
        model="llama3-70b-8192",
        api_key='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',  
    )

    # Chat Section
    st.markdown("<h3 class='chat-section'>Discutez avec AskLaw</h3>", unsafe_allow_html=True)
    message_container = st.container()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = "📚" if message["role"] == "assistant" else "🙋🏻‍♂️"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Décrivez votre situation ou posez votre question..."):
        try:
            message_container.chat_message("user", avatar="🙋🏻‍♂️").markdown(prompt)
            full_prompt = chercher_similarite_commerce(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            with message_container.chat_message("assistant", avatar="📚"):
                with st.spinner("Le modèle travaille sur votre requête..."):
                    stream = client.invoke(full_prompt)
                    
                # stream response
                response = stream.content
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            st.error(e, icon="⛔️")

if __name__ == "__main__":
    main()
