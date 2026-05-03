import streamlit as st
import streamlit.components.v1 as components
from typing import Dict, Optional

ICONS: Dict[str, str] = {
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "shield": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "globe": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10A15.3 15.3 0 0 1 12 2z"/></svg>',
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
    "user": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "folder": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>',
    "tool": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "map_pin": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "calendar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "external_link": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
    "github": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.565 21.796 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>',
    "terminal": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>',
    "database": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "layout": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>',
    "server": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>',
    "award": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
    "send": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>',
    "zap": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
    "briefcase": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "link": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
    "arrow_right": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "layers": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "clipboard": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
    "bar_chart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
    "camera": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
    "message_circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    "gamepad": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/><line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/><rect x="2" y="6" width="20" height="12" rx="2"/></svg>',
    "dollar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "hash": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>',
    "check_circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
}


def get_icon(name: str, size: int = 24) -> str:
    svg = ICONS.get(name, "")
    if size != 24:
        svg = svg.replace('width="24"', f'width="{size}"').replace('height="24"', f'height="{size}"')
    return svg


def render_theme_controls() -> str:
    st.session_state.theme_mode = "Night Rose"
    return "Night Rose"


def _palette(light: bool) -> Dict[str, str]:
    if light:
        return {
            "bg": "#fff4f8",
            "surface": "#fffafd",
            "card": "rgba(255,250,253,.90)",
            "text": "#3a2430",
            "muted": "#7d5a6b",
            "border": "#f0d8e5",
            "accent": "#d14f87",
            "accent2": "#f18bb8",
            "accent_subtle": "rgba(209,79,135,.12)",
            "shadow": "rgba(128,44,85,.10)",
            "shadow_hover": "rgba(128,44,85,.18)",
            "nav_text": "#5e3b4c",
            "nav_hover": "#ffeef5",
            "nav_active": "#ffddea",
            "input_bg": "#fff9fc",
            "input_text": "#3a2430",
            "button_bg": "#d14f87",
            "button_text": "#ffffff",
        }
    return {
        "bg": "#1e141a",
        "surface": "#281c24",
        "card": "rgba(40,28,36,.86)",
        "text": "#ffe8f1",
        "muted": "#d0a7bd",
        "border": "#4b3040",
        "accent": "#ff75ad",
        "accent2": "#ff9cc5",
        "accent_subtle": "rgba(255,117,173,.14)",
        "shadow": "rgba(0,0,0,.30)",
        "shadow_hover": "rgba(0,0,0,.52)",
        "nav_text": "#ffd7e8",
        "nav_hover": "#342431",
        "nav_active": "#432c3b",
        "input_bg": "#2a1c26",
        "input_text": "#ffe8f1",
        "button_bg": "#ff75ad",
        "button_text": "#1e141a",
    }


def set_page_style(mode: str) -> None:
    is_light = mode == "Rose"
    p = _palette(is_light)
    st.markdown(
        f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {{
    --bg:{p['bg']};--surface:{p['surface']};--card:{p['card']};--text:{p['text']};--muted:{p['muted']};
    --border:{p['border']};--accent:{p['accent']};--accent2:{p['accent2']};--accent-subtle:{p['accent_subtle']};
    --shadow:{p['shadow']};--shadow-hover:{p['shadow_hover']};--navtext:{p['nav_text']};--navhover:{p['nav_hover']};
    --navactive:{p['nav_active']};--inputbg:{p['input_bg']};--inputtext:{p['input_text']};--buttonbg:{p['button_bg']};
    --buttontext:{p['button_text']};
}}

.stApp {{
    background: radial-gradient(1000px 400px at 95% 2%, rgba(241,139,184,.18), transparent 50%),
                radial-gradient(800px 340px at 5% 100%, rgba(209,79,135,.16), transparent 52%),
                var(--bg);
    color: var(--text);
    font-family: 'Manrope', sans-serif;
}}

#MainMenu, footer, [data-testid="stHeader"] {{ visibility:hidden; }}

.stApp h1,.stApp h2,.stApp h3 {{ font-family:'Playfair Display', serif; color:var(--text); letter-spacing:.1px; }}
.stApp p,.stApp li,.stApp label,.stApp span {{ font-family:'Manrope', sans-serif; }}

[data-testid="stSidebar"] {{ background: var(--surface); border-right:1px solid var(--border); }}
[data-testid="stSidebarNavLink"] a {{ color:var(--navtext)!important; border-radius:10px; }}
[data-testid="stSidebarNavLink"] a:hover {{ background:var(--navhover)!important; }}
[data-testid="stSidebarNavLink"][aria-current="page"] a {{ background:var(--navactive)!important; font-weight:700; }}

.topbar,.glass-card,.project-row,.info-card,div[data-testid="stMetric"] {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    box-shadow: 0 4px 20px var(--shadow);
    backdrop-filter: blur(10px);
}}

