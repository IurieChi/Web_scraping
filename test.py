import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Define the URL of the webpage
url = "https://mfinante.gov.ro/apps/infocodfiscal.html"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"}

# Send an HTTP GET request to the URL
response = requests.get(url,headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the image tag (assuming the image is embedded in the HTML)
    img_tag = soup.find('img')
    
    if img_tag:
        # Get the image URL from the src attribute
        img_url = img_tag['src']
        
        # Send an HTTP GET request to the image URL
        img_response = requests.get(img_url)
        
        # Check if the image request was successful
        if img_response.status_code == 200:
            # Open the image using PIL
            img = Image.open(BytesIO(img_response.content))
            
            # Display the image or perform any desired operations on it
            img.show()
        else:
            print("Failed to fetch the image.")
    else:
        print("No image found on the webpage.")
else:
    print("Failed to fetch the webpage.")

