import requests
import os

def sanitize_filename(filename):
    # Replace problematic characters with underscores
    return filename.replace('/', '_').replace('\\', '_').replace(' ', '_')

def generate_qr_code(data, title, directory):
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # API endpoint
    api_endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={data}"
    
    # Fetch the QR code image
    response = requests.get(api_endpoint)
    
    # Sanitize the title and create full path
    safe_title = sanitize_filename(title)
    image_path = os.path.join(directory, f"qrcode_{safe_title}.png")
    
    # Save the image
    with open(image_path, 'wb') as f:
        f.write(response.content)
    
    print(f"QR code saved as: {image_path}")

def main():
    directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "qr_codes")
    
    while True:
        data = input("Please paste QR code link: ")
        title = input("Please enter the title of the QR code: ")
        
        generate_qr_code(data, title, directory)
        
        stop = input("Do you want to stop? (y/n): ").lower()
        if stop == 'y':
            print("Stopping the program...")
            print("Thank you for using the QR code generator and your hard work!")
            break

if __name__ == "__main__":
    main()