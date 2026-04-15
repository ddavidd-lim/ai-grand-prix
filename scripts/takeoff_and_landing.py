#!/usr/bin/env python3

import asyncio
import logging
import subprocess

from mavsdk import System

from utils.get_wsl2_ip import get_wsl2_ip


# Enable INFO level logging by default so that INFO messages are shown
logging.basicConfig(level=logging.INFO)


async def run():
    drone = System()
    wsl_ip = get_wsl2_ip()
    print(f"Connecting to WSL2 at {wsl_ip}")
    await drone.connect(system_address=f"udpout://{wsl_ip}:14580")

    status_text_task = asyncio.ensure_future(print_status_text(drone))

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(10)

    print("-- Landing")
    await drone.action.land()

    # Keep alive until Ctrl+C
    print("Keeping connection alive, Ctrl+C to exit")
    while True:
        await asyncio.sleep(1)

    # This kills the connection to ground control
    status_text_task.cancel()


async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
