from ultralytics import YOLO


if __name__ == '__main__':
    # Initialize the YOLO model
    model = YOLO('yolov8l.pt')

    # Tune hyperparameters for 30 epochs
    results = model.tune(
        data='CaptchaPLS-5/data.yaml',
        epochs=80,
        iterations=300,
        imgsz=(130, 50),
        save=False,
        val=False,
        batch=-1,
    )
    print(results)
