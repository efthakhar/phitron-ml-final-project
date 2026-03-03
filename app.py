
import gradio as gr
import pandas as pd
import pickle

with open("water_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_water_potability(ph, hardness, solids, chloramines, sulfate,
                  conductivity, organic_carbon, trihalomethanes, turbidity, neutral):

    input_data = pd.DataFrame([[ph, hardness, solids, chloramines,
                                sulfate, conductivity, organic_carbon,
                                trihalomethanes, turbidity, neutral]],
                              columns=[
                                  "ph", "Hardness", "Solids", "Chloramines",
                                  "Sulfate", "Conductivity", "Organic_carbon",
                                  "Trihalomethanes", "Turbidity", "neutral"
                              ])

    prediction = model.predict(input_data)[0]

    return "✅ Safe" if prediction == 1 else "❌ Harmful"


interface = gr.Interface(
    fn=predict_water_potability,
    inputs=[
        gr.Number(label="pH"),
        gr.Number(label="Hardness"),
        gr.Number(label="Solids"),
        gr.Number(label="Chloramines"),
        gr.Number(label="Sulfate"),
        gr.Number(label="Conductivity"),
        gr.Number(label="Organic Carbon"),
        gr.Number(label="Trihalomethanes"),
        gr.Number(label="Turbidity"),
        gr.Number(label="Neutral (1 if 6.5<pH<8.5 else 0)")
    ],
    outputs="text",
    title="Water Potability Prediction System"
)

interface.launch()