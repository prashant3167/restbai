import requests
from time import sleep
import openai


def get_room_details(img_url):
    print(img_url)
    url = "https://api-eu.restb.ai/vision/v2/multipredict"
    client_key = ("9b1115f0bb06029dc31818b0a57c561f2361a7818f4fca3d9f0ef9f15b466f9a",)
    # for img in images:
    payload = {
        "client_key": client_key,
        "model_id": "re_features_v4,re_roomtype_global_v2",
        "image_url": img_url,
    }
    response = requests.get(url, params=payload).json()

    feature_set = [
        item["label"]
        for item in response["response"]["solutions"]["re_features_v4"]["detections"]
    ]
    room_type = response["response"]["solutions"]["re_roomtype_global_v2"][
        "top_prediction"
    ]["label"]
    sleep(1)
    return room_type, feature_set


def get_advert_title(features):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Give a catchy one liner advertisement headline for property also mention following features: "
        + str(features),
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['"""'],
    )
    return response["choices"][0]["text"]


def get_advert_desc(features):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Give a catchy 5 liner advertisement description for property also mention following features: "
        + str(features),
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['"""'],
    )
    return response["choices"][0]["text"]


def get_request_list_items(items):
    if items != "":
        if "," in items:
            return items.split(",")
        else:
            return list(items)


def get_mentioned_feature(data):
    interior = get_request_list_items(data["interior"])
    kitchen = get_request_list_items(data["kitchen"])
    appliances = get_request_list_items(data["appliances"])

    return (
        interior
        + kitchen
        + appliances
        + [str(data["totalBedroom"]) + "bedrooms"]
        + [str(data["totalWashroom"]) + "washrooms"]
    )
