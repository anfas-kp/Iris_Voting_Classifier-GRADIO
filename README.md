# Iris Voting Classifier Deploy Using Gradio

## Overview
This project implements an **Iris species classification model** using an ensemble **Voting Classifier**. The model predicts the species of an iris flower based on its sepal and petal dimensions. A **Gradio** interface is used to make the model accessible via a user-friendly web app.

## Features
- **Machine Learning Model**: Uses a Voting Classifier with multiple algorithms to enhance prediction accuracy.
- **Gradio Interface**: Provides an interactive UI for users to input flower measurements and get predictions.
- **Easy Deployment**: Can be run locally or deployed on cloud platforms like Hugging Face Spaces.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the application locally using:
```bash
python app.py
```
This will start a Gradio web interface, where you can input iris flower measurements and get predictions.

## Model Details
The Voting Classifier combines predictions from multiple models to improve accuracy. The dataset used is the famous **Iris Dataset**, which includes:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## Deployment
To deploy the app on a cloud platform:
1. Ensure all dependencies are installed.
2. Use **Gradio’s shareable link** feature or deploy via **Hugging Face Spaces**.

## Author
Developed by [Your Name]. Feel free to connect on GitHub!

## License
This project is licensed under the MIT License.

---
Feel free to contribute, raise issues, or suggest improvements!

