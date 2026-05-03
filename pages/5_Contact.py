import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_glass_card,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Contact | Rena Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Contact", "Reach out for collaboration, projects, or opportunities", "mail")

st.title("Contact")

left, right = st.columns(2, gap="large")
with left:
    render_glass_card(f"""
        <h3>Direct Info</h3>
        <p style="display:flex;align-items:center;gap:6px;">{get_icon('phone',16)} 09706394552</p>
        <p style="display:flex;align-items:center;gap:6px;">{get_icon('mail',16)} Valenzuelarenaa934@gmail.com</p>
        <p style="display:flex;align-items:center;gap:6px;margin-bottom:0;">{get_icon('map_pin',16)} Bugtong, Mandaon, Masbate</p>
    """, icon_name="phone")

with right:
    render_glass_card(f"""
        <h3>Profiles</h3>
        <div style="display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.5rem;">
            <a class="social-link" href="https://facebook.com/rena.bensurto" target="_blank">{get_icon('external_link',14)} Facebook</a>
        </div>
    """, icon_name="link")
