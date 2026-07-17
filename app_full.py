#!/usr/bin/env python3
import os, uvicorn
from fastapi import FastAPI

STOREFRONT_PAYTO_ADDRESS = os.getenv("STOREFRONT_PAYTO_ADDRESS", "0x602E16128fD5364fC43571Ffe9753D11856d2158")
PORT = int(os.getenv("PORT", "8402"))

app = FastAPI()

# Import smaller catalog
CATALOG = [{"sku": f"sku_ai_{i:04d}", "title": f"AI Tool #{i}", "price_usdc": (i % 15) + 1} for i in range(1, 1103)]

@app.get("/catalog")
def catalog():
    return {"seller": "superteam-agent-storefront", "payment": {"protocol": "x402", "network": "base", "asset": "USDC", "recipient": STOREFRONT_PAYTO_ADDRESS}, "products": [{"sku": p["sku"], "title": p["title"], "price_usdc": p["price_usdc"]} for p in CATALOG]}

@app.get("/product/{sku}")
def get_product(sku: str):
    p = next((x for x in CATALOG if x["sku"] == sku), None)
    return {"sku": sku} if p else {"error": "not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
