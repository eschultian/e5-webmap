import folium
MAP_FILE_PATH = 'data/map1.html'
if __name__ == '__main__':

    map = folium.Map(location = (35.61, -82.44))
    map.save(MAP_FILE_PATH)
    zoom_start = 10

    