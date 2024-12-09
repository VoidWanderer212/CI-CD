import requests
import os

# Get the WebEx token and room ID from environment variables
WEBEX_TOKEN = ("ZGM2ZTJjOGItYWQxOS00ODY3LWE4OGItYWFiMzBjZjZmYzcwMGRlOTBkYjAtZTFl_P0A1_18df2bf4-66a3-4793-b661-314dcbe95852")  # Replace with your actual environment variable name
ROOM_ID = ("a58cfa40-b5e6-11ef-bf09-6910fd7587cf")          # Replace with your actual environment variable name

def send_webex_notification(message):
    """
    Sends a message to a WebEx room.
    """
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": ROOM_ID,
        "text": message
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    # Replace this message with a dynamic status from your CI/CD pipeline
    message = "The pipeline has successfully completed!"
    send_webex_notification(message)

