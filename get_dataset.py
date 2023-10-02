import os

from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()


token = os.getenv("ROBOFLOW_TOKEN")
workspace_name = os.getenv("ROBOFLOW_WORKSPACE")
project_name = os.getenv("ROBOFLOW_PROJECT")
version = os.getenv("ROBOFLOW_DATASET_VERSION")

rf = Roboflow(api_key=token)
project = rf.workspace(workspace_name).project(project_name)
dataset = project.version(version).download("yolov8")
