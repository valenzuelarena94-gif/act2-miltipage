import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_info_card,
    render_section_header,
    render_skill_bar,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Skills | Rena Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Skills", "Personal strengths and interests", "tool")

st.title("Skills")

lang_db = [
    ("Reading Books", "book"),
    ("Studying", "check_circle"),
    ("Time Management", "calendar"),
    ("Note Taking", "clipboard"),
    ("Communication", "message_circle"),
    ("Consistency", "award"),
]

frameworks = [
    ("Critical Thinking", "zap"),
    ("Self-Discipline", "shield"),
    ("Curiosity", "arrow_right"),
    ("Creativity", "layers"),
]

render_section_header("Core Strengths", "database")
st.markdown(
    '<div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:1rem;" class="reveal-stagger">'
    + "".join(
        f'<span class="chip reveal">{get_icon(icon, 14)} {name}</span>'
        for name, icon in lang_db
    )
    + "</div>",
    unsafe_allow_html=True,
)

render_section_header("Growth Traits", "layers")
st.markdown(
    '<div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:1rem;" class="reveal-stagger">'
    + "".join(
        f'<span class="chip reveal">{get_icon(icon, 14)} {name}</span>'
        for name, icon in frameworks
    )
    + "</div>",
    unsafe_allow_html=True,
)

render_divider()

render_section_header("Self-assessment", "bar_chart")
focus_col, _ = st.columns([1, 1])
focus = focus_col.selectbox("Pick a focus area", ["Reading Habit", "Study Discipline", "Creative Growth"])

data = {
    "Reading Habit": (90, "book", "Enjoys reading regularly to learn new ideas and expand perspective."),
    "Study Discipline": (88, "check_circle", "Maintains consistent study routines and academic focus."),
    "Creative Growth": (85, "layers", "Explores new ways to improve through reflection and experience."),
}

value, icon, desc = data[focus]
render_skill_bar(focus, value, icon)
render_info_card(icon, f'<span style="font-size:.92rem;">{desc}</span>')

render_divider()

render_section_header("Daily Balance", "zap")
project_kind = st.radio(
    "What supports your growth today?",
    ["Reading Time", "Study Session", "K-Drama Break"],
    horizontal=True,
)

rec = {
    "Reading Time": ("book", "Read a few pages and write one key takeaway."),
    "Study Session": ("check_circle", "Focus for 45 minutes and review your notes after."),
    "K-Drama Break": ("message_circle", "Take a short break, enjoy an episode, then reset your focus."),
}

icon_name, stack = rec[project_kind]
render_info_card(icon_name, f'<strong>Suggested routine:</strong> {stack}')
