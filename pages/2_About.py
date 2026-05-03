import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_glass_card,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="About | Rena Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("About Rena", "Profile and personal background", "user")

st.title("About")

render_glass_card(
    """
    <h3>About Me</h3>
    <p>
        I enjoy creating simple and useful projects that can help solve everyday problems.
        I like learning new skills and exploring different ways to improve my work through
        practice and experience.
    </p>
    <p>
        I am passionate about turning ideas into something functional and meaningful.
        Every project gives me a chance to grow, be creative, and gain more knowledge
        along the way.
    </p>
    """,
    icon_name="terminal",
)

info_left, info_right = st.columns(2, gap="large")
with info_left:
    render_glass_card(f"""
        <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('mail',16)} <strong>Email:</strong></span> Valenzuelarenaa934@gmail.com</p>
        <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('phone',16)} <strong>Phone:</strong></span> 09706394552</p>
    """)
with info_right:
    render_glass_card(f"""
        <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('map_pin',16)} <strong>Address:</strong></span> Bugtong, Mandaon, Masbate</p>
        <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('book',16)} <strong>Interests:</strong></span> Reading books, studying, and watching K-Drama</p>
    """)

render_divider()

render_section_header("Interests", "layers")
interests = st.multiselect(
    "Core interests",
    ["Reading Books", "Studying", "Watching K-Drama"],
    default=["Reading Books", "Studying", "Watching K-Drama"],
)
st.write("Selected:", ", ".join(interests))

render_divider()

render_section_header("Journey", "calendar")
edu_tab, exp_tab, cert_tab = st.tabs(["Education", "Focus", "Goals"])

with edu_tab:
    render_glass_card(f"""
        <h3>Education</h3>
        <p><span class="status-dot"></span> Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology</p>
        <p>Bugtong National High School</p>
    """, icon_name="book")

    render_glass_card("""
        <h3>Learning Style</h3>
        <p>Hands-on, consistent, and reflective practice.</p>
        <p>Improving step by step through small goals and routine effort.</p>
    """, icon_name="book")

with exp_tab:
    render_glass_card("""
        <h3>Current Focus</h3>
        <p>Reading books to expand perspective and understanding.</p>
        <p>Studying regularly to build strong academic habits.</p>
        <p>Watching K-Drama as a way to relax and stay inspired.</p>
    """, icon_name="award")
    st.write("- Developing consistency and patience")
    st.write("- Learning from stories, lessons, and experiences")
    st.write("- Staying motivated through meaningful goals")

with cert_tab:
    render_glass_card("""
        <h3>Personal Goals</h3>
        <p>Keep learning, stay curious, and become better each day.</p>
    """, icon_name="check_circle")
