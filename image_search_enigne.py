import requests
import os

# Set up your API key and endpoint
API_KEY = 'Mbdyop4oUsWkOhEon7kpGxfA8hyXzudxxuk4UA2o6YQulMfpccyaFLff'
API_URL = 'https://api.pexels.com/v1/search'

def download_images(query, num_images=5, output_dir='pexels_images'):
    headers = {
        'Authorization': API_KEY
    }
    params = {
        'query': query,
        'per_page': num_images
    }

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for i, photo in enumerate(data['photos']):
            img_url = photo['src']['original']
            img_data = requests.get(img_url).content
            with open(f"{output_dir}/{query.replace(' ', '_')}_{i + 1}.jpg", 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded {i + 1}/{num_images}: {img_url}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    query = input("Enter the description of the image you want to download: ")
    num_images = int(input("Enter the number of images you want to download: "))
    download_images(query, num_images)
