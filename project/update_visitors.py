import pandas as pd
import streamlit as st
from database import update_visitor_data

def update_visitors(ids):
    selected_id = st.selectbox("Choose the SRN :",ids)
    st.warning("Do you want to update ::{}".format(selected_id))
    col1, col2 = st.columns(2)
    with col1:
        visitor_id = st.text_input("Enter id :")
        fname = st.text_input("Enter your First Name :")
        lname = st.text_input("Enter your Last Name :")
        date = st.date_input("Visit date :")

    with col2:
        in_time = st.text_input("Enter in_time in 2400 hrs format :")
        out_time = st.text_input("Enter out_time in 2400 hrs format :")
        mobile = st.number_input("Your mobile number :")
        srn = st.text_input("Enter the students srn :")
        
    if st.button("Update visitor"):
        update_visitor_data(visitor_id,fname,lname,date,in_time,out_time,mobile,srn)
        st.success("Update visitor record : {}".format(visitor_id))