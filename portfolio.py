import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Anjani Kumar Pokhrel | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# ---------------- DARK MODE + PROFILE CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

/* Profile image container */
.profile-img {
    width: 160px;
    height: 160px;
    border-radius: 50%;
    padding: 4px;
    background: linear-gradient(135deg, #00c6ff, #7f00ff, #ff0080);
    box-shadow: 0 0 20px rgba(128, 0, 255, 0.6);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

/* Image inside */
.profile-img img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    background-color: #0e1117;
}

/* Hover animation */
.profile-img:hover {
    transform: scale(1.07) rotate(1deg);
    box-shadow: 0 0 35px rgba(255, 0, 128, 0.9);
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .profile-img {
        width: 110px;
        height: 110px;
        box-shadow: 0 0 15px rgba(128, 0, 255, 0.6);
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 3])
img_base64 = get_base64_image("P5.jpg")

with col1:
    st.markdown(
        f"""
        <div class="profile-img">
            <img src="data:image/jpeg;base64,{img_base64}">
        </div>
        """,
        unsafe_allow_html=True
    )



with col2:
    st.title("👨‍💻 Anjani Kumar Pokhrel")
    st.subheader("AI / Machine Learning Intern | Data Analyst")
    st.write("""
📍 Kathmandu, Nepal  
📧 anjanpokhrel580@gmail.com  
📞 9869879472  
🔗 [LinkedIn](https://www.linkedin.com/in/anjan-pokhrel/)  
💻 [GitHub](https://github.com/Anjan580)
""")

# ---------------- RESUME DOWNLOAD ----------------
with open("Anjani Kumar Pokhrel_CV.pdf", "rb") as file:
    st.download_button(
        "📄 Download Resume",
        file,
        file_name="Anjani Kumar Pokhrel_CV.pdf",
        mime="application/pdf"
    )

st.divider()

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["🙋 About", "📂 Projects", "📬 Contact"])

# ================= ABOUT TAB =================
with tab1:
    st.header("🎯 Career Objective")
    st.write("""
    Seeking an **AI/ML internship** to apply my data analysis and machine learning skills,
    gain real-world experience, and grow under professional mentorship.
    """)

    st.header("🛠️ Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Technical Skills**
        - Data Analysis & Visualization: Excel, Tableau, Power BI  
        - Programming: Python (Pandas, NumPy, Scikit-learn, PyTorch)  
        - Databases: MySQL, PostgreSQL, SQL Server  
        - Statistics: Hypothesis Testing, Probability
        """)

    with col2:
        st.markdown("""
        **Tools & Soft Skills**
        - Tools: Git, GitHub, VS Code, Jupyter, Streamlit, FastAPI  
        - Soft Skills: Problem-Solving, Communication, Critical Thinking
        """)

    st.header("🎓 Education")
    st.write("""
    **Bachelor’s in Computer Science & Information Technology**  
    Trinity International College, Dillibazar  
    2022 – Present
    """)

    st.header("📘 Training")
    st.write("""
    **Data Science with Python**  
    Broadway Infosys Nepal (May – Aug 2025)  
    ✔ 135 hours hands-on training
    """)

# ================= PROJECTS TAB =================
with tab2:
    st.header("📂 Projects")

    with st.expander("📰 Fake News Detection"):
        st.write("""
        **Tech:** Python, Scikit-learn, NLTK  
        ✔ Logistic Regression model  
        ✔ ~96% accuracy  
        🔗 https://github.com/Anjan580/Fake_News_Detection_by_using-_logisticRegression
        """)

    with st.expander("📈 Gold Price Prediction"):
        st.write("""
        **Tech:** Python  
        ✔ Regression-based forecasting  
        🔗 https://github.com/Anjan580/Gold-Price-Prediction-using-Machine-Learning
        """)

    with st.expander("👥 HR Analytics Dashboard"):
        st.write("""
        **Tech:** Power BI  
        ✔ KPIs, Attrition & Workforce Analysis  
        🔗 https://github.com/Anjan580/HR_Analytics_dashboard_power_BI
        """)

# ================= CONTACT TAB =================
with tab3:
    st.header("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("Thank you! I will get back to you soon 😊")

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2025 Anjani Kumar Pokhrel | Built with Streamlit 🚀")
