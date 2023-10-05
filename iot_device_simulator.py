import asyncio
import websockets
import random

# This is an asynchronous function to send simulated temperature data
async def send_temperature_data():
    # The URI of the websocket server
    uri = "ws://localhost:8765"
    
    # Connect to the websocket server
    async with websockets.connect(uri) as websocket:
        while True:
            # Generate a random temperature value between 20°C and 30°C
            simulated_temperature = 25 + random.uniform(-5, 5)
            
            # Send the simulated temperature to the server
            await websocket.send(f"{simulated_temperature:.2f}")
            
            # Wait for 5 seconds before sending the next value
            await asyncio.sleep(5)

# Start the IoT device simulator and keep sending data
asyncio.get_event_loop().run_until_complete(send_temperature_data())
