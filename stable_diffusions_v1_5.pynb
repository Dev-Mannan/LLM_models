#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a horse",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))


# In[28]:


import gradio as gr
import requests
import io
import time
from PIL import Image

# Define the API details
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

# Function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Gradio interface function
def gr_interface(prompt):
    # API request payload
    payload = {"inputs": prompt}

    # Start timer
    start_time = time.time()

    # Make API request
    image_bytes = query(payload)

    # Stop timer
    end_time = time.time()
    processing_time = end_time - start_time

    try:
        # Decode the response content to get the image
        pil_image = Image.open(io.BytesIO(image_bytes))
    except Exception as e:
        # If an error occurs, display an error message
        return None, f"Error: {str(e)}"

    return pil_image, f"Processing time: {processing_time:.2f} seconds"

# Close any existing Gradio interfaces
gr.close_all()

# Example prompts
example_prompts = [
    "Astronaut riding a horse",
    "Sunset over the mountains",
    "Abstract art with vibrant colors",
    "Cute puppies playing in a garden",
]

# Create a Gradio interface
demo = gr.Interface(
    fn=gr_interface,
    inputs=[gr.Textbox(label="Your prompt")],
    outputs=[gr.Image(label="Generated Image"), gr.Textbox(label="Status")],
    title="Image Generation with Stable Diffusion",
    description="Generate images with Stable Diffusion model",
    allow_flagging="never",
    examples=[[prompt] for prompt in example_prompts]
)

# Launch the Gradio interface and print the link
share_link = demo.launch(share=True)
print("Share this link: ", share_link)


# In[ ]:




