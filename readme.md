# AI Image Generator (Stable Diffusion)

A text-to-image generation system built using Stable Diffusion, providing both a Streamlit-based UI and a notebook interface for generating images from prompts.

---

## 🚀 What This Actually Solves

Generates images from text prompts using diffusion models, enabling:
- Rapid visual prototyping  
- Creative content generation  
- Prompt-based image synthesis  

---

## ⚙️ Core Features

### Text-to-Image Generation
- Generate images from natural language prompts  
- Uses Stable Diffusion v1.5  

### Prompt Control
- Supports negative prompts to avoid unwanted elements  
- Adjustable parameters:
  - Inference steps  
  - Guidance scale  
  - Resolution  
  - Random seed  

### Dual Interface
- Streamlit app for interactive usage  
- Jupyter Notebook for experimentation  

### Output Management
- Saves generated images locally  
- Supports reproducible outputs via seed  

---

## 🏗️ System Flow

User Prompt → Model Inference → Image Generation → Save Output

---

## 📁 Project Structure

AI-image-generator-with-Stable-Diffusion/  
├── app.py                  # Streamlit app  
├── Image gen.ipynb         # Notebook version  
├── generated_images/       # Output images  
├── README.md  
└── .gitignore  

---

## 🛠️ Tech Stack

- Python  
- PyTorch  
- Hugging Face Diffusers  
- Stable Diffusion v1.5  
- Streamlit  

---

## 🚀 Setup

pip install streamlit torch diffusers transformers pillow  

---

## ▶️ Run

streamlit run app.py  

---

## 🧪 Usage

1. Enter a prompt  
2. (Optional) Add negative prompt  
3. Adjust parameters  
4. Generate image  
5. Save output  


## 💡 Future Improvements

- Add GPU optimization and batching  
- Support custom model fine-tuning  
- Add REST API for integration  
- Improve prompt presets and UI  

---

## 📌 Why This Project Matters

This project demonstrates:
- Use of diffusion models for image generation  
- Integration of ML models into applications  
- Prompt-based control systems  
- Basic ML deployment with UI  

---

## 👤 Author

Jaikar Ramu  
https://github.com/viperxjaikar  

---

## ⭐ Star if useful
