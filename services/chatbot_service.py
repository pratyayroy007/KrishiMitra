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
        "keywords": [
            "blast", "rice blast", "magnaporthe", "spindle lesion", "paddy blast", "neck blast", "rice", "paddy",
            "धान", "चावल", "झुलसा", "ब्लास्ट", "गर्दन तोड़",
            "ধান", "ব্লাস্ট", "শীষ ব্লাস্ট", "পাতা পোড়া", "চাল", "ধানের",
            "వరి", "బ్లాస్ట్", "అగ్గి తెగులు", "మెడ విరుపు", "వరి ధాన్యం",
            "भात", "करपा", "तांदूळ", "ब्लास्ट रोग", "भाताचा",
            "நெல்", "குலை நோய்", "அரிசி", "இலை கருகல்", "நெற்பயிர்"
        ],
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
        "keywords": [
            "npk", "nitrogen", "phosphorus", "potassium", "fertilizer", "soil health", "urea", "dap", "dose", "nutrient",
            "एनपीके", "नाइट्रोजन", "फास्फोरस", "पोटाश", "उर्वरक", "खाद", "यूरिया", "डीएपी", "मिट्टी की सेहत", "पोषक तत्व",
            "সার", "নাইট্রোজেন", "ফসফরাস", "পটাশ", "ইউরিয়া", "ডিএপি", "মাটির স্বাস্থ্য", "পুষ্টি উপাদান", "এনপিকে",
            "ఎరువులు", "నత్రజని", "భాస్వరం", "పొటాష్", "యూరియా", "భూసారం", "పోషకాలు",
            "खते", "नत्र", "स्फुरद", "पालाश", "युरिया", "मातीचे आरोग्य", "पोषण",
            "உரம்", "தழைச்சத்து", "மணிச்சத்து", "சாம்பல்சத்து", "யூரியா", "மண் வளம்", "ஊட்டச்சத்து"
        ],
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
        "keywords": [
            "ph", "acidic soil", "alkaline soil", "soil acidity", "saline soil", "lime", "gypsum", "soil",
            "पीएच", "अम्लीय मिट्टी", "क्षारीय मिट्टी", "मृदा", "चूना", "जिप्सम",
            "পিএইচ", "অম্লীয় মাটি", "ক্ষারীয় মাটি", "মাটির অম্লতা", "চুন", "জিপসাম", "মাটি",
            "పీహెచ్", "ఆమ్ల నేల", "క్షార నేల", "భూమి", "సున్నం", "జిప్సం",
            "पीएच", "आम्लधर्मी जमीन", "क्षारयुक्त जमीन", "माती", "सुना", "जिप्सम",
            "மண் கார அமில நிலை", "அமில மண்", "கார மண்", "மண்", "சுண்ணாம்பு"
        ],
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
        "keywords": [
            "tomato", "early blight", "late blight", "alternaria", "phytophthora", "leaf spot", "damping off",
            "टमाटर", "अगेती झुलसा", "पछेती झुलसा", "पत्ती धब्बा",
            "টমেটো", "ব্লাইট", "নাভি ধসা", "আগাম ধসা", "পাতার দাগ",
            "టమోటా", "ఆకు మచ్చ తెగులు", "మాడు తెగులు",
            "टोमॅटो", "करपा", "पानावरील डाग",
            "தக்காளி", "இலைப்புள்ளி", "கருகல் நோய்"
        ],
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
        "keywords": [
            "cotton", "bollworm", "whitefly", "pink bollworm", "leaf curl", "pest control", "insect", "bug",
            "कपास", "गुलाबी सुंडी", "सफेद मक्खी", "कीट", "कीड़ा",
            "তুলা", "কীটপতঙ্গ", "সাদা মাছি", "লেদা পোকা", "পোকা দমন",
            "పత్తి", "గులాబీ రంగు పురుగు", "తెల్లదోమ", "పురుగులు",
            "कापूस", "बोंडअळी", "पांढरी माशी", "कीड",
            "பருத்தி", "காய் புழு", "வெள்ளை ஈ", "பூச்சி"
        ],
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
        "keywords": [
            "irrigation", "water", "drip", "sprinkler", "water saving", "drought", "moisture",
            "सिंचाई", "ड्रिप", "फव्वारा", "पानी", "टपक सिंचाई", "नमी",
            "সেচ", "ড্রিপ সেচ", "জল সাশ্রয়", "পানি", "সেচ ব্যবস্থা",
            "నీటిపారుదల", "బిందు సేద్యం", "స్ప్రింక్లర్", "నీరు", "తేమ",
            "ठिबक सिंचन", "तुषार सिंचन", "पाणी नियोजन", "ओलावा",
            "சொட்டு நீர் பாசனம்", "தெளிப்பு நீர் பாசனம்", "பாசனம்", "ஈரப்பதம்"
        ],
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


