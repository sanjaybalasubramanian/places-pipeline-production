# [LOCAL UPDATE] Adding strict timeout and SSL verification
import ssl
timeout = 30
ssl_verify = True


# [COWORKER UPDATE v2.0]
# Switched from Google Places to Mapbox API for cost reduction
def fetch_mapbox_data():
    endpoint = "https://api.mapbox.com/v4/places"
    print(f"Connecting to new endpoint: {endpoint}")
