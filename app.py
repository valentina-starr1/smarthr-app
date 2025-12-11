import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartHR • AI Powered HR App", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beige theme
st.markdown("""
<style>
    /* Import professional font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f1e8 0%, #ebe4d1 100%);
    }
    
    /* Header styling */
    h1 {
        color: #5a4a3a !important;
        font-weight: 700 !important;
        font-size: 3rem !important;
        margin-bottom: 0.5rem !important;
        text-align: center;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #7a6a5a !important;
        font-weight: 500 !important;
        font-size: 1.2rem !important;
        text-align: center;
        margin-bottom: 2rem !important;
    }
    
    h3 {
        color: #5a4a3a !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Card containers */
    .main-card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(90, 74, 58, 0.1);
        margin-bottom: 2rem;
        border: 1px solid #e8dcc8;
    }
    
    /* Form styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #faf8f3 !important;
        border: 2px solid #e8dcc8 !important;
        border-radius: 12px !important;
        color: #5a4a3a !important;
        font-size: 1rem !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #c4a57b !important;
        box-shadow: 0 0 0 3px rgba(196, 165, 123, 0.1) !important;
    }
    
    /* Labels */
    .stTextInput > label,
    .stTextArea > label {
        color: #5a4a3a !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #c4a57b 0%, #a88f6b 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 32px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(196, 165, 123, 0.3) !important;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(196, 165, 123, 0.4) !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #faf8f3 0%, #f5f1e8 100%) !important;
        border: 2px solid #e8dcc8 !important;
        border-radius: 12px !important;
        color: #5a4a3a !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding: 1rem 1.5rem !important;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #f5f1e8 0%, #ebe4d1 100%) !important;
        border-color: #c4a57b !important;
    }
    
    .streamlit-expanderContent {
        background: white !important;
        border: 2px solid #e8dcc8 !important;
        border-top: none !important;
        border-radius: 0 0 12px 12px !important;
        padding: 1.5rem !important;
    }
    
    /* Success/Info/Warning messages */
    .stSuccess {
        background-color: #e8f5e9 !important;
        color: #2e7d32 !important;
        border-left: 4px solid #66bb6a !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    .stInfo {
        background-color: #e3f2fd !important;
        color: #1565c0 !important;
        border-left: 4px solid #42a5f5 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    .stWarning {
        background-color: #fff3e0 !important;
        color: #e65100 !important;
        border-left: 4px solid #ff9800 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #faf8f3 0%, #f5f1e8 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border: 2px solid #e8dcc8;
        text-align: center;
        margin: 0.5rem;
    }
    
    .metric-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #c4a57b;
        margin: 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #7a6a5a;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    
    /* Skills badge */
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #c4a57b 0%, #a88f6b 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.85rem;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(196, 165, 123, 0.3);
    }
    
    /* Form container */
    .stForm {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid #e8dcc8;
        box-shadow: 0 8px 32px rgba(90, 74, 58, 0.08);
    }
    
    /* Header decoration */
    .header-decoration {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .header-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #c4a57b, transparent);
        margin: 2rem 0;
    }
    
    /* Stats container */
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        gap: 1rem;
    }
    
    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem;
        color: #7a6a5a;
    }
    
    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.3;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "employees" not in st.session_state:
    st.session_state["employees"] = []

# Header with icon
st.markdown('<div class="header-decoration"><div class="header-icon">👔</div></div>', unsafe_allow_html=True)
st.title("SmartHR • AI Powered")
st.subheader("Intelligent Employee Management & Resume Analysis")

# Statistics dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-number">{len(st.session_state["employees"])}</p>
        <p class="metric-label">Total Employees</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.session_state["employees"]:
        avg_skills = sum(len([skill for skill in ['JavaScript', 'HTML', 'CSS', 'Python', 'Java', 'Project Management', 'Leadership', 'React', 'Communication', 'SQL', 'Design'] 
                             if skill.lower() in emp["resume"].lower()]) 
                        for emp in st.session_state["employees"]) / len(st.session_state["employees"])
    else:
        avg_skills = 0
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-number">{avg_skills:.1f}</p>
        <p class="metric-label">Avg. Skills/Employee</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_skills = sum(len([skill for skill in ['JavaScript', 'HTML', 'CSS', 'Python', 'Java', 'Project Management', 'Leadership', 'React', 'Communication', 'SQL', 'Design'] 
                           if skill.lower() in emp["resume"].lower()]) 
                      for emp in st.session_state["employees"])
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-number">{total_skills}</p>
        <p class="metric-label">Total Skills Pool</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Add Employee Form
st.markdown("### ➕ Add New Employee")

with st.form(key="employee_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name", placeholder="e.g., John Smith")
        email = st.text_input("Email Address", placeholder="e.g., john.smith@company.com")
    
    with col2:
        department = st.text_input("Department", placeholder="e.g., Engineering")
        position = st.text_input("Position", placeholder="e.g., Senior Developer")
    
    resume = st.text_area(
        "Resume / Professional Summary", 
        placeholder="Paste resume text here or provide a professional summary including skills, experience, and qualifications...",
        height=200
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submit = st.form_submit_button("✨ Add Employee to Directory")
    
    if submit and name and email and resume:
        st.session_state["employees"].append({
            "name": name, 
            "email": email, 
            "department": department or "Not specified",
            "position": position or "Not specified",
            "resume": resume
        })
        st.success(f"✅ Successfully added {name} to the employee directory!")
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# Employee Directory
st.markdown("### 📋 Employee Directory")

if not st.session_state["employees"]:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-state-icon">📁</div>
        <h3>No employees yet</h3>
        <p>Add your first employee using the form above to get started!</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Search and filter
    search_term = st.text_input("🔍 Search employees", placeholder="Search by name, email, or skills...")
    
    filtered_employees = st.session_state["employees"]
    if search_term:
        filtered_employees = [emp for emp in st.session_state["employees"] 
                            if search_term.lower() in emp["name"].lower() 
                            or search_term.lower() in emp["email"].lower()
                            or search_term.lower() in emp["resume"].lower()]
    
    st.markdown(f"**Showing {len(filtered_employees)} of {len(st.session_state['employees'])} employees**")
    st.markdown("")
    
    for idx, emp in enumerate(filtered_employees):
        with st.expander(f"👤 {emp['name']} • {emp['email']} • {emp['position']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**📧 Email:** {emp['email']}")
                st.markdown(f"**🏢 Department:** {emp['department']}")
                st.markdown(f"**💼 Position:** {emp['position']}")
            
            with col2:
                if st.button(f"🔍 Analyze Resume", key=f"analyze_{idx}", use_container_width=True):
                    with st.spinner("Analyzing resume..."):
                        # Simulated skill extraction
                        SKILLS = ['JavaScript', 'HTML', 'CSS', 'Python', 'Java', 'C++', 'C#', 
                                'Project Management', 'Leadership', 'React', 'Angular', 'Vue',
                                'Communication', 'SQL', 'NoSQL', 'MongoDB', 'Design', 'AWS', 
                                'Azure', 'Docker', 'Kubernetes', 'Agile', 'Scrum', 'Git',
                                'Machine Learning', 'AI', 'Data Analysis', 'TypeScript']
                        
                        found = [skill for skill in SKILLS if skill.lower() in emp["resume"].lower()]
                        
                        if found:
                            st.success(f"✅ **Analysis Complete!**")
                            
                            # Display skills as badges
                            st.markdown("**🎯 Identified Skills:**")
                            skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in found])
                            st.markdown(skills_html, unsafe_allow_html=True)
                            
                            # Profile assessment
                            st.markdown("")
                            if len(found) >= 5:
                                st.info("💎 **Expert Profile:** Highly skilled multi-domain professional with extensive expertise.")
                            elif len(found) >= 3:
                                st.info("⭐ **Strong Profile:** Multi-skilled candidate with solid competencies.")
                            else:
                                st.info("📌 **Specialist Profile:** Focused expertise in core areas.")
                            
                            # Skill categories
                            tech_skills = [s for s in found if s in ['JavaScript', 'HTML', 'CSS', 'Python', 'Java', 'C++', 'C#', 'React', 'Angular', 'Vue', 'SQL', 'NoSQL', 'MongoDB', 'TypeScript', 'Docker', 'Kubernetes', 'AWS', 'Azure']]
                            soft_skills = [s for s in found if s in ['Project Management', 'Leadership', 'Communication', 'Agile', 'Scrum']]
                            
                            if tech_skills or soft_skills:
                                col1, col2 = st.columns(2)
                                with col1:
                                    if tech_skills:
                                        st.markdown(f"**💻 Technical:** {len(tech_skills)} skills")
                                with col2:
                                    if soft_skills:
                                        st.markdown(f"**🤝 Soft Skills:** {len(soft_skills)} skills")
                        else:
                            st.warning("⚠️ No major skills detected. Consider adding more keywords or details to the resume.")
            
            st.markdown("---")
            st.markdown("**📄 Resume:**")
            st.text_area("", emp["resume"], height=150, key=f"resume_{idx}", disabled=True, label_visibility="collapsed")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("📧 Send Email", key=f"email_{idx}", use_container_width=True):
                    st.info(f"Email client opening for: {emp['email']}")
            with col2:
                if st.button("📝 Edit Profile", key=f"edit_{idx}", use_container_width=True):
                    st.info("Edit functionality - Coming soon!")
            with col3:
                if st.button("🗑️ Remove", key=f"delete_{idx}", use_container_width=True):
                    st.session_state["employees"].remove(emp)
                    st.success(f"Removed {emp['name']} from directory")
                    st.rerun()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #7a6a5a; padding: 2rem;">
    <p style="margin: 0; font-weight: 500;">SmartHR • AI Powered HR Management System</p>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.7;">Streamlining talent management with intelligent automation</p>
</div>
""", unsafe_allow_html=True)
