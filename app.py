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

    parameters = "Parameters have been erased from this image or unsupported format"
    if 'parameters' in image.info:
        parameters = image.info['parameters']

    return image, parameters, image.info

blocks = gr.Blocks(css="#out_image {height: 400px}")
with blocks as png_info:
    with gr.Row():
        gr.Markdown(
    """
    Report any issues on the (GitHub)[https://github.com/andzhik/png-params] page of this project
    """)
    with gr.Row().style(equal_height=False):
        with gr.Column():
            in_url = gr.Textbox(label="Source URL")
            in_image = gr.Image(label="Source Image", type='pil')
            with gr.Row():
                btn_submit = gr.Button("Submit", variant="primary")

        with gr.Column():
            out_image = gr.Image(type='pil', elem_id="out_image")
            out_info = gr.Textbox(label="Generation Parameters")
            out_meta = gr.Textbox(label="Metadata")
    
    btn_submit.click(fn=display_image_from_url,
    inputs=[in_url, in_image],
    outputs=[out_image, out_info, out_meta])
            
png_info.launch()
