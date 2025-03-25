from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
from typing import Set
import time

app = FastAPI(title="Trusted URL Checker API")

# Global set to store URLs
trusted_urls: Set[str] = set()

class URLRequest(BaseModel):
    url: str

@app.on_event("startup")
async def startup_event():
    """Load URLs into memory on startup"""
    print("Loading trusted URLs into memory...")
    start_time = time.time()
    
    try:
        with open("tranco_YX9YG.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 2:  # Ensure row has at least 2 elements
                    trusted_urls.add(row[1].strip())
        
        load_time = time.time() - start_time
        print(f"Loaded {len(trusted_urls)} URLs in {load_time:.2f} seconds")
    except Exception as e:
        print(f"Error loading URLs: {e}")
        raise

@app.get("/")
async def root():
    return {"message": "Trusted URL Checker API is running"}

@app.post("/check-url")
async def check_url(request: URLRequest):
    """Check if a URL is in the trusted list"""
    # Remove protocol and www if present
    url = request.url.lower()
    if url.startswith(('http://', 'https://')):
        url = url.split('://')[1]
    if url.startswith('www.'):
        url = url[4:]
    
    # Remove trailing slash if present
    url = url.rstrip('/')
    
    is_trusted = url in trusted_urls
    return {
        "url": request.url,
        "is_trusted": is_trusted,
        "normalized_url": url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 