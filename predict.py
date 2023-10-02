import requests
import io

from PIL import Image

from ultralytics import YOLO


model_path = "runs/detect/412dataset/weights/best.pt"
captcha_link = "https://game.granbluefantasy.jp/c/i?t=169608487"


def get_captcha():
    req = requests.get(captcha_link)
    img = Image.open(io.BytesIO(req.content))
    img.save("captcha.png")

    return img


if __name__ == '__main__':
    model = YOLO(model_path)

    captcha = get_captcha()

    predictions = model.predict(
        captcha,
        save_txt=None
    )

    to_sort = []
    total_confidence = 0
    total_predictions = 0

    # parse predictions
    for idx, prediction in enumerate(predictions[0].boxes.xywhn):
        cls = int(predictions[0].boxes.cls[idx].item())
        cls_name = predictions[0].names[cls]

        # position of the bounding box in the image
        x = prediction[0].item()
        y = prediction[1].item()
        w = prediction[2].item()
        h = prediction[3].item()
        to_sort.append((x, cls_name))
        total_confidence += predictions[0].boxes.conf[idx].item()
        total_predictions += 1

    # sort by x position
    to_sort.sort(key=lambda x: x[0])
    # parse to string by class name
    result = "".join([x[1] for x in to_sort])
    print(f"'{captcha_link}', {total_confidence / total_predictions}, {result}")
