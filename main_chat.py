from pydantic import BaseModel, Field
from enum import Enum
from my_app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


class BasicExtraction(BaseModel):
    needs_rooms: bool = Field(desc="In the given message, is user giving information about the flight and number of rooms they need for the flight?")
    arrival_date: str = Field(desc="Arrival date in YYYY-MM-DD format")
    arrival_time: str = Field(desc="Arrival time in HH:MM format")
    departure_date: str = Field(desc="Departure date in YYYY-MM-DD format")
    departure_time: str = Field(desc="Departure time in HH:MM format")
    number_of_rooms: int = Field(desc="Number of rooms needed")

class BookingResponse(BaseModel):
    booking_room: bool
    number_of_rooms: int

class NumberOfRooms(BaseModel):
    number_of_rooms: int
    date: str

class ResponseType(str, Enum):
    SHUT_DOWN_AGENT = "shut_down_agent"
    START_AGENT = "start_agent"
    ROOMS_BOOKED_QUERY = "rooms_booked_query"
    REPORT = "report"
    OVERRIDE_ROOMS = "override_rooms"
    OTHERS = "others"
    ROOMS_EMPTY_QUERY = "rooms_empty_query"
    CHANGE_MESSAGE_ORIGINATOR = "change_airlines_number" 
    GET_ORIGINATOR = "get_airlines_number"
    CHANGE_HOTEL_EMPLOYEE_NUMBER = "change_hotel_employee_number"
    GET_HOTEL_EMPLOYEE_NUMBER = "get_hotel_employee_number"
    HELP = "help"

class ConfirmationResponse(BaseModel):
    response_type: ResponseType

class OverrideResponse(BaseModel):
    date: str
    number_of_rooms: int

class PhoneNumberResponse(BaseModel):
    phone_number: str = Field(..., description="Phone number")

class DateResponse(BaseModel):
    date: str = Field(..., description="Date for which rooms booked are queried in YYYY-MM-DD format")
