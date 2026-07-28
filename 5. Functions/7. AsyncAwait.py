"""
Asynchronous Programming (Async/Await)
--------------------------------------
Concurrency is crucial in modern web development (like FastAPI). 
Instead of waiting for slow I/O operations (like network requests or database queries) 
to finish, `asyncio` allows Python to switch to other tasks while waiting.
"""

import asyncio
import time

# 1. Defining an asynchronous function using `async def`
async def fetch_data(id: int, delay: int):
    print(f"Task {id}: Starting to fetch data...")
    # asyncio.sleep simulates a slow I/O operation (like a network request).
    # Using 'await' gives control back to the Event Loop to run other tasks.
    await asyncio.sleep(delay) 
    print(f"Task {id}: Finished fetching data after {delay} seconds!")
    return {"id": id, "data": "Some data from DB"}

async def main():
    print("--- Starting Async Tasks ---")
    start_time = time.time()
    
    # 2. Running multiple tasks concurrently using asyncio.gather()
    # Instead of running task 1, waiting, then running task 2,
    # we kick them both off at the same time.
    results = await asyncio.gather(
        fetch_data(id=1, delay=2),
        fetch_data(id=2, delay=3)
    )
    
    end_time = time.time()
    
    print("\n--- Results ---")
    print(f"Data returned: {results}")
    # Notice that the total time is ~3 seconds (the longest delay), NOT 5 seconds (2+3)!
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# 3. Starting the Event Loop
asyncio.run(main())

