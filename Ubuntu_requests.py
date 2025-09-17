import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    # Prompt user for URL
    url = input("Please enter the image URL: ").strip()

    # Create directory for fetched images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Connect to the global community 🌍
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one using timestamp
        if not filename or "." not in filename:
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        # Full path to save file
        filepath = os.path.join(folder, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("⚠️ Invalid URL. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. Please try again later.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
