import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_glass_card,
    render_info_card,
    render_interest_card_html,
    render_section_header,
    render_theme_controls,
    render_typing_hero,
    set_page_style,
)

st.set_page_config(page_title="Home | Rena Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)

# Hero
render_typing_hero(
    "Rena",
    "Computer Science Student  ·  Bugtong, Mandaon, Masbate",
)

st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

# Quick stats
sp_left, center_col, sp_right = st.columns([1, 2, 1])
with center_col:
    st.metric("Focus", "Reading and Studying")

render_divider()

# Interests
render_section_header("Interests", "layers")

cols = st.columns(3)
cols[0].markdown(
    render_interest_card_html("code", "Programming", "Building practical systems with clean logic."),
    unsafe_allow_html=True,
)
cols[1].markdown(
    render_interest_card_html("book", "Reading Books", "Enjoying stories and learning through books in my free time."),
    unsafe_allow_html=True,
)
cols[2].markdown(
    render_interest_card_html("message_circle", "Watching K-Drama", "Relaxing with character-driven stories and Korean drama series."),
    unsafe_allow_html=True,
)

render_divider()

# Explore
render_section_header("Explore This App", "arrow_right")

choice = st.radio(
    "What do you want to check first?",
    ["Projects", "Skills", "About and Experience", "Contact"],
    horizontal=True,
)

explore_map = {
    "Projects":             ("folder",    "Open the Projects page to view live links and project categories."),
    "Skills":               ("tool",      "Open the Skills page to view languages, databases, and libraries."),
    "About and Experience": ("user",      "Open the About page for education timeline and achievements."),
    "Contact":              ("mail",      "Open Contact for direct details and message form."),
}

icon_name, msg = explore_map[choice]
render_info_card(icon_name, f'<span style="color:var(--muted);font-size:.93rem;">{msg}</span>')