.topbar {{ display:flex;gap:.8rem;align-items:center;padding:1rem 1.2rem;margin-bottom:1rem; }}
.topbar-icon,.sh-icon,.ic-icon,.proj-icon,.card-icon-badge {{ color:var(--accent); }}
.topbar strong {{ font-size:1.04rem; }}
.topbar p {{ margin:.2rem 0 0;color:var(--muted);font-size:.88rem; }}

.hero-section {{ padding:1.4rem 0 .8rem; }}
.hero-section {{
    text-align:center;
    max-width:980px;
    margin:0 auto;
}}
.typing-text,.hero-title-static {{
    font-family:'Playfair Display', serif;
    font-size:clamp(2.1rem,5vw,3.25rem);
    font-weight:700;
    line-height:1.12;
    letter-spacing:.2px;
}}
.hero-subtitle,.hero-subtitle-static {{
    margin-top:.55rem;
    color:var(--muted);
    font-size:1.02rem;
    font-weight:500;
    letter-spacing:.1px;
    text-align:center;
}}
.typing-text {{
    overflow:hidden;white-space:nowrap;display:inline-block;border-right:2px solid var(--accent);max-width:0;
    animation: typing 1.5s steps(14, end) .3s forwards, blink .8s step-end infinite;
}}
@keyframes typing {{ from {{ max-width:0; }} to {{ max-width:100%; }} }}
@keyframes blink {{ 50% {{ border-right-color:transparent; }} }}

.glass-card {{ padding:1.2rem;margin-bottom:.9rem;transition:.25s ease; }}
.glass-card:hover,.project-row:hover,.info-card:hover,div[data-testid="stMetric"]:hover {{ transform:translateY(-2px); box-shadow:0 8px 24px var(--shadow-hover); }}
.card-icon-badge,.proj-icon {{ width:42px;height:42px;border-radius:12px;background:var(--accent-subtle);display:flex;align-items:center;justify-content:center;margin-bottom:.7rem; }}

.section-hdr {{ display:flex;align-items:center;gap:.6rem;margin:1.4rem 0 .9rem; }}
.section-hdr h2 {{ margin:0;font-size:1.35rem; }}

.chip {{ display:inline-flex;align-items:center;gap:.35rem;padding:.32rem .8rem;border-radius:999px;border:1px solid var(--border);background:var(--surface);font-size:.82rem;font-weight:600; }}

.skill-bar {{ margin-bottom:1rem; }}
.skill-bar-header {{ display:flex;justify-content:space-between;margin-bottom:.35rem; }}
.skill-bar-track {{ background:var(--border);height:9px;border-radius:999px;overflow:hidden; }}
.skill-bar-fill {{ background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;width:0;animation:fillBar 1.2s ease .2s forwards; }}
@keyframes fillBar {{ from {{ width:0; }} to {{ width:var(--bar-w); }} }}

.project-row {{ display:flex;gap:.8rem;align-items:flex-start;padding:1rem;margin-bottom:.7rem; }}
.project-row h4 {{ margin:0 0 .2rem; }}
.project-row p {{ margin:0 0 .45rem;color:var(--muted);font-size:.9rem; }}

.info-card {{ display:flex;gap:.7rem;align-items:center;padding:1rem; }}

.social-link {{ display:inline-flex;align-items:center;gap:.4rem;padding:.35rem .7rem;border-radius:10px;border:1px solid var(--border);text-decoration:none;color:var(--text); }}
.social-link:hover {{ border-color:var(--accent);color:var(--accent); }}

.stButton > button,[data-testid="stFormSubmitButton"] > button,[data-testid="stLinkButton"] a {{
    border-radius:12px!important;border:1px solid var(--border)!important;background:var(--buttonbg)!important;
    color:var(--buttontext)!important;font-weight:700!important;box-shadow:0 4px 14px var(--shadow)!important;
}}

.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"] > div {{
    border-radius:10px!important;border:1px solid var(--border)!important;background:var(--inputbg)!important;color:var(--inputtext)!important;
}}

