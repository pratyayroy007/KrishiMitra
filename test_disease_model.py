"""Krishi Mitra: Offline & Real-Time Disease Detection Model Verification Script
Usage:
  python test_disease_model.py                 # Runs verification test on a sample leaf
  python test_disease_model.py path/to/leaf.jpg  # Tests your own custom leaf image
"""

import os
import sys
import base64
from PIL import Image, ImageDraw

# Add current directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from services.disease_service import disease_service


def create_sample_leaf():
    """Creates a synthetic test leaf specimen with chlorotic fungal lesions."""
    img = Image.new("RGB", (300, 300), color=(18, 36, 27))
    draw = ImageDraw.Draw(img)

    # Draw leaf blade (oval green shape)
    draw.ellipse([50, 40, 250, 260], fill=(46, 117, 89), outline=(116, 198, 157), width=3)

    # Draw main vein and side veins
    draw.line([150, 40, 150, 260], fill=(168, 218, 181), width=3)
    draw.line([150, 100, 90, 80], fill=(168, 218, 181), width=2)
    draw.line([150, 100, 210, 80], fill=(168, 218, 181), width=2)
    draw.line([150, 150, 80, 130], fill=(168, 218, 181), width=2)
    draw.line([150, 150, 220, 130], fill=(168, 218, 181), width=2)

    # Draw fungal lesion spots (Target board rings / Early Blight simulation)
    draw.ellipse([90, 110, 130, 150], fill=(138, 79, 43), outline=(218, 165, 32), width=3)
    draw.ellipse([100, 120, 120, 140], fill=(59, 29, 13))

    draw.ellipse([170, 160, 205, 195], fill=(138, 79, 43), outline=(218, 165, 32), width=2)
    draw.ellipse([178, 168, 197, 187], fill=(59, 29, 13))

    os.makedirs("test_samples", exist_ok=True)
    sample_path = os.path.join("test_samples", "sample_test_leaf.png")
    img.save(sample_path)
    return sample_path


def main():
    print("=" * 65)
    print(" 🌾 KRISHI MITRA: PLANT DISEASE VISION MODEL VERIFICATION")
    print("=" * 65)

    if disease_service.pytorch_model is not None:
        print(f"✅ Active Engine : Local PyTorch MobileNetV3 ({len(disease_service.class_indices)} Disease Classes)")
    else:
        print("⚠️ Active Engine : Gemini Vision Fallback (Local model weights not found)")

    # Choose image to test
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        test_img_path = sys.argv[1]
        print(f"📷 Testing Image: {test_img_path}")
    else:
        test_img_path = create_sample_leaf()
        print(f"📷 Testing Image: Created specimen at {test_img_path}")

    # Convert image to base64
    with open(test_img_path, "rb") as f:
        b64_str = base64.b64encode(f.read()).decode("utf-8")

    # Run inference through disease service
    result = disease_service.analyze_image_base64(b64_str)

    print("\n" + "-" * 65)
    print(" 🎯 DIAGNOSTIC RESULTS")
    print("-" * 65)
    print(f"  🌿 Crop Species   : {result.get('crop_name')}")
    print(f"  🔍 Health Status  : {result.get('condition')}")
    print(f"  🔬 Pathology      : {result.get('diagnosis')}")
    print(f"  📊 Confidence     : {result.get('confidence_percent')}%")
    print(f"  ⚙️ Model Source   : {result.get('source')}")
    print(f"\n  👁️ Visible Symptoms:\n     {result.get('symptoms')}")
    print(f"\n  💊 Actionable Remedy / Fungicide:\n     {result.get('treatment')}")
    print(f"\n  🛡️ Long-term Cultural Prevention:\n     {result.get('prevention')}")
    print("=" * 65)


if __name__ == "__main__":
    main()
