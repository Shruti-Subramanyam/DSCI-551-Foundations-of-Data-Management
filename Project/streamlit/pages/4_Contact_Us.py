import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.write("# Contact Us 💬")
contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <input type="text" name="phone" placeholder="Phone No." required>
     <textarea name="message" placeholder="Enquiry"></textarea>
     <div style="text-align: left;">
        <button type="submit">Send</button>
     </div>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.markdown("""
---
### Our Location
Address: 123 Maple Street  
Phone Number: +123 456 7890
""")

local_css("style.css")
