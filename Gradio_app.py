import pickle

def prediction_class(sepal_length,sepal_width,petal_length,petal_width):
    
    loaded_model = pickle.load(open("iris_voting_classifier.pkl", "rb"))
    input_data=[[sepal_length,sepal_width,petal_length,petal_width]]
    prediction=loaded_model.predict(input_data)[0]
    return str(prediction)

# create Gradio interface
import gradio as gr

iface=gr.Interface(
    fn=prediction_class,
    inputs=[
        gr.Number(label='Sepal Length (CM)'),
        gr.Number(label='Sepal Width (CM)'),
        gr.Number(label='Petal Length (CM)'),
        gr.Number(label='Petal Width (CM)'),
    ],
    outputs='text',
    title='Iris Flower Classifier With Voting Ensemble',
    description='Enter The Flowers Measurment for the prediction',
    theme="huggingface"
)


# to launch

iface.launch()