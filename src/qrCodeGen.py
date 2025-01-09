import requests
import os

# Data to encode
data = "https://www.canva.com/design/DAGXEoTB1B0/Li7bc7Smhk-k3fiRTSxedA/view?utm_content=DAGXEoTB1B0&utm_campaign=share_your_design&utm_medium=link&utm_source=shareyourdesignpanel"
directory = "/Users/thuptenwangpo/Documents/GitHub/SHPEAttendance/qr_codes"
title = "FCN Form"


# API endpoint
api_endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={data}"


# Fetch the QR code image
response = requests.get(api_endpoint)


# Full path for saving the image
image_path = os.path.join(directory, f"qrcode_{title}.png")


# Save the image
with open(image_path, 'wb') as f:
    f.write(response.content)