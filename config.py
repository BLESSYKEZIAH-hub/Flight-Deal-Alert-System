import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load values from .env file
load_dotenv()


# ========== FLIGHT ROUTE MODEL ==========
@dataclass
class FlightRoute:
    origin: str
    destination: str
    current_price: float
    target_price: float


# ========== AMADEUS API CONFIG (NEW) ==========
# These variables load your private keys from the .env file
AMADEUS_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")

# The URLs required to talk to the Amadeus Server
AMADEUS_TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_SEARCH_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"


# ========== EMAIL CONFIG ==========
# Toggle email alerts here
ENABLE_EMAIL_ALERTS = True  # set True only when you’re ready

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email credentials loaded from .env
SENDER_EMAIL = os.getenv("SMTP_EMAIL")
SENDER_PASSWORD = os.getenv("SMTP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECEIVER_EMAIL")


# ========== SAMPLE FLIGHTS (STATIC DATA) ==========
# Kept as a backup in case the API fails
SAMPLE_FLIGHTS = [
    FlightRoute("HYD", "DEL", 4500, 5000),
    FlightRoute("HYD", "BLR", 3800, 3500),
    FlightRoute("HYD", "MAA", 3200, 3200),
    FlightRoute("DEL", "BOM", 6200, 5500),
]