.styled-hr {{ border:none;height:1px;background:var(--border);margin:1.6rem 0 1.2rem; }}
.status-dot {{ display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;background:var(--accent); }}

/* Metric typography refinement */
div[data-testid="stMetricLabel"] {{
    font-family:'Manrope', sans-serif!important;
    font-size:.92rem!important;
    font-weight:600!important;
    letter-spacing:.1px!important;
    text-align:center!important;
    justify-content:center!important;
}}
div[data-testid="stMetricValue"] {{
    font-family:'Manrope', sans-serif!important;
    font-size:2.2rem!important;
    font-weight:700!important;
    line-height:1.25!important;
    letter-spacing:.1px!important;
    text-align:center!important;
}}

@media (max-width:768px) {{
    .topbar,.glass-card,.project-row,.info-card {{ border-radius:12px; }}
}}
</style>
""",
        unsafe_allow_html=True,
    )
    _inject_scroll_observer()


def _inject_scroll_observer() -> None:
    components.html(
        """
<script>
(function(){
    const doc = window.parent.document;
    const ob = new IntersectionObserver((entries)=>{
        entries.forEach(e=>{ if (e.isIntersecting) e.target.classList.add('revealed'); });
    }, {threshold:0.12});
    doc.querySelectorAll('.reveal').forEach(el=>ob.observe(el));
    const mo = new MutationObserver(()=>{
        doc.querySelectorAll('.reveal:not(.revealed)').forEach(el=>ob.observe(el));
    });
    mo.observe(doc.body, {childList:true, subtree:true});
})();
</script>
        """,
        height=0,
    )


def _clean_html(html_str: str) -> str:
    import re
    return re.sub(r'^\\s+', '', html_str, flags=re.MULTILINE).strip()


def render_topbar(title: str, subtitle: str, icon_name: str = "zap") -> None:
    st.markdown(_clean_html(f"""
    <div class="topbar reveal">
        <div class="topbar-icon">{get_icon(icon_name, 22)}</div>
        <div class="topbar-body"><strong>{title}</strong><p>{subtitle}</p></div>
    </div>
    """), unsafe_allow_html=True)


def render_typing_hero(name: str, subtitle: str) -> None:
    played = st.session_state.get("_typing_played", False)
    if not played:
        st.session_state["_typing_played"] = True
        st.markdown(_clean_html(f"""
        <div class="hero-section">
            <div><span class="typing-text">Hello, I am {name}</span></div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """), unsafe_allow_html=True)
    else:
        st.markdown(_clean_html(f"""
        <div class="hero-section">
            <div class="hero-title-static">Hello, I am {name}</div>
            <div class="hero-subtitle-static">{subtitle}</div>
        </div>
        """), unsafe_allow_html=True)


def render_section_header(text: str, icon_name: str = "hash") -> None:
    st.markdown(_clean_html(f"""
    <div class="section-hdr reveal"><div class="sh-icon">{get_icon(icon_name, 20)}</div><h2>{text}</h2></div>
    """), unsafe_allow_html=True)


def render_glass_card(content_html: str, icon_name: Optional[str] = None) -> None:
    icon_block = ""
    if icon_name:
        icon_block = '<div class="card-icon-badge">' + get_icon(icon_name, 20) + '</div>'
    st.markdown(_clean_html(f"""
    <div class="glass-card reveal">{icon_block}{_clean_html(content_html)}</div>
    """), unsafe_allow_html=True)


def render_interest_card_html(icon_name: str, title: str, desc: str) -> str:
    return _clean_html(f"""
    <div class="glass-card reveal"><div class="card-icon-badge">{get_icon(icon_name,22)}</div><h3>{title}</h3><p>{desc}</p></div>
    """)


def render_skill_bar(label: str, value: int, icon_name: str = "zap") -> None:
    st.markdown(_clean_html(f"""
    <div class="skill-bar reveal">
        <div class="skill-bar-header"><span>{get_icon(icon_name,16)} {label}</span><span><strong>{value}%</strong></span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="--bar-w:{value}%;"></div></div>
    </div>
    """), unsafe_allow_html=True)


def render_divider() -> None:
    st.markdown('<hr class="styled-hr">', unsafe_allow_html=True)


def render_info_card(icon_name: str, text_html: str) -> None:
    st.markdown(_clean_html(f"""
    <div class="info-card reveal"><div class="ic-icon">{get_icon(icon_name,20)}</div><div>{_clean_html(text_html)}</div></div>
    """), unsafe_allow_html=True)
