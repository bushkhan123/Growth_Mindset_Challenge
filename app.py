import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="🌱 Growth Mindset Challenge", layout="centered")

# Title
st.title("🌱 Growth Mindset Challenge")
st.markdown("""
Welcome! This app is here to help you reflect, grow, and stay motivated.  
Adopting a **growth mindset** means embracing challenges, learning from feedback, and believing that your abilities can develop with effort.
""")

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📝 Daily Challenge", "📈 Progress Tracker", "📚 Growth Tips"])

# Session state to store reflections
if "reflections" not in st.session_state:
    st.session_state.reflections = []

# Page: Home
if page == "🏠 Home":
    st.subheader("🌟 Why a Growth Mindset?")
    st.write("""
- **Embrace Challenges:** See them as opportunities.
- **Learn from Mistakes:** Every failure is a step forward.
- **Persist Through Difficulties:** Growth takes time and effort.
- **Celebrate Effort:** Progress matters more than perfection.
- **Stay Curious:** Always be open to learning something new.
    """)
    st.image("mg.jpg", caption="Growth vs Fixed Mindset", use_column_width=True)

# Page: Daily Challenge
elif page == "📝 Daily Challenge":
    st.subheader("💪 Your Daily Growth Reflection")

    today = datetime.now().strftime("%A, %d %B %Y")
    st.markdown(f"🗓️ **Today is:** {today}")

    challenge = st.text_area("🧠 What challenge did you face today?")
    lesson = st.text_area("📘 What did you learn from it?")
    action = st.text_area("🎯 What will you do differently next time?")

    if st.button("✅ Submit Reflection"):
        if challenge and lesson and action:
            st.session_state.reflections.append({
                "date": today,
                "challenge": challenge,
                "lesson": lesson,
                "action": action
            })
            st.success("Reflection saved! Keep growing 💡")
        else:
            st.warning("Please fill out all fields before submitting.")

# Page: Progress Tracker
elif page == "📈 Progress Tracker":
    st.subheader("🧾 Your Reflections So Far")

    if st.session_state.reflections:
        for i, entry in enumerate(reversed(st.session_state.reflections)):
            st.markdown(f"### 🗓️ {entry['date']}")
            st.markdown(f"- **Challenge:** {entry['challenge']}")
            st.markdown(f"- **Lesson Learned:** {entry['lesson']}")
            st.markdown(f"- **Next Time:** {entry['action']}")
            st.markdown("---")
    else:
        st.info("No reflections yet. Go to the Daily Challenge page to add your first one!")

# Page: Growth Tips
elif page == "📚 Growth Tips":
    st.subheader("💡 Growth Mindset Tips")
    st.markdown("""
- 🔁 **Feedback is fuel** – welcome it, even if it's tough.
- 🔍 **Focus on effort**, not outcome.
- 🧩 **Break big goals into small wins**.
- 🕰️ **Be patient** – progress takes time.
- 🌟 **Celebrate small victories**.
- 📖 **Learn from role models** and your past self.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ for lifelong learners.")
