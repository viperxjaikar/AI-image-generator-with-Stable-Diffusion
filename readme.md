echo "# AI Image Generator with Stable Diffusion

Generate stunning images from text descriptions using AI.

## Features
- Generate images from text prompts
- Adjustable parameters (steps, guidance scale, resolution)
- Negative prompts to avoid unwanted elements
- Web interface using Streamlit

## Installation
\`\`\`bash
pip install streamlit torch diffusers transformers pillow
\`\`\`

## Usage
\`\`\`bash
streamlit run app.py
\`\`\`

## Examples
![Example Image](generated_images/waterfall.png)

## License
MIT" > README.md; git add .; git commit -m "Add complete project with README"; git push origin main