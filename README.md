---
title: PNG Info
emoji: 🚀
colorFrom: indigo
colorTo: yellow
sdk: gradio
sdk_version: 3.16.2
app_file: app.py
pinned: false
license: wtfpl
---

This project is published on [HuggingFace](https://huggingface.co/spaces/andzhk/PNGInfo)

# PNG Info (png-params)

This is Gradio project for reading and displaying an image and its metadata from url.

Currently, only PNG is supported.

## Usage

- Copy image address
- Paste it into the **url** field
- or Drag and Drop/Upload image
- Submit

**Generation parameters** text can be directly used in AUTOMATIC1111 UI

## Running locally

### Prerequisites

Python 3

### Install requirements

```bash
pip install -r requirements.txt
```

### Run

```bash
python images.py
```

Use [nodemon](https://www.npmjs.com/package/nodemon) for development.

```bash
nodemon images.py
```

### Open UI

Usually Gradio UI is running on http://127.0.0.1:7860
