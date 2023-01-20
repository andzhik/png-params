import gradio as gr
from PIL import Image
from urllib.request import Request, urlopen

def display_image_from_url(url, input_image):
    if url == '' and input_image is None:
        return None, "", ""

    image = None
    if url != '':
        req = Request(
            url=url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        res = urlopen(req)
        image = Image.open(res)
        image.load()


    if input_image is not None:
        image = input_image

    parameters = "Parameters have been erased from this image"
    if 'parameters' in image.info:
        parameters = image.info['parameters']

    return image, parameters, image.info

server = gr.Interface(display_image_from_url, ["text", gr.Image(type='pil')], [gr.Image(type='pil'), gr.Textbox(label="Generation Parameters"), gr.Textbox(label="Metadata")])
server.launch()
