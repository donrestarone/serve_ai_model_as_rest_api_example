# README
This repository stands as an example on how to serve an AI Model / Checkpoint (from HuggingFace, CivitAI or where-ever) as a Python REST API.
<img width="1301" alt="Screen Shot 2024-03-02 at 11 01 01 AM" src="https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/59adad7d-1d03-454f-9f69-825073ecb97c">

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

# generated artifacts
Using this repository, the following images were generated. Prompts are included in the filename 

![vitruvian-man_vaporwave1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/428fb179-a5c8-42f4-b189-3dbc4df88b74)
![vitruvian-man_--style_vaporwave1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/df8f1a84-08d2-4999-85bf-39fd0c963b98)
![sunset_blood_moon,_photograph_24mm,_airplane_flying_in_distance,_vaporwave1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/e59915be-a595-43e9-9fe7-2b374674ff11)
![photograph:_35mm_3-4_eye-level_portrait,_lighting:_natural,_subject:_actress_pin-up_style,_expression:_sultry,_pose:_holding_thunder,_background:_industrial1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/2cadd8ac-acfb-41e9-b392-c71d3eef0a1c)
![photograph:_35mm_3-4_eye-level_portrait,_lighting:_natural,_subject:_actress_pin-up_style_bangs,_expression:_sultry,_pose:_holding_thunder,_background:_industrial1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/2765a65a-d28d-43aa-b71c-4f3e11d86f0b)
![photograph:_35mm_3-4_eye-level_portrait,_lighting:_natural,_subject:_actress_pin-up_style_bangs,_expression:_sultry,_pose:_facing_camera_hands_out-of-shot,_background:_industrial1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/54ca9378-4c36-4bd6-9e00-e87b82711902)
![photograph:_35mm_3-4_aerial_shot,_lighting:_natural,_subject:_nuclear_explosion,_expression:_devestating,_background:_mountains_ocean1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/373bafa2-dc02-44c7-a40c-6646b4c6e34c)
![photograph:_35mm_3-4_aerial_shot,_lighting:_natural,_subject:_northern_lights,_expression:_soothing,_background:_mountains_ocean1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/4c813bde-8dd9-439b-a867-6bc72f494399)
![photograph_35mm_point-of-view_house_underwater_fish_swimming_in_the_moonlight_natural_light1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/955a7905-4386-4440-b29c-31d404c00c3e)
![photograph_24mm,_farmland,_animals,_crops,_sepia,_rainy_day1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/afacf8fd-33e7-462a-8505-b54f93d8ca13)
![nature](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/ece43b03-a366-44b9-8f36-e2038e8427e1)
![mansion-in-appalachia](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/d6895f47-22f5-4d1d-8cae-fd7cecf007c6)
![landscape_with_water__1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/8d03b4c1-bbaa-4b50-981b-4f5197e70600)
![girldiringpony-appalachia](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/ed73ea07-eab4-400f-938a-93626100aa6e)
![galactic-intelligence_blackhole_--style_vaporwave_1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/a12db367-4a22-47d6-996b-f2bc764355b7)
![galactic_waterfall_vaporwave1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/399ba892-110b-4056-8ff6-b6a955066cbd)
![galactic_intelligence_vaporwave_1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/155cbadc-9add-4b58-a0dd-77b1b2dc453c)
![35mm_photograph_desert_daytime_mountains_camel_3-4_1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/39aed9c7-c247-4e23-b374-dde73bdbb53d)
![3-4_submerged_photograph_in_35mm,_POV_subject:_shark_in_the_ocean_natural-lighting_daytime1](https://github.com/donrestarone/serve_ai_model_as_rest_api_example/assets/35935196/25eff8f4-2672-4993-93b8-d3f7ba76ef01)
