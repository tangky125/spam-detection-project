from fastapi import FastAPI
import uvicorn
import os

# Simple test app
app = FastAPI(title="Test API")

@app.get("/")
async def root():
    return {"message": "Test API is running!", "status": "healthy"}

@app.get("/ping")
async def ping():
    return {"status": "pong", "message": "Test API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy", "message": "Test API is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
