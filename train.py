from ultralytics import YOLO

data_file = "CaptchaPLS-5/data.yaml"
epochs = 500
imgsz = (130, 50)
device = "cuda"
batch = -1


if __name__ == '__main__':
    # Initialize
    model = YOLO("yolov8l.pt")

    # Train
    results = model.train(
        data=data_file,
        epochs=epochs,
        imgsz=imgsz,
        device=device,
        batch=batch,
        val=True,
    )
    print(results)
