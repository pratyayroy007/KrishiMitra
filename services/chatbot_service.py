"""Krishi Mitra AI Agricultural Extension Copilot Service
Adapted from Caterpillar Copilot Service.
Grounded on:
- ICAR and State Agricultural Universities Package-of-Practices (PoP)
- Soil Fertility Management (N-P-K, pH, Micronutrients)
- Integrated Pest Management (IPM) & Crop Disease Protocols
- Live Google GenAI integration with offline agronomic fallback
"""

import os
import re
import json
import logging
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Fallback Grounded Agricultural Knowledge Base
AGRICULTURAL_KNOWLEDGE_BASE = {
    "rice_blast": {
        "keywords": ["blast", "rice blast", "magnaporthe", "spindle lesion", "paddy blast", "neck blast"],
        "answer": (
            "Rice Blast (caused by Magnaporthe oryzae) produces spindle-shaped lesions with grayish centers "
            "and brown margins on leaves, and blackening at node/neck joints. High relative humidity (>90%) "
            "and excessive Nitrogen application exacerbate blast incidence."
        ),
        "action_recommendation": (
            "1. Spray Tricyclazole 75% WP @ 0.6 g/L or Kasugamycin 3% SL @ 2.5 mL/L.\n"
            "2. Avoid excessive top-dressing of urea; balance with Potash (MOP).\n"
            "3. Maintain field drainage during cloudy humid weather."
        ),
        "context_tags": ["Paddy", "FungalDisease", "BlastManagement", "IPM"]
    },
    "soil_npk": {
        "keywords": ["npk", "nitrogen", "phosphorus", "potassium", "fertilizer", "soil health", "urea", "dap"],
        "answer": (
            "Balanced fertilizer application depends on soil test values. Standard general recommendations:\n"
            "- Cereal crops (Rice, Wheat, Maize): 120:60:40 kg/ha (N:P2O5:K2O).\n"
            "- Pulses (Gram, Moong, Arhar): 20:50:20 kg/ha (pulses fix atmospheric N).\n"
            "- Oilseeds (Mustard, Groundnut): 80:40:40 kg/ha with 20 kg Sulphur."
        ),
        "action_recommendation": (
            "Apply entire Phosphorus and Potassium along with 1/3rd Nitrogen at basal sowing. "
            "Split remaining Nitrogen at tillering/vegetative and panicle/flowering stages."
        ),
        "context_tags": ["SoilHealth", "NPKRatio", "NutrientManagement", "Fertilizer"]
    },
    "soil_ph": {
        "keywords": ["ph", "acidic soil", "alkaline soil", "soil acidity", "saline soil", "lime", "gypsum"],
        "answer": (
            "Optimal soil pH for most crops is 6.0 to 7.5. "
            "Acidic soils (pH < 6.0) restrict Phosphorus and Magnesium availability, while alkaline soils (pH > 8.0) "
            "induce Zinc and Iron chlorosis."
        ),
        "action_recommendation": (
            "For acidic soils: Incorporate agricultural lime (CaCO3) @ 2–4 quintals/acre based on soil acidity. "
            "For sodic/alkaline soils: Apply agricultural Gypsum (CaSO4) followed by leaching with fresh water."
        ),
        "context_tags": ["SoilpH", "SoilReclamation", "LimeGypsum", "Agronomy"]
    },
    "tomato_blight": {
        "keywords": ["tomato", "early blight", "late blight", "alternaria", "phytophthora", "leaf spot"],
        "answer": (
            "Tomato Late Blight (Phytophthora infestans) causes water-soaked pale lesions turning dark brown/purplish, "
            "with white fungal bloom under leaf surfaces during cool humid weather. "
            "Early Blight (Alternaria solani) causes target-board concentric ring spots on older leaves."
        ),
        "action_recommendation": (
            "1. Spray Metalaxyl-M + Mancozeb @ 2 g/L or Cymoxanil + Mancozeb for late blight.\n"
            "2. Ensure wide plant spacing (60 x 45 cm) and staking to reduce humidity around canopy.\n"
            "3. Destroy infected crop debris after harvest."
        ),
        "context_tags": ["Horticulture", "Tomato", "BlightControl", "Fungicide"]
    },
    "cotton_pest": {
        "keywords": ["cotton", "bollworm", "whitefly", "pink bollworm", "leaf curl", "pest control"],
        "answer": (
            "Cotton is prone to Pink Bollworm (Pectinophora gossypiella) and Whitefly (Bemisia tabaci), "
            "which also vectors Cotton Leaf Curl Virus (CLCuV). High sucking pest pressure leads to honeydew "
            "and sooty mold on lint."
        ),
        "action_recommendation": (
            "1. Install Pheromone Traps @ 5 traps/acre for monitoring Pink Bollworm moth activity.\n"
            "2. For whitefly: Spray Neem Oil (10,000 ppm) @ 2 mL/L or Diafenthiuron 50% WP @ 1.2 g/L.\n"
            "3. Avoid indiscriminate synthetic pyrethroid sprays to preserve natural predatory bugs."
        ),
        "context_tags": ["CashCrops", "Cotton", "IPM", "PheromoneTraps"]
    },
    "drip_irrigation": {
        "keywords": ["irrigation", "water", "drip", "sprinkler", "water saving", "drought", "moisture"],
        "answer": (
            "Micro-irrigation (Drip & Sprinkler) saves 30–50% water while improving fertilizer use efficiency (fertigation) "
            "by 25–35%. Critical moisture stages: Crown root initiation in wheat, flowering/pod filling in pulses, "
            "and grain filling in rice."
        ),
        "action_recommendation": (
            "Apply water scheduling based on critical growth stages. "
            "Adopt fertigation using 100% water-soluble fertilizers (19:19:19, 0:52:34) via drip lines."
        ),
        "context_tags": ["Irrigation", "DripSystem", "WaterManagement", "Fertigation"]
    }
}


