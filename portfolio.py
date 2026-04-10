import base64
import re
from pathlib import Path

import requests
import streamlit as st

PAGE_TITLE = "Anjani Kumar Pokhrel | Portfolio"
PAGE_ICON = ":briefcase:"
EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
BASE_DIR = Path(__file__).resolve().parent
PROFILE_IMAGE = BASE_DIR / "P5.jpg"
RESUME_FILE = BASE_DIR / "Anjani Kumar Pokhrel_CV.pdf"
FORMSPREE_ENDPOINT = "https://formspree.io/f/mykdjywe"

PROFILE = {
    "name": "Anjani Kumar Pokhrel",
    "title": "Data Analyst Intern at Foodmandu",
    "tagline": "Machine Learning and Data Science enthusiast building practical, data-driven solutions.",
    "location": "Kathmandu, Nepal",
    "email": "anjanpokhrel580@gmail.com",
    "phone": "+977 9869879472",
    "linkedin": "https://www.linkedin.com/in/anjan-pokhrel/",
    "github": "https://github.com/Anjan580",
    "objective": (
        "Aspiring AI and Machine Learning professional with hands-on experience in data analysis, "
        "visualization, and statistical modeling. I enjoy turning messy data into clear business "
        "insights and building ML projects that solve real problems."
    ),
}

SKILLS = {
    "Data & BI": ["Excel", "Power BI", "Tableau", "SQL"],
    "Programming": ["Python", "Pandas", "NumPy", "Scikit-learn", "TensorFlow"],
    "Databases": ["MySQL", "PostgreSQL", "SQL Server"],
    "Workflow": ["Git", "GitHub", "Jupyter", "VS Code", "Streamlit", "FastAPI"],
    "Core Strengths": ["EDA", "Visualization", "Hypothesis Testing", "Communication"],
}

HIGHLIGHTS = [
    ("Projects", "8+"),
    ("Focus", "AI / ML"),
    ("Current Role", "Foodmandu"),
]

PROJECTS = [
    {
        "title": "Fake News Detection",
        "tech": "Python, Scikit-learn, NLTK",
        "summary": "Built a logistic regression classifier for fake news detection with about 96% accuracy.",
        "link": "https://github.com/Anjan580/Fake_News_Detection_by_using-_logisticRegression",
    },
    {
        "title": "Gold Price Prediction",
        "tech": "Python, Regression Modeling",
        "summary": "Created a regression-based forecasting workflow for gold price prediction.",
        "link": "https://github.com/Anjan580/Gold-Price-Prediction-using-Machine-Learning",
    },
    {
        "title": "HR Analytics Dashboard",
        "tech": "Power BI",
        "summary": "Designed KPI dashboards focused on attrition, workforce trends, and HR decision support.",
        "link": "https://github.com/Anjan580/HR_Analytics_dashboard_power_BI",
    },
    {
        "title": "Customer Segmentation Using K-Means",
        "tech": "Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn",
        "summary": "Segmented customers using clustering and the elbow method to uncover actionable business insights.",
        "link": "https://github.com/Anjan580/Customer-Segmentation-using-K-Means-Clustering",
    },
    {
        "title": "Foodmandu-Style Order Performance Dashboard",
        "tech": "Power BI, DAX, Data Modeling",
        "summary": "Built an interactive portfolio dashboard around orders, revenue, AOV, and customer insights using synthetic data.",
        "link": "https://github.com/Anjan580/Foodmandu-Order-Performance-Dashboard",
    },
    {
        "title": "Superstore Sales Dashboard",
        "tech": "Power BI, DAX, Data Visualization",
        "summary": "Explored sales, profit, and category-region performance through a clean decision-making dashboard.",
        "link": "https://github.com/Anjan580/Super-Store-dashboard",
    },
    {
        "title": "Wine Quality Prediction",
        "tech": "Python, Pandas, NumPy, Scikit-learn",
        "summary": "Ran EDA, preprocessing, feature selection, and classification to predict wine quality.",
        "link": "https://github.com/Anjan580/Wine-Quality-Prediction-using-Machine-Learning",
    },
    {
        "title": "Sonar Rock vs Mine Classification",
        "tech": "Python, Pandas, NumPy, Scikit-learn, Matplotlib",
        "summary": "Implemented an end-to-end ML pipeline with evaluation metrics and model generalization analysis.",
        "link": "https://github.com/Anjan580/-SONAR-Rock-vs-Mine-Prediction",
    },
]