from services.translation_service import (
    get_prompt_language_instruction,
    get_localized_kb_entry,
    SUPPORTED_LANGUAGES
)


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

    def answer_query(self, query: str, crop_context: Optional[str] = None, lang: str = "en") -> Dict[str, Any]:
        """Processes agricultural query and returns response, tags, and action items in requested language."""
        clean_q = query.strip()
        lang = lang.lower() if lang else "en"
        if lang not in SUPPORTED_LANGUAGES:
            lang = "en"

        if not clean_q:
            empty_msg = {
                "en": "Please enter an agricultural question regarding crops, soil health, fertilizers, or diseases.",
                "hi": "कृपया फसलों, मिट्टी के स्वास्थ्य, उर्वरकों या रोगों के बारे में एक कृषि प्रश्न दर्ज करें।",
                "bn": "অনুগ্রহ করে ফসল, মাটির স্বাস্থ্য, সার বা রোগ সম্পর্কিত একটি কৃষি প্রশ্ন জিজ্ঞাসা করুন।",
                "te": "దయచేసి పంటలు, భూసారం, ఎరువులు లేదా తెగుళ్ళకు సంబంధించి ఒక వ్యవసాయ ప్రశ్నను అడగండి.",
                "mr": "कृपया पिके, मातीचे आरोग्य, खते किंवा रोगांविषयी एक कृषी प्रश्न विचारा.",
                "ta": "பயிர்கள், மண் வளம், உரங்கள் அல்லது நோய்கள் பற்றிய வேளாண் கேள்வியைக் கேட்கவும்."
            }
            return {
                "response": empty_msg.get(lang, empty_msg["en"]),
                "context_tags": ["#KrishiMitra"],
                "action_recommendation": None,
                "model": "rule-based"
            }

        # 1. Try Gemini GenAI if configured
        if self.client:
            try:
                lang_instruction = get_prompt_language_instruction(lang)
                system_instruction = (
                    "You are 'Krishi Mitra AI Copilot', an expert agricultural extension advisor for Indian farmers. "
                    "Your advice is grounded in ICAR (Indian Council of Agricultural Research), Package-of-Practices (PoP), "
                    "and integrated pest/soil management guidelines. "
                    "Provide practical, scientific, yet easy-to-understand advice. "
                    "Include: (1) Main explanation, (2) Key Actionable Steps, (3) Mention safe dosages and non-chemical IPM options where relevant. "
                    "Keep answers concise, direct, and farmer-friendly.\n\n"
                    f"{lang_instruction}"
                )

                prompt = f"Farmer Query: {clean_q}"
                if crop_context:
                    prompt += f"\nActive Recommended Crop: {crop_context}"

                import concurrent.futures

                def _call_gemini():
                    return self.client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=prompt,
                        config={
                            "system_instruction": system_instruction,
                            "temperature": 0.3,
                            "max_output_tokens": 600,
                        }
                    )

                executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
                try:
                    future = executor.submit(_call_gemini)
                    response = future.result(timeout=8.0)
                finally:
                    executor.shutdown(wait=False, cancel_futures=True)

                text = response.text or ""
                # Extract tags and recommendations heuristically
                tags = ["#KrishiMitra", "#PoPAdvisory"]
                if "rice" in clean_q.lower() or "धान" in clean_q or "ধান" in clean_q or "వరి" in clean_q: tags.append("#Paddy")
                if "wheat" in clean_q.lower() or "गेहूं" in clean_q or "গম" in clean_q: tags.append("#Wheat")
                if "fertilizer" in clean_q.lower() or "npk" in clean_q.lower() or "खाद" in clean_q or "সার" in clean_q: tags.append("#NutrientManagement")
                if "disease" in clean_q.lower() or "रोग" in clean_q or "রোগ" in clean_q or "తెగులు" in clean_q: tags.append("#CropProtection")

                action_notes = {
                    "en": "Consult local Krishi Vigyan Kendra (KVK) or package of practices for region-specific micro-variations.",
                    "hi": "क्षेत्र-विशिष्ट सूक्ष्म विविधताओं के लिए स्थानीय कृषि विज्ञान केंद्र (KVK) से परामर्श लें।",
                    "bn": "অঞ্চলভিত্তিক সুনির্দিষ্ট পরামর্শের জন্য স্থানীয় কৃষি বিজ্ঞান কেন্দ্র (KVK)-এর সাথে যোগাযোগ করুন।",
                    "te": "ప్రాంతీయ నిర్దిష్ట సలహాల కోసం స్థానిక కృషి విజ్ఞాన కేంద్రం (KVK) ని సంప్రదించండి.",
                    "mr": "स्थानिक सूक्ष्म हवामान बदलांसाठी स्थानिक कृषी विज्ञान केंद्राशी (KVK) संपर्क साधा.",
                    "ta": "மண்டல அளவிலான மாற்றங்களுக்கு உங்கள் உள்ளூர் வேளாண் அறிவியல் மையத்தை (KVK) அணுகவும்."
                }

                return {
                    "response": text,
                    "context_tags": tags,
                    "action_recommendation": action_notes.get(lang, action_notes["en"]),
                    "model": "gemini-3.8-flash (Live GenAI)",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"GenAI call error: {e}. Falling back to domain knowledge base.")

        # 2. Domain Knowledge Base Fallback
        q_lower = clean_q.lower()
        for key, entry in AGRICULTURAL_KNOWLEDGE_BASE.items():
            if any(k in q_lower for k in entry["keywords"]):
                loc_entry = get_localized_kb_entry(key, entry, lang)
                return {
                    "response": loc_entry["answer"],
                    "context_tags": [f"#{t}" for t in entry["context_tags"]],
                    "action_recommendation": loc_entry["action_recommendation"],
                    "model": "KrishiMitra Agricultural Knowledge Base (PoP)",
                    "status": "success"
                }

        # 3. Intelligent default response
        default_responses = {
            "en": (
                f"Thank you for consulting Krishi Mitra regarding '{clean_q}'. "
                "For optimal crop productivity, we recommend maintaining soil organic carbon above 0.5%, "
                "performing seasonal soil health card testing, and adhering to certified seed rates and spacing. "
                "You can also use our Crop Recommendation tool and Field Camera scanner above to diagnose specific symptoms."
            ),
            "hi": (
                f"'{clean_q}' के संबंध में कृषि मित्र से संपर्क करने के लिए धन्यवाद। "
                "उत्तम फसल उत्पादकता के लिए, हम मिट्टी में जैविक कार्बन 0.5% से ऊपर बनाए रखने, "
                "नियमित मृदा स्वास्थ्य कार्ड (Soil Health Card) परीक्षण कराने और प्रमाणित बीजों का उचित दूरी पर उपयोग करने की सलाह देते हैं।"
            ),
            "bn": (
                f"'{clean_q}' সংক্রান্ত জিজ্ঞাসার জন্য কৃষি মিত্রকে ধন্যবাদ। "
                "সর্বোত্তম ফলনের জন্য মাটির জৈব কার্বন ০.৫% এর ওপরে রাখা, নিয়মিত মাটি পরীক্ষা করানো "
                "এবং প্রত্যয়িত বীজের সঠিক দূরত্বে বপন নিশ্চিত করার পরামর্শ দেওয়া হচ্ছে।"
            ),
            "te": (
                f"'{clean_q}' గురించి కృషి మిత్రను సంప్రదించినందుకు ధన్యవాదాలు. "
                "ఉత్తమ దిగుబడి కోసం భూమిలో సేంద్రీయ కర్బనాన్ని 0.5% కంటే ఎక్కువగా ఉంచడం, "
                "భూసార పరీక్షలు చేయించడం మరియు నాణ్యమైన విత్తనాలను సరైన దూరంలో నాటడం అవసరం."
            ),
            "mr": (
                f"'{clean_q}' बाबत कृषी मित्राचा सल्ला घेतल्याबद्दल धन्यवाद. "
                "उत्कृष्ट उत्पादनासाठी जमिनीतील सेंद्रिय कर्ब ०.५% पेक्षा जास्त ठेवणे, "
                "माती परीक्षण करणे आणि प्रमाणित बियाण्यांचा योग्य अंतरावर वापर करणे आवश्यक आहे."
            ),
            "ta": (
                f"'{clean_q}' குறித்த கேள்விக்கு நன்றி. "
                "சிறந்த விளைச்சலுக்கு மண்ணில் கரிம கார்பன் அளவை 0.5% மேல் பராமரித்தல், "
                "மண் பரிசோதனை அட்டை பெறுதல் மற்றும் சான்றளிக்கப்பட்ட விதைகளைப் பயன்படுத்துவது அவசியமாகும்."
            )
        }

        default_actions = {
            "en": "Perform a standard soil test (N, P, K, Organic Carbon, pH) before applying basal fertilizers.",
            "hi": "उर्वरक देने से पहले मिट्टी की मानक जांच (N, P, K, जैविक कार्बन, pH) अवश्य करवाएं।",
            "bn": "সার প্রয়োগের পূর্বে মাটির সাধারণ স্বাস্থ্য পরীক্ষা (N, P, K, জৈব কার্বন, pH) করিয়ে নিন।",
            "te": "ఎరువులు వేయడానికి ముందు ప్రాథమిక భూసార పరీక్ష (N, P, K, pH) చేయించుకోండి.",
            "mr": "रासायनिक खते देण्यापूर्वी मातीची मूलभूत तपासणी (N, P, K, pH) करून घ्यावी.",
            "ta": "உரமிடுவதற்கு முன் மண்ணின் அடிப்படை பரிசோதனையை (N, P, K, pH) செய்து கொள்ளவும்."
        }

        return {
            "response": default_responses.get(lang, default_responses["en"]),
            "context_tags": ["#KrishiMitra", "#GeneralAdvisory", "#SoilHealth"],
            "action_recommendation": default_actions.get(lang, default_actions["en"]),
            "model": "KrishiMitra Agronomic Expert",
            "status": "success"
        }

copilot_service = KrishiMitraCopilotService()
