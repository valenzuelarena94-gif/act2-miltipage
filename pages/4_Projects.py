import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Projects | Rena Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Projects", "GitHub profile and repositories", "folder")

st.title("Projects")

projects = [
    {
        "name": "GitHub Profile",
        "cat": "Profile",
        "desc": "Visit the GitHub account to see repositories, projects, and updates.",
        "link": "https://github.com/",
        "icon": "github",
    },
]

filter_col, search_col = st.columns([1, 2], gap="small")
with filter_col:
    category = st.selectbox("Category", ["All", "Profile"])
with search_col:
    keyword = st.text_input("Search project name")

st.caption("Compact view · quick scan + one-click open")

idx = 0
for item in projects:
    if category != "All" and item["cat"] != category:
        continue
    if keyword and keyword.lower() not in item["name"].lower():
        continue

    icon_svg = get_icon(item["icon"], 20)
    left, right = st.columns([5, 1], gap="small", vertical_alignment="center")
    with left:
        from ui import _clean_html
        st.markdown(_clean_html(f"""
        <div class="project-row reveal" style="transition-delay:{idx * .07}s;">
            <div class="proj-icon">{icon_svg}</div>
            <div class="proj-body">
                <h4>{item['name']}</h4>
                <p>{item['desc']}</p>
                <span class="chip">{get_icon('hash', 12)} {item['cat']}</span>
            </div>
        </div>
        """), unsafe_allow_html=True)
    with right:
        st.link_button("Open", item["link"], use_container_width=True)
    idx += 1

render_divider()

with st.expander("Project Poll"):
    render_section_header("Vote", "check_circle")
    poll_col, _ = st.columns([1, 1])
    next_to_improve = poll_col.selectbox(
        "Which area should be updated next?",
        [p["name"] for p in projects],
    )
    if poll_col.button("Submit Vote"):
        poll_col.success(f"Vote received: {next_to_improve}")
