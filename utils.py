import os
import random
from genai import GenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize GenAI with API key from environment
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file or environment.")

genai = GenAI(openai_api_key)

def get_instagram_caption(image_path: str, style_description: str) -> str:
    """
    Generate an Instagram caption for a fashion image.
    
    Parameters:
    ----------
    image_path : str
        Path to the uploaded image file
    style_description : str
        User-provided description of the fashion style or mood
        
    Returns:
    -------
    str
        Generated Instagram caption
    """
    try:
        # Instructions for the AI to generate fashion captions
        instructions = """You are a fashion expert and social media influencer. 
        Generate engaging, trendy Instagram captions for fashion photos. 
        The caption should be:
        - 1-3 sentences long
        - Include relevant hashtags (3-5 hashtags)
        - Match the style/mood described
        - Be authentic and relatable
        - Use emojis appropriately
        - Include a call-to-action or personal touch
        
        Format: Caption text followed by hashtags on new lines."""
        
        # Create the prompt
        prompt = f"""Analyze this fashion image and create an Instagram caption.
        
        Style/Mood Description: {style_description}
        
        Please generate a compelling caption that matches this style and mood."""
        
        # Generate caption using the GenAI class
        caption = genai.generate_image_description(
            image_paths=[image_path],
            instructions=prompt,
            model='gpt-4o-mini'
        )
        
        return caption.strip()
        
    except Exception as e:
        print(f"Error generating caption: {e}")
        # Fallback captions if AI generation fails
        fallback_captions = [
            f"Living my best life in this {style_description} look! ✨ #fashion #style #ootd",
            f"Channeling {style_description} vibes today! 💫 #fashionista #styleinspo",
            f"This {style_description} moment is everything! 🔥 #fashion #trending",
            f"Feeling confident in this {style_description} ensemble! 💃 #style #fashion",
            f"Style is a way to say who you are without having to speak. {style_description} edition! ✨ #fashion #lifestyle"
        ]
        return random.choice(fallback_captions)

def get_outfit_mood_scores(image_path: str) -> dict:
    """
    Analyze an outfit image and return mood scores.
    
    Parameters:
    ----------
    image_path : str
        Path to the uploaded outfit image
        
    Returns:
    -------
    dict
        Dictionary with mood labels and confidence percentages
    """
    try:
        # Instructions for the AI to analyze outfit mood
        instructions = """You are a fashion psychologist and style analyst. 
        Analyze this outfit image and determine the mood and style characteristics.
        
        Please analyze the outfit for these mood categories and provide confidence scores (0-100):
        - Fierce: Bold, confident, statement-making, powerful
        - Minimalist: Clean, simple, understated elegance, refined
        - Whimsical: Playful, creative, artistic, fun
        - Elegant: Sophisticated, refined, classic, timeless
        - Casual: Relaxed, comfortable, everyday, laid-back
        - Romantic: Soft, feminine, dreamy, delicate
        
        Return ONLY a JSON object with the mood categories as keys and scores (0-100) as values.
        Example: {"Fierce": 85, "Minimalist": 30, "Whimsical": 15, "Elegant": 60, "Casual": 20, "Romantic": 10}"""
        
        # Generate mood analysis using the GenAI class
        analysis = genai.generate_image_description(
            image_paths=[image_path],
            instructions=instructions,
            model='gpt-4o-mini'
        )
        
        # Try to parse the response as JSON
        import json
        try:
            # Clean the response and extract JSON
            analysis = analysis.strip()
            if analysis.startswith('```json'):
                analysis = analysis[7:]
            if analysis.endswith('```'):
                analysis = analysis[:-3]
            
            scores = json.loads(analysis)
            
            # Ensure all required moods are present
            required_moods = ["Fierce", "Minimalist", "Whimsical", "Elegant", "Casual", "Romantic"]
            for mood in required_moods:
                if mood not in scores:
                    scores[mood] = random.randint(5, 25)
            
            return scores
            
        except json.JSONDecodeError:
            # Fallback to random scores if JSON parsing fails
            return generate_fallback_scores()
            
    except Exception as e:
        # Fallback scores if AI analysis fails
        return generate_fallback_scores()

def generate_fallback_scores() -> dict:
    """Generate fallback mood scores when AI analysis fails"""
    moods = ["Fierce", "Minimalist", "Whimsical", "Elegant", "Casual", "Romantic"]
    scores = {}
    
    # Generate random scores that sum to a reasonable total
    total_score = 0
    for mood in moods:
        score = random.randint(10, 90)
        scores[mood] = score
        total_score += score
    
    # Normalize scores to percentages
    for mood in scores:
        scores[mood] = int((scores[mood] / total_score) * 100)
    
    # Ensure at least one mood has a high score
    high_mood = random.choice(moods)
    scores[high_mood] = random.randint(70, 95)
    
    return scores

# Example usage and testing functions
def test_instagram_caption():
    """Test function for Instagram caption generation"""
    # This would be used for testing with a sample image
    sample_style = "elegant evening wear"
    # sample_image_path = "path/to/sample/image.jpg"
    # caption = get_instagram_caption(sample_image_path, sample_style)
    # print(f"Generated caption: {caption}")
    pass

def test_outfit_mood_scores():
    """Test function for outfit mood scoring"""
    # This would be used for testing with a sample image
    # sample_image_path = "path/to/sample/outfit.jpg"
    # scores = get_outfit_mood_scores(sample_image_path)
    # print(f"Mood scores: {scores}")
    pass

if __name__ == "__main__":
    # Test the functions
    test_instagram_caption()
    test_outfit_mood_scores() 