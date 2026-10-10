import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from services.translation_service import (
    SUPPORTED_LANGUAGES,
    get_localized_disease_info,
    get_localized_kb_entry,
    get_prompt_language_instruction
)
from services.chatbot_service import copilot_service
from services.disease_service import disease_service
from app import app
import json

print("=================================================================")
print(" 🌐 KRISHI MITRA: REGIONAL LANGUAGES MODULE VERIFICATION")
print("=================================================================")

print("\n1. Supported Indian Languages:")
for code, meta in SUPPORTED_LANGUAGES.items():
    print(f"   [{code}] {meta['name']} - {meta['native']} (Speech tag: {meta['speech_code']})")

print("\n2. Disease Diagnosis Localization (Sample: Tomato Early Blight):")
sample_raw = {
    'crop': 'Tomato',
    'condition': 'Fungal Disease',
    'diagnosis': 'Tomato Early Blight',
    'symptoms': 'Concentric rings',
    'treatment': 'Spray Mancozeb',
    'prevention': 'Mulch base'
}
for lang in ['hi', 'bn', 'te', 'mr', 'ta']:
    info = get_localized_disease_info('Tomato___Early_blight', sample_raw, lang=lang)
    print(f"   • [{lang.upper()}] {info['crop']} -> {info['diagnosis']}")
    print(f"     💊 {info['treatment']}")

print("\n3. Copilot Advisory in Regional Languages:")
for q, lang, title in [
    ("rice blast", "hi", "Hindi Query (धान ब्लास्ट)"),
    ("npk fertilizer", "bn", "Bengali Query (সার ব্যবস্থাপনা)"),
    ("rice blast", "te", "Telugu Query (వరి అగ్గితెగులు)")
]:
    res = copilot_service.answer_query(q, lang=lang)
    print(f"   • {title}:")
    print(f"     💬 {res['response'][:90]}...")
    if res.get('action_recommendation'):
        print(f"     ⚡ {res['action_recommendation'][:80]}...")

print("\n4. Flask API Endpoint Verification (/api/chat and /api/scan_leaf):")
with app.test_client() as client:
    # Test /api/chat with Hindi
    chat_resp = client.post('/api/chat', json={'query': 'rice blast', 'lang': 'hi'})
    assert chat_resp.status_code == 200, f"Chat failed: {chat_resp.status_code}"
    chat_data = chat_resp.get_json()
    assert "धान" in chat_data['response'], "Hindi text not found in response"
    print(f"   ✅ /api/chat [Hindi] Status: 200 OK | Received: {chat_data['response'][:45]}...")

    # Test /api/chat with Bengali
    chat_resp_bn = client.post('/api/chat', json={'query': 'npk', 'lang': 'bn'})
    assert chat_resp_bn.status_code == 200
    chat_data_bn = chat_resp_bn.get_json()
    assert "সার" in chat_data_bn['response'], "Bengali text not found in response"
    print(f"   ✅ /api/chat [Bengali] Status: 200 OK | Received: {chat_data_bn['response'][:45]}...")

print("\n=================================================================")
print(" 🎉 REGIONAL LANGUAGES VERIFICATION PASSED SUCCESSFULLY!")
print("=================================================================")
