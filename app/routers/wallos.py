import httpx

from fastapi import APIRouter
from app.schemas.wallos import TestConnectionRequest

router = APIRouter()

@router.post("/test_connection")
async def test_connection(request: TestConnectionRequest):
    url = f"{request.wallos_host_url.rstrip('/')}/api/subscriptions/get_subscriptions.php"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"apiKey": request.api_key})
        
    if response.status_code != 200:
        return {"success": False, "message": "Failed to connect to Wallos API."}
    
    try:
        data = response.json()
        
        if not data.get("success", False):
            return {"success": False, "message": data.get("message", "Unknown error from Wallos API.")}
        
        subscriptions = data.get("subscriptions", [])
        return {
            "success": True,
            "message": f"Connection successful. Found {len(subscriptions)} subscriptions.",
            "subscriptions": subscriptions
        }

    except Exception as e:
        return {"success": False, "message": f"Error parsing response: {str(e)}"}

