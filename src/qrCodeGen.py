import requests
import os

# Data to encode
data = input("please paste qr code link: ")
directory = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/qr_codes"
title = input("Please enter the title of the qr code: ")


# API endpoint
api_endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={data}"


# Fetch the QR code image
response = requests.get(api_endpoint)


# Full path for saving the image
image_path = os.path.join(directory, f"qrcode_{title}.png")


# Save the image
with open(image_path, 'wb') as f:
    f.write(response.content)
    
    
# Ask if the user wants to stop
stop = "n"
while not stop:
    stop = input("Do you want to stop? (y/n): ")
    if stop.lower() == "y":
        stop = True
    else:
        data = input("please paste qr code link: ")
        directory = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/qr_codes"
        title = input("Please enter the title of the qr code: ")


        # API endpoint
        api_endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={data}"


        # Fetch the QR code image
        response = requests.get(api_endpoint)


        # Full path for saving the image
        image_path = os.path.join(directory, f"qrcode_{title}.png")


        # Save the image
        with open(image_path, 'wb') as f:
            f.write(response.content)