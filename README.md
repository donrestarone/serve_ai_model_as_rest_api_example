# README

This repository stands as an example on how to serve an AI Model / Checkpoint (from HuggingFace, CivitAI or where-ever) as a Python REST API.

# Caveats 

1. requests are processed in-line
2. if not CUDA, MPS is used. Please switch to CPU if you're running this in a non-CUDA and non-MPS environment (see here for guide: https://stackoverflow.com/questions/53266350/how-to-tell-pytorch-to-not-use-the-gpu)

# installing dependencies 
create/initialize python virtual environment

``` bash
python3 -m venv .env

source .env/bin/activate
```

install dependencies 

``` bash
pip install -r requirements.txt
```

# starting the server

``` bash
uvicorn api:app --reload --port 8001
```

# sample request
POST localhost:8000/generate
```json
{"prompt": "photograph: 35mm 3/4 eye-level portrait, lighting: natural, subject: actress pin-up style, expression: amused, pose: cowboy-shot, background: industrial", "negative_prompt": "blurry, dark photo, blue, deformed body features, mutated body parts, disfigured"}
```