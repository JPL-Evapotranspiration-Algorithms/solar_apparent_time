from typing import Union

from datetime import datetime, timedelta
import numpy as np
import rasters as rt

def UTC_to_solar(time_UTC: datetime, lon: float) -> datetime:
    """
    Converts Coordinated Universal Time (UTC) to solar time.

    Parameters:
    time_UTC (datetime): The UTC time.
    lon (float): The longitude in degrees.

    Returns:
    datetime: The solar time at the given longitude.
    """
    return time_UTC + timedelta(hours=(np.radians(lon) / np.pi * 12))

def solar_to_UTC(time_solar: datetime, lon: float) -> datetime:
    """
    Converts solar time to Coordinated Universal Time (UTC).

    Parameters:
    time_solar (datetime): The solar time.
    lon (float): The longitude in degrees.

    Returns:
    datetime: The UTC time at the given longitude.
    """
    return time_solar - timedelta(hours=(np.radians(lon) / np.pi * 12))

def UTC_offset_hours_for_longitude(lon: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Calculates the offset in hours from UTC based on the given longitude.

    Args:
        lon (Union[float, np.ndarray]): The longitude in degrees.

    Returns:
        Union[float, np.ndarray]: The calculated offset in hours from UTC.
    """
    # Convert longitude to radians and calculate the offset in hours from UTC
    return np.radians(lon) / np.pi * 12

def UTC_offset_hours_for_area(geometry: rt.RasterGeometry) -> rt.Raster:
    """
    Calculates the UTC offset in hours for a given raster geometry.

    Parameters:
    geometry (rt.RasterGeometry): The raster geometry.

    Returns:
    rt.Raster: The UTC offset in hours.
    """
    return rt.Raster(np.radians(geometry.lon) / np.pi * 12, geometry=geometry)

def solar_day_of_year_for_area(time_UTC: datetime, geometry: rt.RasterGeometry) -> rt.Raster:
    """
    Calculates the day of the year for a given UTC time and raster geometry.

    Parameters:
    time_UTC (datetime): The UTC time.
    geometry (rt.RasterGeometry): The raster geometry.

    Returns:
    rt.Raster: The day of the year.
    """
    doy_UTC = time_UTC.timetuple().tm_yday
    hour_UTC = time_UTC.hour + time_UTC.minute / 60 + time_UTC.second / 3600
    UTC_offset_hours = UTC_offset_hours_for_area(geometry=geometry)
    hour_of_day = hour_UTC + UTC_offset_hours
    doy = doy_UTC
    doy = rt.where(hour_of_day < 0, doy - 1, doy)
    doy = rt.where(hour_of_day > 24, doy + 1, doy)

    return doy

def solar_day_of_year_for_longitude(time_UTC: datetime, lon: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Calculates the day of year based on the given UTC time and longitude.

    Args:
        time_UTC (datetime.datetime): The UTC time to calculate the day of year for.
        lon (Union[float, np.ndarray]): The longitude in degrees.

    Returns:
        Union[float, np.ndarray]: The calculated day of year.
    """
    # Calculate the day of year at the given longitude
    DOY_UTC = time_UTC.timetuple().tm_yday
    hour_UTC = time_UTC.hour + time_UTC.minute / 60 + time_UTC.second / 3600
    offset = UTC_offset_hours_for_longitude(lon)
    hour_of_day = hour_UTC + offset
    DOY = DOY_UTC
    # Adjust the day of year if the hour of day is outside the range [0, 24]
    DOY = np.where(hour_of_day < 0, DOY - 1, DOY)
    DOY = np.where(hour_of_day > 24, DOY + 1, DOY)

    return DOY

def solar_hour_of_day_for_area(time_UTC: datetime, geometry: rt.RasterGeometry) -> rt.Raster:
    """
    Calculates the hour of the day for a given UTC time and raster geometry.

    Parameters:
    time_UTC (datetime): The UTC time.
    geometry (rt.RasterGeometry): The raster geometry.

    Returns:
    rt.Raster: The hour of the day.
    """
    hour_UTC = time_UTC.hour + time_UTC.minute / 60 + time_UTC.second / 3600
    UTC_offset_hours = UTC_offset_hours_for_area(geometry=geometry)
    hour_of_day = hour_UTC + UTC_offset_hours
    hour_of_day = rt.where(hour_of_day < 0, hour_of_day + 24, hour_of_day)
    hour_of_day = rt.where(hour_of_day > 24, hour_of_day - 24, hour_of_day)

    return hour_of_day
