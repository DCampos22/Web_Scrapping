import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove random symbols (@ % $ ^^)
    text = re.sub(r'[@%$\^]+', '', text)
    
    # Remove leftover numbers that are standalone (like 45, 55)
    text = re.sub(r'\b\d+\b', '', text)
    
    # Fix extra whitespace
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    
    # Strip each line
    lines = [line.strip() for line in text.split('\n')]
    
    # Remove empty lines
    lines = [line for line in lines if line]
    
    return '\n'.join(lines)

# --- Movie Corpus ---
with open('corrupt_movie_corpus.txt', 'r', encoding='utf-8') as f:
    movie_text = f.read()

print("=== SAMPLE RAW MOVIE LINES ===")
for line in movie_text.split('\n')[:5]:
    print(line)

cleaned_movie = clean_text(movie_text)

print("\n=== SAMPLE CLEANED MOVIE LINES ===")
for line in cleaned_movie.split('\n')[:5]:
    print(line)

with open('cleaned_movie.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_movie)

# --- Twitter Corpus ---
with open('corrupt_twitter_corpus.txt', 'r', encoding='utf-8') as f:
    twitter_text = f.read()

print("\n=== SAMPLE RAW TWITTER LINES ===")
for line in twitter_text.split('\n')[:5]:
    print(line)

cleaned_twitter = clean_text(twitter_text)

print("\n=== SAMPLE CLEANED TWITTER LINES ===")
for line in cleaned_twitter.split('\n')[:5]:
    print(line)

with open('cleaned_twitter.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_twitter)

print("\nDone! Cleaned files saved.")