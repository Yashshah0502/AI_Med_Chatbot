import streamlit as st

def main():
    st.title("Welcome to My Streamlit App")
    st.write("This is a simple app to demonstrate Streamlit functionality.")

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        st.chat_message(message["role"]).markdown(message["content"])

    prompt = st.chat_input("Enter a prompt:")
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = "Hi, I am a medibot. "
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Here you can add functionality to process the prompt, e.g., call an LLM or perform some computation.
if __name__ == "__main__":
    main()