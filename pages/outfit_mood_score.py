import streamlit as st
import tempfile
import os
from utils import get_outfit_mood_scores
import streamlit.components.v1 as components

def create_mood_chart_html(scores):
    """Create HTML bar chart for mood scores"""
    
    # Sort scores by value (descending)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Create HTML for the chart
    chart_html = """
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <h3 style="text-align: center; color: #333; margin-bottom: 20px;">🎭 Mood Analysis Results</h3>
    """
    
    for mood, score in sorted_scores:
        # Calculate bar width (percentage of max score)
        max_score = max(scores.values())
        bar_width = (score / max_score) * 100
        
        # Color based on score
        if score >= 80:
            color = "#28a745"  # Green for high scores
        elif score >= 60:
            color = "#ffc107"  # Yellow for medium scores
        else:
            color = "#dc3545"  # Red for low scores
        
        chart_html += f"""
        <div style="margin-bottom: 15px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-weight: bold; color: #333;">{mood}</span>
                <span style="font-weight: bold; color: {color};">{score}%</span>
            </div>
            <div style="background-color: #f8f9fa; border-radius: 10px; height: 20px; overflow: hidden;">
                <div style="
                    background-color: {color}; 
                    height: 100%; 
                    width: {bar_width}%; 
                    border-radius: 10px;
                    transition: width 0.5s ease-in-out;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                "></div>
            </div>
        </div>
        """
    
    chart_html += "</div>"
    return chart_html

def show_outfit_mood_score_page():
    """Outfit Mood Score Analysis page"""
    
    st.markdown("## 🎭 Outfit Mood Score")
    st.markdown("Upload your outfit photo and discover its mood and style personality!")
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 Upload Your Outfit")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose an outfit image",
            type=['png', 'jpg', 'jpeg'],
            help="Upload a photo of your outfit to analyze its mood"
        )
        
        # Analyze button
        analyze_button = st.button(
            "🔍 Analyze Mood",
            type="primary",
            use_container_width=True,
            disabled=uploaded_file is None
        )
        
        # Additional info
        st.markdown("### 💡 About Mood Analysis")
        st.markdown("""
        Our AI analyzes your outfit to determine its mood characteristics:
        
        • **Fierce**: Bold, confident, statement-making
        • **Minimalist**: Clean, simple, understated elegance
        • **Whimsical**: Playful, creative, artistic
        • **Elegant**: Sophisticated, refined, classic
        • **Casual**: Relaxed, comfortable, everyday
        • **Romantic**: Soft, feminine, dreamy
        """)
    
    with col2:
        st.markdown("### 📊 Mood Analysis Results")
        
        if uploaded_file is not None:
            # Display uploaded image
            st.image(uploaded_file, caption="Your outfit", use_container_width=True)
            
            # Process the image and analyze mood
            if analyze_button:
                with st.spinner("🔍 Analyzing your outfit's mood..."):
                    try:
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            temp_image_path = tmp_file.name
                        
                        # Get mood scores using utils function
                        scores = get_outfit_mood_scores(temp_image_path)
                        
                        # Clean up temporary file
                        os.unlink(temp_image_path)
                        
                        # Display results
                        st.markdown("---")
                        
                        # Create and display the HTML chart
                        chart_html = create_mood_chart_html(scores)
                        components.html(chart_html, height=400)
                        
                        # Display top mood
                        top_mood = max(scores.items(), key=lambda x: x[1])
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            padding: 20px;
                            border-radius: 10px;
                            text-align: center;
                            margin: 20px 0;
                        ">
                            <h3>🎯 Primary Mood</h3>
                            <h2 style="margin: 0; font-size: 2.5rem;">{top_mood[0]}</h2>
                            <p style="margin: 5px 0 0 0; font-size: 1.2rem;">{top_mood[1]}% confidence</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Success message
                        st.success("✅ Mood analysis completed! Your outfit has been analyzed.")
                        
                        # Additional insights
                        st.markdown("### 💭 Style Insights")
                        if top_mood[1] >= 80:
                            st.info(f"🌟 Your outfit strongly embodies the **{top_mood[0]}** mood! This is a clear style statement.")
                        elif top_mood[1] >= 60:
                            st.info(f"✨ Your outfit has a **{top_mood[0]}** vibe with some mixed elements. Great balance!")
                        else:
                            st.info(f"🎨 Your outfit has a subtle **{top_mood[0]}** influence. Consider adding more elements to strengthen this mood.")
                        
                    except Exception as e:
                        st.error(f"❌ Error analyzing mood: {str(e)}")
                        st.info("Please try again with a different image.")
        
        else:
            st.info("📤 Please upload an outfit image to get started!")
            st.markdown("""
            **Tips for better analysis:**
            - Use full-body shots when possible
            - Ensure good lighting
            - Include accessories and shoes
            - Avoid cluttered backgrounds
            """)

if __name__ == "__main__":
    show_outfit_mood_score_page() 