EDUCATION = {
    "degree": "Bachelor's in Computer Science and Information Technology",
    "institution": "Trinity International College, Dillibazar, Kathmandu",
    "period": "2022 - 2026",
}

TRAINING = {
    "program": "Data Science with Python",
    "provider": "Broadway Infosys Nepal",
    "period": "May 2025 - August 2025",
    "details": "135 hours of hands-on training in Python-based data science workflows.",
}


def load_base64_image(image_path: Path) -> str:
    with image_path.open("rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


@st.cache_data(show_spinner=False)
def load_resume_bytes() -> bytes:
    return RESUME_FILE.read_bytes()


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email.strip()))


def send_message(name: str, email: str, message: str) -> tuple[bool, str]:
    try:
        response = requests.post(
            FORMSPREE_ENDPOINT,
            data={"name": name.strip(), "email": email.strip(), "message": message.strip()},
            timeout=10,
        )
    except requests.RequestException:
        return False, "Couldn't reach the contact service. Please try again in a moment."

    if response.ok:
        return True, "Message sent successfully. I'll get back to you soon."

    return False, "Something went wrong while sending the message. Please try again later."


def inject_styles() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #081120;
                --surface: rgba(12, 23, 41, 0.82);
                --surface-strong: #0f1b30;
                --text: #e8eef9;
                --muted: #a8b6cc;
                --accent: #38bdf8;
                --accent-2: #22c55e;
                --border: rgba(148, 163, 184, 0.16);
                --shadow: 0 18px 45px rgba(2, 8, 23, 0.34);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(56, 189, 248, 0.18), transparent 28%),
                    radial-gradient(circle at top right, rgba(34, 197, 94, 0.16), transparent 30%),
                    linear-gradient(180deg, #081120 0%, #0f172a 55%, #131c31 100%);
                color: var(--text);
            }

            .block-container {
                padding-top: 2.4rem;
                padding-bottom: 2rem;
            }

            h1, h2, h3 {
                color: var(--text);
                letter-spacing: -0.02em;
            }

            p, li, label, .stMarkdown, .stCaption {
                color: var(--muted);
            }

            .hero-card,
            .info-card,
            .project-card,
            .contact-card {
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: 24px;
                box-shadow: var(--shadow);
                backdrop-filter: blur(10px);
            }

            .hero-card {
                padding: 1.7rem;
                min-height: 100%;
            }

            .hero-layout {
                display: flex;
                align-items: flex-start;
                gap: 1.5rem;
            }

            .hero-copy {
                flex: 1;
            }

            .hero-chip {
                display: inline-block;
                padding: 0.35rem 0.8rem;
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.14);
                color: #7dd3fc;
                font-size: 0.9rem;
                font-weight: 600;
                margin-bottom: 0.9rem;
            }

            .hero-title {
                font-size: clamp(2.1rem, 4vw, 3.5rem);
                line-height: 1.03;
                margin-bottom: 0.35rem;
                color: var(--text);
            }

            .hero-subtitle {
                font-size: 1.15rem;
                color: #86efac;
                margin-bottom: 1rem;
                font-weight: 600;
            }

            .hero-description {
                font-size: 1rem;
                line-height: 1.7;
                margin-bottom: 1rem;
            }

            .contact-list {
                display: grid;
                gap: 0.45rem;
                margin: 1rem 0 0;
            }

            .contact-list a {
                color: var(--accent-2);
                text-decoration: none;
                font-weight: 600;
            }

            .profile-wrap {
                display: flex;
                justify-content: flex-start;
                align-items: flex-start;
                padding: 0;
                position: relative;
                overflow: visible;
                flex: 0 0 auto;
            }

            .profile-ring {
                width: min(220px, 42vw);
                aspect-ratio: 1;
                border-radius: 28px;
                padding: 10px;
                background: linear-gradient(135deg, #38bdf8, #2563eb, #22c55e);
                box-shadow: 0 22px 55px rgba(2, 8, 23, 0.42);
                transform: rotate(-3deg);
                position: relative;
                animation: floatPortrait 5s ease-in-out infinite;
                transition: transform 0.35s ease, box-shadow 0.35s ease;
            }

            .profile-ring::before,
            .profile-ring::after {
                content: "";
                position: absolute;
                inset: -14px;
                border-radius: 36px;
                z-index: -1;
            }

            .profile-ring::before {
                background: linear-gradient(135deg, rgba(56, 189, 248, 0.26), rgba(34, 197, 94, 0.16));
                filter: blur(12px);
            }

            .profile-ring::after {
                inset: auto;
                width: 72%;
                height: 72%;
                right: -18px;
                bottom: -18px;
                border-radius: 30px;
                background:
                    radial-gradient(circle at center, rgba(37, 99, 235, 0.32), transparent 65%);
            }

            .profile-ring img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: 22px;
                display: block;
                transform: rotate(3deg);
                filter: saturate(1.08) contrast(1.04);
            }

            .profile-ring:hover {
                transform: rotate(-1deg) translateY(-6px) scale(1.02);
                box-shadow: 0 28px 70px rgba(2, 8, 23, 0.52);
            }

            .photo-badge {
                position: absolute;
                left: -8px;
                bottom: 18px;
                padding: 0.6rem 0.95rem;
                border-radius: 999px;
                background: rgba(15, 23, 42, 0.94);
                border: 1px solid rgba(125, 211, 252, 0.18);
                box-shadow: 0 16px 32px rgba(2, 8, 23, 0.24);
                color: var(--text);
                font-size: 0.88rem;
                font-weight: 700;
                letter-spacing: 0.01em;
            }

            .photo-badge span {
                display: block;
                font-size: 0.78rem;
                font-weight: 600;
                color: var(--muted);
                margin-top: 0.15rem;
            }

            @keyframes floatPortrait {
                0%,
                100% {
                    transform: rotate(-3deg) translateY(0px);
                }
                50% {
                    transform: rotate(-2deg) translateY(-8px);
                }
            }

            .highlight-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.9rem;
                margin-top: 1rem;
            }

            .info-card,
            .project-card,
            .contact-card {
                padding: 1.15rem 1.2rem;
                margin-bottom: 1rem;
            }

            .metric-label {
                font-size: 0.85rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                color: var(--muted);
                margin-bottom: 0.25rem;
            }

            .metric-value {
                font-size: 1.15rem;
                font-weight: 700;
                color: var(--text);
            }

            .skill-pill {
                display: inline-block;
                margin: 0.2rem 0.35rem 0.2rem 0;
                padding: 0.36rem 0.75rem;
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.14);
                color: #93c5fd;
                font-size: 0.9rem;
                font-weight: 600;
            }

            .section-label {
                font-size: 0.8rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.09em;
                color: var(--accent);
                margin-bottom: 0.55rem;
            }

            .project-title {
                color: var(--text);
                font-size: 1.1rem;
                font-weight: 700;
                margin-bottom: 0.3rem;
            }

            .project-tech {
                color: #7dd3fc;
                font-size: 0.92rem;
                font-weight: 600;
                margin-bottom: 0.55rem;
            }

            .project-link a {
                color: var(--accent-2);
                font-weight: 700;
                text-decoration: none;
            }

            .stDownloadButton button,
            .stFormSubmitButton button {
                border-radius: 999px;
                border: none;
                background: linear-gradient(135deg, #0ea5e9, #2563eb);
                color: white;
                font-weight: 700;
                padding: 0.6rem 1.2rem;
            }

            .stTextInput input,
            .stTextArea textarea {
                border-radius: 16px;
                border: 1px solid rgba(148, 163, 184, 0.18);
                background: rgba(15, 23, 42, 0.72);
                color: var(--text);
            }

            @media (max-width: 900px) {
                .hero-layout {
                    flex-direction: column;
                }

                .highlight-grid {
                    grid-template-columns: 1fr;
                }

                .hero-card,
                .profile-wrap {
                    padding: 1.2rem;
                }

                .profile-wrap {
                    padding: 0;
                }

                .profile-ring {
                    width: min(220px, 58vw);
                }

                .photo-badge {
                    left: 12px;
                    bottom: 12px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
inject_styles()

image_base64 = load_base64_image(PROFILE_IMAGE)
resume_bytes = load_resume_bytes()

st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-layout">
                <div class="profile-wrap">
                    <div class="profile-ring">
                        <img src="data:image/jpeg;base64,{image_base64}" alt="Profile photo of {PROFILE['name']}">
                    </div>
                    <div class="photo-badge">
                        Data + ML
                        <span>Open to opportunities</span>
                    </div>
                </div>
                <div class="hero-copy">
            <div class="hero-chip">Open to internships and data roles</div>
            <div class="hero-title">{PROFILE['name']}</div>
            <div class="hero-subtitle">{PROFILE['title']}</div>
            <div class="hero-description">{PROFILE['tagline']}</div>
            <div class="hero-description">{PROFILE['objective']}</div>
            <div class="contact-list">
                <span>Location: {PROFILE['location']}</span>
                <span>Email: <a href="mailto:{PROFILE['email']}">{PROFILE['email']}</a></span>
                <span>Phone: {PROFILE['phone']}</span>
                <span>Links: <a href="{PROFILE['linkedin']}" target="_blank">LinkedIn</a> | <a href="{PROFILE['github']}" target="_blank">GitHub</a></span>
            </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
)

st.download_button(
    "Download Resume",
    resume_bytes,
    file_name=RESUME_FILE.name,
    mime="application/pdf",
)

st.markdown('<div class="highlight-grid">' + ''.join(
    f'<div class="info-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>'
    for label, value in HIGHLIGHTS
) + '</div>', unsafe_allow_html=True)

about_tab, projects_tab, contact_tab = st.tabs(["About", "Projects", "Contact"])

with about_tab:
    st.subheader("Skills")
    skill_columns = st.columns(2)
    for index, (category, entries) in enumerate(SKILLS.items()):
        with skill_columns[index % 2]:
            pills = "".join(f'<span class="skill-pill">{skill}</span>' for skill in entries)
            st.markdown(
                f"""
                <div class="info-card">
                    <div class="section-label">{category}</div>
                    <div>{pills}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    edu_col, train_col = st.columns(2, gap="large")

    with edu_col:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="section-label">Education</div>
                <div class="metric-value">{EDUCATION['degree']}</div>
                <p><strong>{EDUCATION['institution']}</strong><br>{EDUCATION['period']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with train_col:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="section-label">Training</div>
                <div class="metric-value">{TRAINING['program']}</div>
                <p><strong>{TRAINING['provider']}</strong><br>{TRAINING['period']}</p>
                <p>{TRAINING['details']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with projects_tab:
    st.subheader("Selected Work")
    project_columns = st.columns(2, gap="large")
    for index, project in enumerate(PROJECTS):
        with project_columns[index % 2]:
            st.markdown(
                f"""
                <div class="project-card">
                    <div class="project-title">{project['title']}</div>
                    <div class="project-tech">{project['tech']}</div>
                    <p>{project['summary']}</p>
                    <div class="project-link"><a href="{project['link']}" target="_blank">View project</a></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

with contact_tab:
    st.markdown(
        """
        <div class="contact-card">
            <div class="section-label">Let's Connect</div>
            <p>If you would like to discuss internships, data projects, or collaboration opportunities, send a message here.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message", height=160, placeholder="Write a short message...")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            clean_name = name.strip()
            clean_email = email.strip()
            clean_message = message.strip()

            if not clean_name or not clean_email or not clean_message:
                st.warning("Please fill in all fields before sending your message.")
            elif not is_valid_email(clean_email):
                st.warning("Please enter a valid email address.")
            else:
                with st.spinner("Sending message..."):
                    success, response_message = send_message(clean_name, clean_email, clean_message)

                if success:
                    st.success(response_message)
                else:
                    st.error(response_message)

st.caption("(c) 2026 Anjani Kumar Pokhrel | Built with Streamlit")
