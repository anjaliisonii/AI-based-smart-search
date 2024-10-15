import streamlit as st
from smart_search import SmartSearchSystem
import base64

# Initialize the search system
@st.cache_resource
def load_search_system():
    return SmartSearchSystem('Smart_analytics_vidhya_courses.csv')

search_system = load_search_system()

# Function to add background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1518655048521-f130df041f66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

# Custom CSS for hover effects and buttons
def local_css():
    st.markdown("""
    <style>
    .course-box {
        background-color: rgba(240, 242, 246, 0.8);
        padding: 20px;
        margin: 10px 0;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .course-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .course-title {
        color: #1f618d;
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #1f618d;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #154360;
        transform: translateY(-2px);
        box-shadow: 0 5px 10px rgba(0,0,0,0.1);
    }
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
def main():
    add_bg_from_url()
    local_css()

    st.title("Smart Analytics Vidhya Course Search")

    query = st.text_input("Enter your search query:")
    if st.button("Search"):
        if query:
            results = search_system.search(query)
            st.write(f"Top results for '{query}':")
            for _, course in results.iterrows():
                st.markdown(f"""
                <div class="course-box">
                    <h3 class="course-title">{course['title']}</h3>
                    <p><strong>Rating:</strong> {course['rating']}</p>
                    <p><strong>Lessons:</strong> {course['lessons']}</p>
                    <p><strong>Price:</strong> {course['price']}</p>
                    <a href="{course['link']}" target="_blank" style="text-decoration: none;">
                        <div class="stButton">
                            <button style="display: inline-block;">Go to course</button>
                        </div>
                    </a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter a search query.")

    st.markdown("""
    ---
    <p style="text-align: center; color: #7f8c8d;">
        © 2024 Smart Analytics Vidhya Course Search. All rights reserved.
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()