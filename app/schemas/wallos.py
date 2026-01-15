from pydantic import BaseModel

class TestConnectionRequest(BaseModel):
    wallos_host_url: str
    api_key: str
