import requests
import os

# Your Google Custom Search API key if you dont know read markdown file
API_KEY = ""

# Your Google Custom Search Engine ID
SEARCH_ENGINE_ID = ""

# Perform a Google Custom Search
def google_search(query, num=10, start=1):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&num={num}&start={start}&searchType=image"
    response = requests.get(url)
    return response.json()

def download_images(query, num_images=10, download_folder='images'):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    total_images_downloaded = 0
    start_index = 1
    while total_images_downloaded < num_images:
        results = google_search(query, num=min(10, num_images - total_images_downloaded), start=start_index)
        if 'items' not in results:
            break
        for item in results['items']:
            image_url = item['link']
            image_name = image_url.split('/')[-1]
            image_path = os.path.join(download_folder, image_name)
            try:
                with open(image_path, 'wb') as f:
                    image_data = requests.get(image_url).content
                    f.write(image_data)
                print(f"Downloaded: {image_name}")
            except Exception as e:
                print(f"Error downloading {image_name}: {e}")
            total_images_downloaded += 1
            if total_images_downloaded >= num_images:
                break
        start_index += 10

# List of search queries
search_queries = [
    "search1",
    "search2"
]

# Download images for each search query
number_of_images = 50 # you can change
for query in search_queries:
    download_images(query, num_images=number_of_images)
