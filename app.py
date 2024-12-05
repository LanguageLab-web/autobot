from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

# Import your data models from main.py
from main import BasicExtraction, BookingResponse, NumberOfRooms, ResponseType, ConfirmationResponse, OverrideResponse, PhoneNumberResponse, DateResponse

app = FastAPI()  # Create the FastAPI application instance

# Define your API endpoints for processing message types
@app.post("/extract_info")
async def extract_info(data: BasicExtraction):
    # Process the extracted information from the request body (data)
    # ... your processing logic here ...
    return {"message": "Information extracted successfully"}

# Add more API endpoints as needed for processing other message types
# ... (add additional endpoints here) ...
