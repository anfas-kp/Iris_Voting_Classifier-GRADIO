# Iris Voting Classifier Deploy Using Gradio

## Overview
This project implements an **Iris species classification model** using an ensemble **Voting Classifier**. The model predicts the species of an iris flower based on its sepal and petal dimensions. A **Gradio** interface is used to make the model accessible via a user-friendly web app.

## Features
- **Machine Learning Model**: Uses a Voting Classifier that combines multiple algorithms to enhance prediction accuracy.
- **Gradio Interface**: Provides an interactive UI for users to input flower measurements and get real-time predictions.
- **Dataset**: Uses the well-known **Iris dataset** consisting of 150 samples across three species.
- **Visualization**: Displays prediction confidence and feature importance (if applicable).
- **Easy Deployment**: Can be run locally or deployed on cloud platforms like Hugging Face Spaces.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Dependencies
The following Python libraries are required:
- `numpy`
- `pandas`
- `scikit-learn`
- `gradio`
- `matplotlib` (optional for visualization)

## Usage
### Running Locally
To start the Gradio interface locally, run the following command:
```bash
python app.py
```
This will launch a local Gradio web interface where users can input iris flower measurements and get predictions.

### Using the Interface
1. Open the provided Gradio link in your browser.
2. Enter values for Sepal Length, Sepal Width, Petal Length, and Petal Width.
3. Click the **Predict** button to get the predicted Iris species along with confidence scores.

## Model Details
### Dataset
The model is trained using the **Iris dataset**, which consists of:
- 150 samples categorized into three species: Setosa, Versicolor, and Virginica.
- Four feature measurements:
  - **Sepal Length** (cm)
  - **Sepal Width** (cm)
  - **Petal Length** (cm)
  - **Petal Width** (cm)

### Machine Learning Approach
The Voting Classifier is an ensemble model that combines multiple classifiers to improve accuracy. It includes:
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Random Forest Classifier**

The final prediction is made based on majority voting among these models.

## Deployment
### Deploying on Hugging Face Spaces
To deploy the app on Hugging Face Spaces:
1. Create a new Space on Hugging Face and select **Gradio** as the SDK.
2. Upload your repository files.
3. Ensure `requirements.txt` is included to install dependencies.
4. Run the application, and a public Gradio link will be generated.

### Deploying on Other Platforms
- You can also deploy using **Streamlit Sharing, Heroku, or Flask** if needed.
- Dockerization can be done for container-based deployment.

## Author
Developed by Anfas-KP. Feel free to connect on GitHub and contribute to this project!


## License
This project is licensed under the **MIT License**.

---


