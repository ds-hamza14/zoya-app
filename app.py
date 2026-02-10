import streamlit as st
import time
import streamlit.components.v1 as html

# Page Setup
st.set_page_config(page_title="Justice for Zoya", page_icon="🎓", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
    .chat-container { display: flex; flex-direction: column; gap: 10px; padding: 20px; border-radius: 10px; background-color: #f0f2f6; }
    .prof-msg { align-self: flex-start; background-color: #e0e0e0; color: black; padding: 10px; border-radius: 15px 15px 15px 0; max-width: 80%; border: 2px solid red; }
    .zoya-msg { align-self: flex-end; background-color: #0078ff; color: white; padding: 10px; border-radius: 15px 15px 0 15px; max-width: 80%; }
    .grade-card { background-color: #1a1a2e; color: white; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid gold; }
    .big-grade { font-size: 50px; font-weight: bold; color: #e94560; }
    .regret-box { background-color: #ffe6e6; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 5px; margin: 10px 0; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; height: 50px; font-size: 20px; }
    .shayari-box { font-family: 'Urdu Typesetting', 'Noori Nastaliq', serif; font-size: 24px; text-align: center; color: #e94560; padding: 20px; direction: rtl; }
</style>
""", unsafe_allow_html=True)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def next_stage():
    st.session_state.stage += 1
    st.rerun()

# --- SCENE 1: THE RESULT DAY ---
if st.session_state.stage == 0:
    st.title("📅 Result Day: Fall Semester")
    st.subheader("The Group Chat is buzzing...")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("😎 **Irfan**")
        st.write("T&D: **B-**")
        st.caption("Status: 'Thinking about her...'")
        
    with col2:
        st.info("🧐 **Areeba**")
        st.write("T&D: **C+**")
        st.caption("Status: 'Lovesick & Distracted'")
        
    with col3:
        st.error("👑 **Zoya**")
        st.write("T&D: ...")
        st.write("Processing Reality...")

    if st.button("Reveal Zoya's Unfair Grade"):
        next_stage()

# --- SCENE 2: THE REGRET ---
elif st.session_state.stage == 1:
    st.title("💔 The Realization")
    st.subheader("While Zoya was studying, the others were...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif", width=300)
        st.markdown("""<div class="regret-box"><b>Irfan's Internal Monologue:</b><br>"I spent 4 hours a day replying to her stories and got a B-. If I had Zoya's focus, I'd be a topper."</div>""", unsafe_allow_html=True)
    
    with col2:
        st.image("https://media.giphy.com/media/7SF5scnyEfxsc/giphy.gif", width=300)
        st.markdown("""<div class="regret-box"><b>Areeba's Regret:</b><br>"Love is a scam. Zoya is a legend. I should have opened the book instead of WhatsApp."</div>""", unsafe_allow_html=True)

    st.warning("Zoya worked the hardest. She didn't let 'Ishq' ruin her GPA.")
    if st.button("But why is Zoya's grade low? 🕵️‍♀️"):
        next_stage()

# --- SCENE 3: THE FLASHBACK (The Flirt) ---
elif st.session_state.stage == 2:
    st.title("🕰️ Flashback: The Boundary")
    chat_placeholder = st.empty()
    with chat_placeholder.container():
        st.markdown('<div class="chat-container"><div class="prof-msg"><b>Sir Sanaullah:</b> Hello Zoya beta. Discussion over coffee? 😉☕</div></div>', unsafe_allow_html=True)
        time.sleep(1)
        st.markdown('<div class="chat-container"><div class="zoya-msg"><b>Zoya:</b> Sir, respect the boundary. I am studying.</div><div class="zoya-msg">🚫 <b>ZOYA BLOCKED SIR SANAULLAH</b></div></div>', unsafe_allow_html=True)
    
    st.error("The ego was bruised. The 'A' was in danger.")
    if st.button("See the Revenge 😈"):
        next_stage()

# --- SCENE 4: THE OVERRIDE ---
elif st.session_state.stage == 3:
    st.title("😈 The Revenge")
    st.markdown("### Sir Sanaullah: *'Blocked? Fine. Enjoy the B+.'*")
    my_bar = st.progress(0)
    for i in range(100):
        my_bar.progress(i + 1)
        time.sleep(0.01)
    st.markdown('<div class="grade-card"><h2>Zoya</h2><div class="big-grade">B+</div><p>Official Grade (Due to Ego)</p></div>', unsafe_allow_html=True)
    
    if st.button("The Final Verdict"):
        next_stage()

# --- SCENE 5: THE CONSOLATION & SHAYARI ---
elif st.session_state.stage == 4:
    st.balloons()
    st.title("🎉 Justice for Zoya")
    st.write("Irfan and Areeba lost their grades to love. Zoya lost hers to integrity. We know who the real winner is.")

    st.markdown("### 🍰 The Honor Cake")
    html.html("""
    <div style="text-align:center; color:white; font-family:sans-serif;">
        <h1 style="font-size:100px;">🍰</h1>
        <p>A gift for the most focused student!</p>
    </div>
    """, height=200)

    st.markdown("---")
    st.markdown("### ✍️ A Tribute to Zoya")
    st.markdown("""
    <div class="shayari-box">
        سنا ہے حشر ہیں اس کی غزل سی آنکھیں<br>
        سنا ہے ہرن اس کو دشت بھر کے دیکھتے ہیں
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Over"):
        st.session_state.stage = 0
        st.rerun()
