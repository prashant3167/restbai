import requests
from time import sleep

def get_room_details(img_url):
    print(img_url)
    detected_features = []
    detected_roomtype = []
    url = "https://api-eu.restb.ai/vision/v2/multipredict"
    client_key = ("9b1115f0bb06029dc31818b0a57c561f2361a7818f4fca3d9f0ef9f15b466f9a",)
    # for img in images:
    payload = {
        "client_key": client_key,
        "model_id": "re_features_v4,re_roomtype_global_v2",
        "image_url": img_url,
    }
    response = requests.get(url, params=payload).json()
    detected_features.extend(
        [
            item["label"]
            for item in response["response"]["solutions"]["re_features_v4"][
                "detections"
            ]
        ]
    )
    detected_roomtype.append(
        response["response"]["solutions"]["re_roomtype_global_v2"]["top_prediction"][
            "label"
        ]
    )
    detected_feature_set = set(detected_features)
    sleep(1)
    return detected_roomtype, detected_features
