import streamlit as st 
from advisor import analyze_student 

st.title ("Ai tu van hoc tap cho sinh vien")
gpa=st.slider("Gpa",0.0,4.0,2.5)
study_hours=st.slider("Gio hoc moi tuan ",0,40,10)
weak_subjects=st.slider("Muc do cham chi",1,5,3)
effort=st.slider("Muc do cham chi",1,5,3)

if st.button ("Phan tich"):
    level,reason,advice=analyze_student(
        gpa,study_hours,weak_subjects,effort
    )
    st.success(f"Hoc luc:{level}")
    st.info(f"Nguyen nhan:{reason}")
    st.warning(f"Loi khuyen:{advice}")