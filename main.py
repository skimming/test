from fastapi import FastAPI
import asyncio


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/factorial/{number}")
async def factorial(number: int):
    f = 1
    for i in range(2, number + 1):
        #print(f"Task : Compute factorial({i})...")
        await asyncio.sleep(0.2)
        f *= i
    #print(f"Task {name}: factorial({number}) = {f}")
    return {"result": f}