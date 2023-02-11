from fastai.vision.all import *
import cv2
import numpy as np
import json
import os

learn = load_learner('model.pkl')
with open('./breeds.json') as f:
    labels = json.load(f)


def classify(img):
    img = cv2.resize(img, (512, 512))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _,_,probs = learn.predict(img)

    result = {labels[i]: float(probs[i]) for i in range(len(labels))}

    max_value = max(result.values())
    if max_value > 0.25:
        max_name = max(result, key=result.get)
    else:
        max_name = "I don't recognized it, please send me a cat or dog photo"

    return max_name

def print_cats():
    directory = "cats"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            path = os.path.join(directory, filename)
            img = cv2.imread(path)
            result = classify(img)
            print(filename, result)

if __name__ == "__main__":
    print_cats()
