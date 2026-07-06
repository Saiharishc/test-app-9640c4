import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/api/health')
def health_check():
    return {"status": "ok"}

@app.get('/api/test')
def test_endpoint():
    return {"message": "This is a test response!"}

if os.path.isdir("frontend/build"):
    app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

    @app.get("{path:path}")
    async def serve_frontend(path: str):
        if path.startswith("api/"):
            # If it's an API route, let FastAPI handle it
            raise HTTPException(status_code=404, detail="Not Found")
        return FileResponse("frontend/build/index.html")
else:
    @app.get("/")
    def read_root():
        return {"message": "Frontend build not found. Please run `npm run build`."}

    # If frontend build is not found, still provide API endpoints
    # The health and test endpoints are defined above and will be available
    # For testing purposes, we can add dummy routes here if needed
    pass

