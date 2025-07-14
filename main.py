from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_auth_token=True
)

pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

prompt = "Nikola tesla in black and white "

image = pipe(prompt).images[0]

image.save("generated_image.jpg")
image.show()

