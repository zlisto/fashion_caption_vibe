import streamlit as st
import os
from pages.instagram_caption import show_instagram_caption_page
from pages.outfit_mood_score import show_outfit_mood_score_page

# Configure the page
st.set_page_config(
    page_title="Fashion Social Toolkit",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">👗 Fashion Social Toolkit</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your AI-powered fashion companion for social media</p>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("🎯 Navigation")
    
    # Page selection
    page = st.sidebar.selectbox(
        "Choose a tool:",
        ["Instagram Caption Generator", "Outfit Mood Score"],
        index=0
    )
    
    # Sidebar info
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📱 About")
    st.sidebar.markdown("""
    This toolkit helps you create engaging fashion content for social media:
    
    • **Instagram Caption Generator**: Create compelling captions for your fashion posts
    • **Outfit Mood Score**: Analyze the mood and style of your outfit
    
    Upload an image and let AI do the magic! ✨
    """)
    
    # Display selected page
    if page == "Instagram Caption Generator":
        show_instagram_caption_page()
    elif page == "Outfit Mood Score":
        show_outfit_mood_score_page()

if __name__ == "__main__":
    main() 