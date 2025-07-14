# 🖼️ Text-to-Image Generation using Stable Diffusion

This project demonstrates how to generate high-quality images from simple text prompts using the `Stable Diffusion` model. It uses the Hugging Face `diffusers` library and PyTorch to utilize a pre-trained generative model.

---

## 📌 Objective

To create a Python script that:
- Loads a pre-trained Stable Diffusion model
- Accepts a text prompt
- Generates and saves an image based on that prompt

---

## 🚀 Technologies Used

- Python 3.x
- Hugging Face 🤗 `diffusers`
- `transformers`
- `torch` (PyTorch)
- `safetensors`
- CUDA (optional, but recommended for GPU acceleration)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install diffusers transformers accelerate torch safetensors
```

### 4. Hugging Face Login (if required)

```bash
huggingface-cli login
```

---

## 🧠 How It Works

1. The script loads the pre-trained `runwayml/stable-diffusion-v1-5` model from Hugging Face using `StableDiffusionPipeline`.
2. It detects whether a GPU (CUDA) is available, and loads the model accordingly.
3. A text prompt is passed to the pipeline (e.g., "a futuristic city floating in the clouds").
4. The model generates a realistic image from that prompt.
5. The output is saved as `output.jpg` and also displayed.

---

## 📷 Example Prompt

```python
prompt = "Nikola Tesla in black and white"
```

### Output:
An AI-generated image based on the given description.

---

## 📁 Output

Image is saved locally as:

```
output.jpg
```

---

## ✅ Result

This project demonstrates the power of generative AI in transforming natural language into vivid images using pre-trained diffusion models.

---

## 📜 License

MIT License. Refer to [Stable Diffusion model license](https://huggingface.co/runwayml/stable-diffusion-v1-5) for details regarding model usage.

---

## 🙌 Acknowledgments

- [Hugging Face](https://huggingface.co/)
- [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
