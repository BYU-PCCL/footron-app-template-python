import asyncio
import time

import foomsg

messaging = foomsg.Messaging()


def message_handler(message):
    print(message)


async def main_loop():
    while True:
        await messaging.send_message(round(time.time() * 1000))
        await asyncio.sleep(0.05)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    messaging.add_message_listener(message_handler)
    messaging_loop = event_loop.create_task(messaging.start())
    event_loop.create_task(main_loop())
    event_loop.run_until_complete(messaging_loop)
