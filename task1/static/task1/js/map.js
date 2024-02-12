// map.js

/**
 * Asynchronously fetches JSON data from the specified URL.
 * @param {string} url - The URL to fetch JSON data from.
 * @returns {Promise<Object>} - A promise that resolves to the parsed JSON data.
 */
async function fetchJsonData(url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

// Fetch polygon coordinates from polygon.json
fetchJsonData('/static/task1/json/polygon.json')
.then(rawData => {
    // Process raw data to match the expected GeoJSON structure
    data = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates":  [rawData.polygon.map(coord => ol.proj.transform(coord, 'EPSG:4326', 'EPSG:3857'))]
        }
    }
    // Create a GeoJSON format to read the polygon data
    const geojsonFormat = new ol.format.GeoJSON();

    // Create a feature from the GeoJSON data
    const polygonFeature = geojsonFormat.readFeature(data);

    // Apply red color styling for visibility
    const polygonStyle = new ol.style.Style({
        fill: new ol.style.Fill({
            color: 'rgba(255, 0, 0, 0.2)', // Fill color with 20% opacity red
        }),
        stroke: new ol.style.Stroke({
            color: 'red', // Stroke color
            width: 2,     // Stroke width
        }),
    });
    polygonFeature.setStyle(polygonStyle);

    // Get the extent (bounding box) of the polygon geometry
    const extent = polygonFeature.getGeometry().getExtent();

    // Create a source and layer for the polygon
    const polygonSource = new ol.source.Vector({
      features: [polygonFeature],
    });
    const polygonLayer = new ol.layer.Vector({
      source: polygonSource,
    });

    // Create a map centered on the polygon
    const map = new ol.Map({
      target: 'map',
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM(),
        }),
        polygonLayer,
      ],
      view: new ol.View({
        center: ol.extent.getCenter(extent),
        zoom: 12, // Adjust the zoom level as needed
      }),
    });

    // Fit the view to the extent of the polygon with padding (adjust the padding as needed)
    map.getView().fit(extent, { padding: [50, 50, 50, 50], duration: 1000 });
  })
  .catch(error => {
    console.error('Error fetching or processing polygon data:', error);
  });