# README
# python -m venv .env
# source .env/bin/activate
# python model.py
# prompt = "3/4 submerged photograph in 35mm, POV subject: lone shark in the clear ocean natural-lighting daytime"
# negative_prompt = "blurry, dark photo, blue, deformed body features, mutated body parts, disfigured"
# get_model().generate(prompt, negative_prompt)

import torch
from diffusers import DiffusionPipeline
from diffusers import DPMSolverMultistepScheduler



class Model:

  def __init__(self):
    # set manual seed for determinism
    self.seed = 1
    self.default_negative_prompt = "blurry, dark photo, blue, deformed body features, mutated body parts, disfigured"

    if torch.cuda.is_available():
      print("using CUDA!")

    self.device = torch.device("cuda" if torch.cuda.is_available() else "mps")
    self.pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    self.pipe = self.pipe.to(self.device)
    self.generator = torch.Generator("cuda" if torch.cuda.is_available() else "mps").manual_seed(self.seed)

    #configuration 
    self.pipe.safety_checker = None
    self.pipe.requires_safety_checker = False
    # Recommended if your computer has < 64 GB of RAM
    self.pipe.enable_attention_slicing()
    # optimize speed
    self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)

  def generate(self, prompt, negative_prompt):
    # generate
    images = self.pipe(prompt, negative_prompt=negative_prompt, generator=self.generator, num_inference_steps=20).images

    # save to disk
    file_name = 'outputs/' + '_'.join(prompt.replace('/', "-").split(" ")) + str(self.seed) + ".png"
    image = images[0]
    image.save(file_name)
    image.show()
    return image

model = Model()

def get_model():
  return model



