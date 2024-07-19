from datetime import datetime, timedelta
import numpy as np

def UTC_to_solar(time_UTC: datetime, lon: float) -> datetime:
    return time_UTC + timedelta(hours=(np.radians(lon) / np.pi * 12))

def solar_to_UTC(time_solar: datetime, lon: float) -> datetime:
    return time_solar - timedelta(hours=(np.radians(lon) / np.pi * 12))
