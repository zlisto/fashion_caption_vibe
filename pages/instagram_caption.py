import streamlit as st
import tempfile
import os
from utils import get_instagram_caption

def show_instagram_caption_page():
    """Instagram Caption Generator page"""
    
    st.markdown("## 📸 Instagram Caption Generator")
    st.markdown("Upload your fashion photo and get an engaging caption!")
    
    # Create two columns with fixed widths
    col1, col2 = st.columns([1, 1], gap="medium")
    
    with col1:
        st.markdown("### 📤 Upload Your Image")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['png', 'jpg', 'jpeg'],
            help="Upload a fashion photo to generate a caption for"
        )
        
        # Style description input
        st.markdown("### 🎨 Style Description")
        style_description = st.text_input(
            "Describe your fashion style or mood",
            placeholder="e.g., 'elegant evening wear', 'casual street style', 'bohemian chic'",
            help="Describe the style, mood, or occasion for your outfit"
        )
        
        # Generate button
        generate_button = st.button(
            "✨ Generate Caption",
            type="primary",
            use_container_width=True,
            disabled=uploaded_file is None
        )
    
    with col2:
        st.markdown("### 📝 Generated Caption")
        
        if uploaded_file is not None:
            # Display uploaded image with fixed container
            image_container = st.container()
            with image_container:
                st.image(uploaded_file, caption="Your uploaded image", use_container_width=True)
            
            # Process the image and generate caption
            if generate_button and style_description:
                with st.spinner("🤖 Generating your perfect caption..."):
                    try:
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            temp_image_path = tmp_file.name
                        
                        # Generate caption using utils function
                        caption = get_instagram_caption(temp_image_path, style_description)
                        
                        # Clean up temporary file
                        os.unlink(temp_image_path)
                        
                        # Display the generated caption in a fixed container
                        caption_container = st.container()
                        with caption_container:
                            st.markdown("---")
                            st.markdown("### 🎯 Your Generated Caption:")
                            
                            # Create a styled caption box with fixed width
                            st.markdown(f"""
                            <div style="
                                background-color: white;
                                border: 2px solid #FF6B6B;
                                padding: 1rem;
                                border-radius: 5px;
                                margin: 1rem 0;
                                font-style: italic;
                                color: black;
                                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                                max-width: 100%;
                                word-wrap: break-word;
                                overflow-wrap: break-word;
                            ">
                                "{caption}"
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Copy button functionality
                            st.markdown("### 📋 Copy Caption")
                            st.code(caption, language=None)
                            
                            # Success message
                            st.success("✅ Caption generated successfully! Copy it above and use it for your Instagram post.")
                        
                    except Exception as e:
                        st.error(f"❌ Error generating caption: {str(e)}")
                        st.info("Please try again with a different image or style description.")
            
            elif generate_button and not style_description:
                st.warning("⚠️ Please enter a style description to generate a caption.")
        
        else:
            st.info("📤 Please upload an image to get started!")
            st.markdown("""
            **Tips for better captions:**
            - Use high-quality, well-lit images
            - Be specific about your style description
            - Include details about the occasion or mood
            """)

if __name__ == "__main__":
    show_instagram_caption_page() 