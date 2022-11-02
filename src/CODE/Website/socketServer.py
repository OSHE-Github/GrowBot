#import rospy
import websockets
import asyncio

# Async functions my cause issues when integrating to ROS
async def open(websocket, path):
    msg = await websocket.recv()

    if msg == "temp":
        # Read data from ROS message that reads from temp sensors
        await websocket.send("12C")
    if msg == "hum":
        # Read data from ROS message that reads from temp sensors
        await websocket.send("17%")

start_server = websockets.serve(open, "localhost", 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
