import streamlit as st

st.set_page_config(page_title="SmartHR  AI Powered HR App", layout="centered")

st.title("SmartHR  AI Powered HR App")
st.subheader("Employee Directory with Resume Analysis (Demo)")

if "employees" not in st.session_state:
    st.session_state["employees"] = []

with st.form(key="employee_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    resume = st.text_area("Resume (paste text)")
    submit = st.form_submit_button("Add Employee")
    if submit and name and email and resume:
        st.session_state["employees"].append({"name": name, "email": email, "resume": resume})
        st.success(f"Added {name}")

st.markdown("### Directory")
for idx, emp in enumerate(st.session_state["employees"]):
    with st.expander(f"{emp['name']}  {emp['email']}"):
        st.write("**Resume:**")
        st.write(emp["resume"])
        if st.button(f"Analyze Resume {idx}"):
            # Simulated skill extraction
            SKILLS = ['JavaScript', 'HTML', 'CSS', 'Python', 'Java', 'Project Management', 'Leadership', 'React', 'Communication', 'SQL', 'Design']
            found = [skill for skill in SKILLS if skill.lower() in emp["resume"].lower()]
            if found:
                st.success(f"Identified Skills: {', '.join(found)}")
                st.info(f"Profile Strengths: {'Multi-skilled' if len(found)>1 else 'Specialist'} candidate.")
            else:
                st.warning("No major skills detected, please add more keywords.")
