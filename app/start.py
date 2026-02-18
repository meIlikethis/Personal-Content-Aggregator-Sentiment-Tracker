import requests
from bs4 import BeautifulSoup
from textblob import TextBlob


import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# 1. Grab the website data
url = "https://news.ycombinator.com/"
response = requests.get(url)

# 2. Parse the HTML (The "Soup")
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find all the headlines
# Hacker News puts headlines in a specific 'span' called 'titleline'
headlines = soup.find_all('span', class_='titleline')

print(f"{'HEADLINE':<60} | {'VIBE'}")
print("-" * 75)

for item in headlines[:15]:  # Just look at the top 15
    title = item.get_text()
    
    # Calculate Sentiment
    analysis = TextBlob(title)
    score = analysis.sentiment.polarity
    
    # Simple Vibe Check
    if score > 0:
        vibe = "😊 Positive"
    elif score < 0:
        vibe = "😟 Negative"
    else:
        vibe = "😐 Neutral"
        
    print(f"{title[:58]:<60} | {vibe}")





