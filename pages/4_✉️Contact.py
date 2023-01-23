import streamlit as st 

st.title("Vous souhaitez nous contacter? ")
st.subheader("Plusieurs options sont possibles! ")


###Create a contact form
contact_form= """"
<form action="https://formsubmit.co/anaisprojetcours@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
