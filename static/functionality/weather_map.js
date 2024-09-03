console.log("Map script loaded.");
var map = L.map('map').setView([51.505, -0.09], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

var temperatureLayer = L.tileLayer(`https://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid=${api_key}`, {
    maxZoom: 19,
    opacity: 0.5
}).addTo(map);

var precipitationLayer = L.tileLayer(`https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=${api_key}`, {
    maxZoom: 19,
    opacity: 0.5
});

var baseLayers = {
    "Temperature": temperatureLayer,
    "Precipitation": precipitationLayer
};

L.control.layers(baseLayers).addTo(map);