class KrishiMitraCopilotService:
    def __init__(self):
        self.client = None
        self._init_genai()

    def _init_genai(self):
        if GEMINI_API_KEY:
            try:
                from google import genai
                self.client = genai.Client(api_key=GEMINI_API_KEY)
                logger.info("Krishi Mitra Copilot initialized with Google GenAI client.")
            except Exception as e:
                logger.warning(f"Failed to initialize GenAI client: {e}")
                self.client = None

    def answer_query(self, query: str, crop_context: Optional[str] = None) -> Dict[str, Any]:
        """Processes agricultural query and returns response, tags, and action items."""
        clean_q = query.strip()
        if not clean_q:
            return {
                "response": "Please enter an agricultural question regarding crops, soil health, fertilizers, or diseases.",
                "context_tags": ["#KrishiMitra"],
                "action_recommendation": None,
                "model": "rule-based"
            }

        # 1. Try Gemini GenAI if configured
        if self.client:
            try:
                system_instruction = (
                    "You are 'Krishi Mitra AI Copilot', an expert agricultural extension advisor for Indian farmers. "
                    "Your advice is grounded in ICAR (Indian Council of Agricultural Research), Package-of-Practices (PoP), "
                    "and integrated pest/soil management guidelines. "
                    "Provide practical, scientific, yet easy-to-understand advice. "
                    "Include: (1) Main explanation, (2) Key Actionable Steps, (3) Mention safe dosages and non-chemical IPM options where relevant. "
                    "Keep answers concise, direct, and farmer-friendly."
                )

                prompt = f"Farmer Query: {clean_q}"
                if crop_context:
                    prompt += f"\nActive Recommended Crop: {crop_context}"

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config={
                        "system_instruction": system_instruction,
                        "temperature": 0.3,
                        "max_output_tokens": 600,
                    }
                )

                text = response.text or ""
                # Extract tags and recommendations heuristically
                tags = ["#KrishiMitra", "#PoPAdvisory"]
                if "rice" in clean_q.lower() or "paddy" in clean_q.lower(): tags.append("#Paddy")
                if "wheat" in clean_q.lower(): tags.append("#Wheat")
                if "fertilizer" in clean_q.lower() or "npk" in clean_q.lower(): tags.append("#NutrientManagement")
                if "disease" in clean_q.lower() or "leaf" in clean_q.lower(): tags.append("#CropProtection")
                if "weather" in clean_q.lower() or "rain" in clean_q.lower(): tags.append("#AgroClimate")

                return {
                    "response": text,
                    "context_tags": tags,
                    "action_recommendation": "Consult local Krishi Vigyan Kendra (KVK) or package of practices for region-specific micro-variations.",
                    "model": "gemini-2.5-flash (Live GenAI)",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"GenAI call error: {e}. Falling back to domain knowledge base.")

        # 2. Domain Knowledge Base Fallback
        q_lower = clean_q.lower()
        for key, entry in AGRICULTURAL_KNOWLEDGE_BASE.items():
            if any(k in q_lower for k in entry["keywords"]):
                return {
                    "response": entry["answer"],
                    "context_tags": [f"#{t}" for t in entry["context_tags"]],
                    "action_recommendation": entry["action_recommendation"],
                    "model": "KrishiMitra Agricultural Knowledge Base (PoP)",
                    "status": "success"
                }

        # 3. Intelligent default response
        return {
            "response": (
                f"Thank you for consulting Krishi Mitra regarding '{clean_q}'. "
                "For optimal crop productivity, we recommend maintaining soil organic carbon above 0.5%, "
                "performing seasonal soil health card testing, and adhering to certified seed rates and spacing. "
                "You can also use our Crop Recommendation tool and Field Camera scanner above to diagnose specific symptoms."
            ),
            "context_tags": ["#KrishiMitra", "#GeneralAdvisory", "#SoilHealth"],
            "action_recommendation": "Perform a standard soil test (N, P, K, Organic Carbon, pH) before applying basal fertilizers.",
            "model": "KrishiMitra Agronomic Expert",
            "status": "success"
        }

copilot_service = KrishiMitraCopilotService()
