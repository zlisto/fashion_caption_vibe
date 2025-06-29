# 👗 Fashion Social Toolkit

A Streamlit-powered AI application that helps fashion enthusiasts create engaging social media content and analyze outfit moods.

## ✨ Features

### 📸 Instagram Caption Generator
- Upload fashion photos and get AI-generated captions
- Customize style descriptions and moods
- Generate trendy, hashtag-rich captions
- Copy-ready captions for immediate use

### 🎭 Outfit Mood Score
- Analyze outfit photos for mood characteristics
- Get confidence scores for different style categories:
  - **Fierce**: Bold, confident, statement-making
  - **Minimalist**: Clean, simple, understated elegance
  - **Whimsical**: Playful, creative, artistic
  - **Elegant**: Sophisticated, refined, classic
  - **Casual**: Relaxed, comfortable, everyday
  - **Romantic**: Soft, feminine, dreamy
- Visual bar charts and style insights

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fashion_caption_vibe
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   **Option A: .env file (recommended)**
   ```bash
   # Create a .env file in the project root
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```
   
   **Option B: Environment variable**
   ```bash
   # On Windows
   set OPENAI_API_KEY=your-api-key-here
   
   # On macOS/Linux
   export OPENAI_API_KEY=your-api-key-here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
fashion_caption_vibe/
├── app.py                 # Main Streamlit application
├── utils.py              # Core processing functions
├── genai.py              # OpenAI API wrapper class
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── pages/               # Streamlit pages
    ├── __init__.py
    ├── instagram_caption.py    # Instagram caption generator
    └── outfit_mood_score.py    # Outfit mood analyzer
```

## 🎯 Usage Guide

### Instagram Caption Generator

1. **Upload an image** - Choose a high-quality fashion photo
2. **Describe the style** - Enter details like "elegant evening wear" or "casual street style"
3. **Generate caption** - Click the button to get your AI-generated caption
4. **Copy and use** - Copy the generated caption for your Instagram post

### Outfit Mood Score

1. **Upload an outfit photo** - Use full-body shots for best results
2. **Analyze mood** - Click to analyze your outfit's style characteristics
3. **Review results** - See confidence scores for different mood categories
4. **Get insights** - Read personalized style recommendations

## 🔧 Configuration

### API Settings
The app uses OpenAI's GPT-4 Vision model for image analysis. Make sure you have:
- A valid OpenAI API key
- Sufficient API credits for image analysis

### Customization
You can modify the following in `utils.py`:
- **Caption style**: Edit the instructions in `get_instagram_caption()`
- **Mood categories**: Modify the mood list in `get_outfit_mood_scores()`
- **Fallback responses**: Customize fallback captions and scores

## 🎨 Tips for Best Results

### For Caption Generation:
- Use well-lit, high-quality images
- Be specific about style descriptions
- Include occasion or mood details
- Avoid cluttered backgrounds

### For Mood Analysis:
- Use full-body outfit shots
- Include accessories and shoes
- Ensure good lighting
- Avoid busy backgrounds

## 🛠️ Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **OpenAI**: AI model integration
- **OpenCV**: Image processing
- **Pillow**: Image handling
- **Pandas**: Data manipulation

### AI Models Used
- **GPT-4 Vision**: Image analysis and caption generation
- **Custom prompts**: Tailored for fashion content

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**"API key not found" error:**
- Ensure your OpenAI API key is set correctly
- Check that the environment variable is properly configured

**"Image upload failed" error:**
- Verify the image format (PNG, JPG, JPEG)
- Check file size (should be under 10MB)

**"Analysis failed" error:**
- Try with a different image
- Ensure good image quality and lighting
- Check your internet connection

### Getting Help
- Check the console output for detailed error messages
- Verify your OpenAI API key and credits
- Try with sample images first

## 🎉 Acknowledgments

- Built with Streamlit
- Powered by OpenAI GPT-4 Vision
- Inspired by fashion influencers and content creators

---

**Happy styling! ✨👗** 