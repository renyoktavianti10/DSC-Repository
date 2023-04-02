import re
import pandas as pd
import gradio as gr

from flask import Flask, jsonify

def clean_text(text):
    # Ganti semua karakter non-alfanumerik menggunakan spasi
    text = re.sub('[^a-zA-Z0-9\s]', ' ', text) 
    # Konversi semua ke lowercase
    text = text.lower()
    # Hapus double space
    text = re.sub(r'\s+',' ',text).strip() 
    return text

def read_csv(file, text_input):
    # Baca csv menjadi dataframe
    df = pd.read_csv(file.name)
    # Original data csv
    df_original = df.copy()
    # Data clean menggunakan regex
    df_cleaned = df.applymap(clean_text)
    # Input manual dari textbox
    text_cleaned = clean_text(text_input)
    return df_original, df_cleaned, text_cleaned

    
  # buat fungsi untuk menampilkan list di Gradio
gradio_ui = gr.Interface(
        fn=read_csv,
        title="Aplikasi Cleansing Data Binar Academy",
        description="Data cleansing file upload dan teks",
        inputs=[
            gr.inputs.File(),
            gr.inputs.Textbox(label="Masukan teks yang ingin dibersihkan...")],
        outputs=["dataframe", "dataframe", "text"])


# buat Gradio interface
gradio_ui.launch(share=True)

