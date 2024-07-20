# `solar_apparent_time` Python Package

The `solar_apparent_time` Python package translates Python datetime between solar apparent time and Coordinate Universal Time (UTC).

[Gregory H. Halverson](https://github.com/gregory-halverson-jpl) (they/them)<br>
[gregory.h.halverson@jpl.nasa.gov](mailto:gregory.h.halverson@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 329G

## Usage

### `UTC_to_solar(time_UTC: datetime, lon: float) -> datetime`

Converts Coordinated Universal Time (UTC) to solar apparent time at given longitude for single time.

**Parameters:**
- `time_UTC` (datetime): The UTC time.
- `lon` (float): The longitude in degrees.

**Returns:**
- datetime: The solar time at the given longitude.

### `solar_to_UTC(time_solar: datetime, lon: float) -> datetime`

Converts solar apparent time to Coordinated Universal Time (UTC) at given longitude for single time.

**Parameters:**
- `time_solar` (datetime): The solar time.
- `lon` (float): The longitude in degrees.

**Returns:**
- datetime: The UTC time at the given longitude.

### `UTC_offset_hours(geometry: rasters.RasterGeometry) -> rasters.Raster`

Calculates the UTC offset in hours for an area defined by a `RasterGeometry` object from the `rasters` package.

**Parameters:**
- `geometry` (rasters.RasterGeometry): The raster geometry.

**Returns:**
- rasters.Raster: The UTC offset in hours.

### `day_of_year(time_UTC: datetime, geometry: rasters.RasterGeometry) -> rasters.Raster`

Calculates the day of the year for a given UTC time and an area defined by a `RasterGeometry` object from the `rasters` package.

**Parameters:**
- `time_UTC` (datetime): The UTC time.
- `geometry` (rasters.RasterGeometry): The raster geometry.

**Returns:**
- rasters.Raster: The day of the year.

### `hour_of_day(time_UTC: datetime, geometry: rasters.RasterGeometry) -> rasters.Raster`

Calculates the hour of the day for a given UTC time and an area defined by a `RasterGeometry` object from the `rasters` package.

**Parameters:**
- `time_UTC` (datetime): The UTC time.
- `geometry` (rasters.RasterGeometry): The raster geometry.

**Returns:**
- rasters.Raster: The hour of the day.

