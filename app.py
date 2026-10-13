import streamlit as st

a = st.chat_input("Enter a command")

if a:
    st.chat_message("user").write(a)

    if a.lower() == "hi":
        st.chat_message("assistant").write("Hello")

    elif a.lower() == "hello":
        st.chat_message("assistant").write("Hi, how are you?")

    elif a.lower() == "how are you":
        st.chat_message("assistant").write("I am Good, thank you!")

    elif a.lower() == "good morning":
        st.chat_message("assistant").write("Good morning!")

    elif a.lower() == "good afternoon":
        st.chat_message("assistant").write("Good afternoon!")

    elif a.lower() == "good evening":
        st.chat_message("assistant").write("Good evening!")

    elif a.lower() == "what is your name":
        st.chat_message("assistant").write("My name is ChatBot.")

    elif a.lower() == "who are you":
        st.chat_message("assistant").write("I am a simple chatbot.")

    elif a.lower() == "thank you":
        st.chat_message("assistant").write("You are welcome!")

    elif a.lower() == "bye":
        st.chat_message("assistant").write("Goodbye!")

    elif a.lower() == "what is python":
        st.chat_message("assistant").write("Python is a programming language.")

    elif a.lower() == "what is streamlit":
        st.chat_message("assistant").write("Streamlit is a Python framework for creating web apps.")

    elif a.lower() == "what is chatbot":
        st.chat_message("assistant").write("A chatbot is a program that communicates with users.")

    else:
        st.chat_message("assistant").write("Sorry, I don't understand that command.")