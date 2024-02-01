from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
pipe.safety_checker = None

# prompt = "a photo of an astronaut riding a horse on mars"
prompt = "a photo of a gril in a church"
image = pipe(prompt).images[0]  
    
# image.save("astronaut_rides_horse.png")
image.save("girl_in_church.png")
