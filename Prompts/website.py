import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="AI Website Builder",
    page_icon="🌐",
    layout="wide"
)

# Initialize model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3
)

# Header
st.title("🌐 AI Website Builder")
st.write(
    "Describe your website and get a fully functional website instantly."
)

# User input
website_description = st.text_area(
    "Describe your website",
    height=250,
    placeholder="""
Example:

Create a modern AI agency website.

Colors:
- Black
- White
- Blue

Pages:
- Hero
- About
- Services
- Testimonials
- Contact

Style:
- Modern
- Responsive
- Animations
"""
)

# Generate button
if st.button("Generate Website"):

    if not website_description.strip():
        st.warning("Please describe your website.")
        st.stop()

    with st.spinner("Generating website..."):

        prompt = f"""
You are a senior frontend developer.

Create a complete production-quality website.

Requirements:
{website_description}

Rules:

1. Return ONLY HTML.
2. Include CSS inside <style>.
3. Include JavaScript inside <script>.
4. Fully responsive.
5. Mobile friendly.
6. Professional UI.
7. Modern animations.
8. Clean design.
9. No explanations.
10. No markdown.
11. No code fences.

Generate a complete HTML document.
"""

        response = llm.invoke(prompt)

        html_code = response.content

        # Remove markdown fences if model adds them
        html_code = html_code.replace("```html", "")
        html_code = html_code.replace("```", "")

        st.success("Website Generated!")

        # Preview
        st.subheader("Live Preview")

        st.components.v1.html(
            html_code,
            height=800,
            scrolling=True
        )

        # Code
        st.subheader("Generated Code")

        st.code(
            html_code,
            language="html"
        )

        # Download button
        st.download_button(
            label="Download Website",
            data=html_code,
            file_name="index.html",
            mime="text/html"
        )