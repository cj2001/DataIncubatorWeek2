# SnowStats: My Capstone Project at The Data Incubator

This is code for my project for The Data Incubator called SnowStats.  For more information on this project, check out http://snowstats.strikingly.com.

In general, I used the a script to do a bulk download of LANDSAT data (mainly LANDSAT 1-5 and 8) to find the days when a geographic region had no cloud cover and then grab the image to calculate the Normalized Difference Snow Index (NDSI) as a measure of snow coverage.  I chose LANDSAT because of how long it has been operating (back to 1970) as well as the ease of access to their data, which is freely and publicly available.  My goal was to then correlate the NDSI to El Nino/La Nina as measured by ENSO 3.4 in an attempt to prove or disprove the rumored correlation of snow fall (approximated by NDSI) to ENSO.  

Ultimately this proved unsuccessful because the return rate of LANDSAT is every 14 days.  If, on return, the area was cloudy, then there would be no data.  So the collected data points were too sparse to do much with.  But the method is viable and a variety of other satellite constellations (that do not provide free access to their data) would potentially be better candidates.  Some have return rates on the order of 1 day and might better resolution than LANDSAT.
