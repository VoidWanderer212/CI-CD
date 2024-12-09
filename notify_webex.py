import requests
import o

# Environment variables for security
WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")  # Replace with your WebEx bot token
ROOM_ID = os.getenv("ROOM_ID")          # Replace with your WebEx Room ID

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
