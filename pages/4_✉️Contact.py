import streamlit as st 

st.title("Vous souhaitez nous contacter? ")
st.subheader("Plusieurs options sont possibles! ")


###Create a contact form
contact_form= """"
<form action="https://formsubmit.co/anaisprojetcours@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Votre nom" required>
     <input type="email" name="email" placeholder="Votre email" required>
     <textarea name="message" placeholder"Votre message"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name): 
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./style/style.css")
