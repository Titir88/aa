#!/usr/bin/env python3
import uvicorn
import os
from app_full import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8402)))
