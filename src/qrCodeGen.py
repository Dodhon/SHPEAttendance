import requests
import os

# Data to encode
data = "https://docs.google.com/forms/d/e/1FAIpQLSes8Gsf7XbL9haJcA6C54OU9jvc92JAJ2-ZKrKol7VWPv5Q9Q/viewform?usp=sf_link"
directory = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/qr_codes"
title = "shpetinas_interest_form"


# API endpoint
api_endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={data}"


# Fetch the QR code image
response = requests.get(api_endpoint)


# Full path for saving the image
image_path = os.path.join(directory, f"qrcode_{title}.png")


# Save the image
with open(image_path, 'wb') as f:
    f.write(response.content)