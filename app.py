# Alternative smaller starter script
from fastapi import FastAPI
import os

app = FastAPI(title="Superteam Agent Storefront", version="1.0.0")

# Import the full app
import app_full
app = app_full.app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8402))
    uvicorn.run(app, host="0.0.0.0", port=port)
