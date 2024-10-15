import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_analytics_vidhya_courses(url):
    courses = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all course containers
    course_containers = soup.find_all('a', class_='course-card')
    
    for container in course_containers:
        # Extract title
        title = container.find('h3').text.strip()
        
        # Extract rating
        rating_span = container.find('span', class_='review__stars-count')
        rating = rating_span.text.strip('()') if rating_span else 'No ratings'
        
        # Extract number of lessons
        lessons_span = container.find('span', class_='course-card__lesson-count')
        lessons = lessons_span.strong.text if lessons_span else 'N/A'
        
        # Extract price
        price_span = container.find('span', class_='course-card__price')
        price = price_span.strong.text if price_span else 'N/A'
        
        # Determine if it's free
        is_free = price.lower() == 'free'
        
        # Extract course link
        link = "https://courses.analyticsvidhya.com" + container['href']
        
        courses.append({
            'title': title,
            'rating': rating,
            'lessons': lessons,
            'price': price,
            'is_free': is_free,
            'link': link
        })
    
    return courses

# URL of the free courses page
url = 'https://courses.analyticsvidhya.com/pages/all-free-courses'

# Scrape the courses
all_courses = scrape_analytics_vidhya_courses(url)

# Convert to DataFrame
df = pd.DataFrame(all_courses)

# Save to CSV
df.to_csv('Smart_analytics_vidhya_courses.csv', index=False)

print(f"Scraped {len(all_courses)} courses and saved to analytics_vidhya_courses.csv")

# Display the first few rows of the DataFrame
print(df.head())