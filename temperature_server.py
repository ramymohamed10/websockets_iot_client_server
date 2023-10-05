# temperature_server.py
import asyncio
import websockets
from datetime import datetime

# This is an asynchronous function to handle incoming temperature data
async def handle_temperature_data(websocket, path):
    try:
        # Continuously listen for messages on the websocket
        async for message in websocket:
            # Print the received temperature along with details about the source and timestamp
            print(f"Received temperature: {message}°C from {websocket.remote_address} at {datetime.now()}")
    except websockets.exceptions.ConnectionClosedOK:
        # Handle the case when the connection is intentionally closed
        print(f"Connection closed by {websocket.remote_address}")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"Error occurred: {e}")

# Start a websocket server on the specified host and port, and use the handle_temperature_data function to manage connections
start_server = websockets.serve(handle_temperature_data, "localhost", 8765)

# Start the server and keep it running indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
