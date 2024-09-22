import folium
import json
from folium.plugins import LocateControl, MarkerCluster

# Path to the custom icon image
icon_image = r'D:\ecojustice\icon.png'

# Load eco justice data from JSON
with open('eco_justice_data.json', 'r') as f:
    eco_justice_data = json.load(f)

# Initialize map object
mapObj = folium.Map(location=[41.4129347271411, 74.51477050781251], 
                    tiles='OpenStreetMap', 
                    zoom_start=6, 
                    max_zoom=19, 
                    control_scale=True)

# Initialize marker cluster
cluster = MarkerCluster().add_to(mapObj)

# Loop through eco justice data
for item in eco_justice_data:
    name = item['name']
    coordinates = (item['latitude'], item['longitude'])
    insta_post = item['instagram_link']
    image_path = item['image_path']
    small_article = item['small_article']

    # Create custom icon using the predefined icon image
    custom_icon = folium.CustomIcon(icon_image, icon_size=(35, 35), popup_anchor=(0, -22))

    # Define HTML for marker pop-up with a unique image for each entry
    pub_html = folium.Html(f"""
    <div style="text-align: center;">
        <p><span style="font-family: Didot, serif; font-size: 21px;">{name}</span></p>
        <img src="{image_path}" alt="{name} image" style="width:200px;height:150px;">
        <p style="font-size: 12px; color: gray;">{small_article}</p>
        <p><a href="{insta_post}" target="_blank">More on Instagram</a></p>
    </div>
    """, script=True)

    # Create pop-up
    popup = folium.Popup(pub_html, max_width=700)

    # Create marker with the custom icon and add it to the cluster
    custom_marker = folium.Marker(location=coordinates, icon=custom_icon, tooltip=name, popup=popup)
    custom_marker.add_to(cluster)

# Add locate control
LocateControl(auto_start=False).add_to(mapObj)

# Save the map to an HTML file
mapObj.save('output.html')
