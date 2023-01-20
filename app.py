import gradio as gr
from PIL import Image
from urllib.request import Request, urlopen

def display_image_from_url(url):
    if url == '':
        return None, ""

    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    res = urlopen(req)
    image = Image.open(res)
    image.load()

    parameters = "Parameters have been erased from this image"
    if 'parameters' in image.info:
        parameters = image.info['parameters']

    return image, parameters, image.info

server = gr.Interface(display_image_from_url, "text", ["image", gr.Textbox(label="Generation Parameters"), gr.Textbox(label="Metadata")])
server.launch()
