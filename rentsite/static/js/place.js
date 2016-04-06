/**
 * Created by votetob on 25.03.16.
 */

var dfd = coords_from_django;
var center_point = [dfd['latitude'], dfd['longitude']];
var map = new ymaps.Map('MyMap', {
     center: center_point,
     zoom: 15
});
map.geoObjects.add(new ymaps.Placemark(center_point));
map.setZoom(15);
map.addControl(new ymaps.Zoom());



