---

# AI Image Generation with Stable Diffusion

This project demonstrates **AI-based image generation** using **Stable Diffusion**. Users can generate high-quality, customizable images from text prompts with optional negative prompts to guide the results.

---

## 🚀 Features

* Generate images from **text prompts**.
* Use **negative prompts** to avoid unwanted artifacts.
* Customize image size, inference steps, and guidance scale.
* Set a **manual random seed** for reproducible outputs.
* Works on **CUDA**, **MPS (Apple Silicon)**, or CPU.

---

## 🛠️ Requirements

* Python 3.10+
* [PyTorch](https://pytorch.org/) (with CUDA if available)
* [Diffusers](https://github.com/huggingface/diffusers)
* [Transformers](https://github.com/huggingface/transformers)
* PIL (Python Imaging Library)
* Optional: Matplotlib (for inline display)

You can install dependencies using:

```bash
pip install torch torchvision diffusers transformers pillow matplotlib
```

---

## ⚡ Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-image-generation.git
cd ai-image-generation
```

2. Run the script:

```bash
python generate_image.py
```

3. Modify the parameters in the script:

```python
prompt = "ultra-detailed portrait of a red fox wearing a tiny scarf, cinematic lighting, 35mm"
negative_prompt = "blurry, lowres, jpeg artifacts, extra fingers, text, watermark"
num_inference_steps = 30
guidance_scale = 7.5
height = 512
width = 512
```

4. Generated image will be saved as:

```
generated_image.png
```

5. Optional: Display the image in Python:

```python
from PIL import Image
image = Image.open("generated_image.png")
image.show()
```

Or in Jupyter Notebook:

```python
from IPython.display import display
display(image)
```

---

## ⚙️ How It Works

1. Loads the **Stable Diffusion v1-5** model from Hugging Face.
2. Uses the **Euler Ancestral Scheduler** for image sampling.
3. Runs inference on GPU if available; otherwise falls back to CPU or Apple MPS.
4. Generates a **high-quality image** based on your text prompt and settings.
5. Saves the output image locally.

---

## 🔧 Customization

* Change `prompt` and `negative_prompt` to generate different styles.
* Adjust `num_inference_steps` (20–35 is recommended).
* Change `guidance_scale` to control adherence to the prompt (5–9 recommended).
* Modify `height` and `width` for higher or lower resolution.

---

## 📸 Example Output

![generated_image](https://github.com/DavieObi/AI-Image-Generation-with-Stable-Diffusion/blob/1699b11febc3ca17f533f42de003fd1e052e9aad/generated_image.png)

---

## 📄 References

* [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
* [Diffusers Library](https://huggingface.co/docs/diffusers/index)
* [Euler Ancestral Scheduler](https://huggingface.co/docs/diffusers/api/schedulers/euler_ancestral_discrete)

---

## ⚡ License

MIT License – free to use and modify.

---
