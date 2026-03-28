import streamlit as st
import torch
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
from PIL import Image
import io
import time

# Configure page
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 AI Image Generator with Stable Diffusion")
st.markdown("Generate stunning images from text descriptions using AI")

# Cache the model to avoid reloading
@st.cache_resource
def load_model():
    """Load and cache the Stable Diffusion model"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    with st.spinner("📥 Loading AI model... This may take a few minutes on first run."):
        model_id = "runwayml/stable-diffusion-v1-5"
        
        # Load pipeline
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            safety_checker=None,  # Disable safety checker for faster loading
            requires_safety_checker=False
        )
        
        # Use Euler Ancestral scheduler for better quality
        pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
        
        # Move to device
        if device == "cuda":
            pipe = pipe.to(device)
            pipe.enable_attention_slicing()  # Save memory
        else:
            pipe.to(device)
        
        return pipe, device

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("---")
    
    # Model info
    st.info("🤖 Model: Stable Diffusion v1.5")
    
    st.markdown("---")
    
    # Generation parameters
    st.subheader("🎛️ Generation Parameters")
    
    num_steps = st.slider(
        "Inference Steps",
        min_value=20,
        max_value=50,
        value=30,
        step=1,
        help="More steps = better quality but slower. 20-35 is recommended."
    )
    
    guidance_scale = st.slider(
        "Guidance Scale",
        min_value=5.0,
        max_value=15.0,
        value=7.5,
        step=0.5,
        help="Higher = follows prompt more closely. 5-9 is recommended."
    )
    
    st.markdown("---")
    
    # Image size
    st.subheader("📐 Image Size")
    col1, col2 = st.columns(2)
    with col1:
        height = st.selectbox("Height", [512, 768, 1024], index=0)
    with col2:
        width = st.selectbox("Width", [512, 768, 1024], index=0)
    
    st.markdown("---")
    
    # Random seed
    seed = st.number_input(
        "🎲 Random Seed",
        value=42,
        step=1,
        help="Same seed = reproducible results. -1 for random."
    )
    
    st.markdown("---")
    
    # Tips
    with st.expander("💡 Tips for better results"):
        st.markdown("""
        - **Be specific** in your prompts
        - Include **style keywords**: *photorealistic*, *cinematic lighting*, *oil painting*
        - Use **negative prompts** to avoid unwanted elements
        - Try different **seeds** for variations
        - More **steps** = better quality but slower
        - Higher **guidance** = closer to prompt but may reduce creativity
        """)

# Main content area
st.markdown("## 📝 Enter Your Prompt")

# Prompt inputs
col1, col2 = st.columns(2)

with col1:
    prompt = st.text_area(
        "✨ Positive Prompt",
        value="ultra-detailed portrait of a red fox wearing a tiny scarf, cinematic lighting, 35mm photography, shallow depth of field",
        height=150,
        help="Describe what you want to generate"
    )

with col2:
    negative_prompt = st.text_area(
        "🚫 Negative Prompt",
        value="blurry, low resolution, jpeg artifacts, extra fingers, deformed hands, text, watermark, ugly, out of frame",
        height=150,
        help="Describe what you want to avoid in the image"
    )

# Advanced options
with st.expander("🔧 Advanced Options"):
    st.markdown("These are advanced settings. The defaults work well for most cases.")
    
    col_adv1, col_adv2 = st.columns(2)
    with col_adv1:
        eta = st.slider(
            "ETA (Noise multiplier)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            step=0.1,
            help="Controls noise addition. 0 = deterministic, 1 = more random"
        )
    with col_adv2:
        use_attention_slicing = st.checkbox(
            "Enable Attention Slicing",
            value=True,
            help="Reduces memory usage (recommended for GPU)"
        )

# Generate button
generate_btn = st.button("🚀 Generate Image", type="primary", use_container_width=True)

# Result area
if generate_btn:
    if not prompt.strip():
        st.error("❌ Please enter a prompt!")
    else:
        try:
            # Load model
            pipe, device = load_model()
            
            # Enable attention slicing if selected
            if use_attention_slicing and device == "cuda":
                pipe.enable_attention_slicing()
            
            # Set seed
            generator = None
            if seed != -1:
                generator = torch.Generator(device=device).manual_seed(seed)
            
            # Progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Generate image
            status_text.text("🎨 Generating image... This may take 10-30 seconds...")
            
            start_time = time.time()
            
            with st.spinner("Creating your masterpiece..."):
                image = pipe(
                    prompt=prompt,
                    negative_prompt=negative_prompt if negative_prompt else None,
                    num_inference_steps=num_steps,
                    guidance_scale=guidance_scale,
                    height=height,
                    width=width,
                    generator=generator,
                    eta=eta
                ).images[0]
            
            elapsed_time = time.time() - start_time
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            # Display result
            st.success(f"✅ Image generated successfully in {elapsed_time:.1f} seconds!")
            
            # Show image
            st.markdown("### 🖼️ Generated Image")
            col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
            with col_img2:
                st.image(image, use_container_width=True)
            
            # Download button
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)
            
            st.download_button(
                label="💾 Download Image",
                data=buf,
                file_name=f"generated_image_{int(time.time())}.png",
                mime="image/png",
                use_container_width=True
            )
            
            # Show generation info
            with st.expander("ℹ️ Generation Info"):
                st.json({
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "steps": num_steps,
                    "guidance_scale": guidance_scale,
                    "resolution": f"{width}x{height}",
                    "seed": seed,
                    "time_taken": f"{elapsed_time:.1f} seconds",
                    "device": device.upper()
                })
                
        except Exception as e:
            st.error(f"❌ Error generating image: {str(e)}")
            st.info("💡 Try reducing the resolution or inference steps if you're running out of memory.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
    Made with ❤️ Jaikar Ramu
    </div>
    """,
    unsafe_allow_html=True
)