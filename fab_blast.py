import marimo

__generated_with = "0.7.5"
app = marimo.App(width="medium")


@app.cell
def __():
    import folium

    # Initialize the map centered around a central location
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    tiles = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"

    m = folium.Map(location=[20, 0], zoom_start=2, tiles=tiles, attr=attr)

    # Define the cities with their coordinates
    cities = [
        ('Tuxtla Gutierrez, Mexico', (16.75, -93.11)),
        ('Beauvais, France', (49.43, 2.10)),
        ('Duhok, Iraq', (36.88, 42.99)),
        ('Washington DC, USA', (38.90, -77.03)),
        ('Berlin, Germany', (52.52, 13.40))
    ]

    # Collect coordinates for polyline
    coords = [(lat, lon) for city, (lat, lon) in cities]

    media = ["1.jpg", "9.jpg", "14.jpg", "18.jpg", "5.jpg"]

    # Add markers with numbers
    for i, (city, (lat, lon)) in enumerate(cities):
        folium.Marker(
            location=[lat, lon],
            popup=f"{i+1}. {city}",
            icon = folium.DivIcon(html=f"""<div style="font-size: 12pt; color: black; font-weight: bold;">
        <img src='/media/{media[i]}' style='width: 200pt;' />
    </div>"""))

    # Add polylines with increasing thickness
    base_weight = 5  # Starting weight
    for i in range(len(coords) - 1):
        segment_coords = coords[i:i+2]
        opac = 0.25 * i + 0.2
        weight = base_weight * (1.5 ** i)  # Increase weight by 50% per segment
        folium.PolyLine(locations=segment_coords, color='#8800ff', weight=weight, opacity=opac).add_to(m)

    # Save the map to an HTML file
    m.save('map.html')

    return (
        attr,
        base_weight,
        cities,
        city,
        coords,
        folium,
        i,
        lat,
        lon,
        m,
        media,
        opac,
        segment_coords,
        tiles,
        weight,
    )


@app.cell
def __(m):
    m
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
