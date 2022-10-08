import tensorflow as tf 
from PIL import Image 
import streamlit as st
import numpy as np


"""
#deep Classifier project
"""
model=tf.keras.models.load_model('model.h5')
uploaded_file=st.file_uploader('Choose a file')
if  uploaded_file is not None:
    image=Image.open(uploaded_file)
    img=image.resize((244,244))
    img_array=np.array(img)
    img_array=np.expand_dims(img_array,axis=0)
    result=model.predict(img_array)

    argmax_idx=np.argmax(result,axis=1)
    if argmax_idx[0] == 0:
        st.image(image,caption="predicted: cat")
    else:
        st.image(image,caption="predicted : dog") 