import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SmartSearchSystem:
    def __init__(self, courses_file):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.courses_df = pd.read_csv(courses_file)
        self.prepare_data()
        
    def prepare_data(self):
        # Combine relevant fields for embedding
        self.courses_df['combined_text'] = (
            self.courses_df['title'] + ' ' + 
            self.courses_df['lessons'].astype(str) + ' ' + 
            self.courses_df['price'].astype(str)
        )
        # Create embeddings for all courses
        self.course_embeddings = self.model.encode(self.courses_df['combined_text'].tolist())
        
    def search(self, query, top_k=5):
        # Create embedding for the query
        query_embedding = self.model.encode([query])
        
        # Calculate similarity between query and all courses
        similarities = cosine_similarity(query_embedding, self.course_embeddings)[0]
        
        # Get top k most similar courses
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Return the top k courses
        return self.courses_df.iloc[top_indices]
    
    def get_course_details(self, course_index):
        return self.courses_df.iloc[course_index].to_dict()

# Usage example
if __name__ == "__main__":
    search_system = SmartSearchSystem('Smart_analytics_vidhya_courses.csv')
    
    # Example search
    query = "machine learning for beginners"
    results = search_system.search(query)
    
    print(f"Top results for '{query}':")
    for _, course in results.iterrows():
        print(f"Title: {course['title']}")
        print(f"Lessons: {course['lessons']}")
        print(f"Price: {course['price']}")
        print(f"Rating: {course['rating']}")
        print(f"Link: {course['link']}")
        print("---")