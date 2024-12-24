import requests

INSTAGRAM_API_URL = "https://www.instagram.com/api/v1"
PROFILE_INFO_ROUTE = INSTAGRAM_API_URL + "/users/web_profile_info"

#TODO add types.

def get_timeline(username : str):
  request_url = PROFILE_INFO_ROUTE + f"/?username={username}"
  
  x_ig_app_id = "936619743392459" 

  headers = {"X-IG-App-ID" : x_ig_app_id }
  response = requests.get(request_url, headers=headers)
  return response.json["data"]["user"]


def get_latest_timeline_image_url(username : str):
  timeline = get_timeline(username)

  timeline_images = timeline["edges"]
  latest_image = timeline_images[0]["node"]
  latest_image_url = latest_image["display_url"]
  print(latest_image_url)
  return latest_image_url


