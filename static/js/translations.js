/**
 * Krishi Mitra Regional Language Dictionaries & Voice Engine
 * Supported Languages:
 * - English (en)
 * - Hindi (hi) [हिन्दी]
 * - Bengali (bn) [বাংলা]
 * - Telugu (te) [తెలుగు]
 * - Marathi (mr) [मराठी]
 * - Tamil (ta) [தமிழ்]
 */

const KRISHI_TRANSLATIONS = {
    en: {
        code: "en",
        speechCode: "en-IN",
        name: "English",
        native: "English",
        nav: {
            title: "Krishi Mitra",
            badge: "AI EXTENSION AGENT",
            subtitle: "Smart Crop Intelligence • Computer Vision • PoP Advisory",
            btnCamera: "Field Camera Scanner",
            btnLive: "LIVE",
            btnCopilot: "AI Agri Copilot"
        },
        weather: {
            title: "Live Agro-Climate Intelligence",
            tag: "POWERED BY OPEN-METEO",
            subtitle: "Real-time hyper-local temperature, humidity, rainfall & 5-day farming advisory",
            placeholder: "District / City (e.g. Pune, Ludhiana)",
            btnFetch: "Fetch Weather",
            btnGPS: "📍 Detect GPS",
            quickSelect: "Quick Select:",
            humidity: "Relative Humidity",
            rainfall: "Growing Rainfall",
            wind: "Wind Velocity",
            sprayingTitle: "🧪 Spraying Advisory",
            irrigationTitle: "💧 Irrigation Advisory",
            forecastTitle: "5-Day Agricultural Forecast",
            btnAutoFill: "⚡ Auto-Fill This Climate into Crop Form",
            toastApplied: "✓ Parameters injected into form!"
        },
        cropForm: {
            title: "Smart Crop Recommendation",
            subtitle: "Powered by Random Forest Model & Agro-Meteorological Inputs",
            soilSection: "🧪 Soil Nutrient Profile (kg/ha)",
            nitrogen: "Nitrogen (N)",
            phosphorus: "Phosphorus (P)",
            potassium: "Potassium (K)",
            ph: "Soil pH",
            climateSection: "🌦️ Climate & Atmospheric Conditions",
            temperature: "Temperature",
            humidity: "Humidity",
            rainfall: "Rainfall",
            btnPredict: "🌾 Predict Optimal Crop"
        },
        resultCard: {
            title: "Prediction Result",
            subtitle: "Agronomic Advisory Outcome",
            badge: "RECOMMENDED FOR CURRENT CONDITIONS",
            note: "This crop is mathematically optimal for your soil N-P-K balance, pH range, and local temperature/rainfall profile.",
            btnAskCopilot: "💬 Ask AI Copilot about practices",
            placeholder: "Fill in the soil and weather parameters and click Predict Optimal Crop to view recommendations."
        },
        pillars: {
            title: "Krishi Mitra Capabilities",
            p1Title: "Pillar 1: Leaf Disease Vision",
            p1Desc: "Real-time optical scanner with disease diagnosis & fungicide remedies.",
            p3Title: "Pillar 3: Grounded AI Advisory",
            p3Desc: "AI Extension Agent grounded on ICAR Package of Practices (PoP).",
            p2Title: "Pillar 2: Regional Yield Models",
            p2Desc: "Dimensionality-reduced agro-meteorological forecasting engine."
        },
        camera: {
            title: "Field & Leaf Optical Diagnostic Scanner",
            subtitle: "Unit: CAM-AGRI-01 • Sensor: CMOS Optical & Chlorophyll IR",
            tabWebcam: "Live Camera",
            tabSim: "Field Sample Mode",
            btnFilter: "🎨 Switch Filter: Plant Stress IR",
            btnUpload: "📁 Upload Leaf File",
            btnCapture: "📸 Capture Leaf & Diagnose",
            btnDone: "Done",
            symptomsTitle: "Visible Symptoms:",
            treatmentTitle: "Actionable Remedy / Fungicide:",
            btnListen: "🔊 Listen in Voice",
            btnStopVoice: "⏹ Stop Voice",
            scanning: "SCANNING & DIAGNOSING...",
            ready: "READY TO SCAN",
            analyzingUpload: "ANALYZING UPLOADED IMAGE..."
        },
        copilot: {
            title: "Krishi Mitra Agri Copilot",
            subtitle: "Grounded on ICAR & State SAU Package-of-Practices (PoP)",
            welcome: "Namaste! I am your AI Agricultural Extension Agent. Grounded in verified Package-of-Practices (PoP), soil nutrition science, and regional crop guidelines. How can I assist your farm today?",
            placeholder: "Ask about crops, pests, fertilizer dosages (or click 🎙️ to speak)...",
            btnSend: "Send",
            actionTitle: "🌿 Actionable Agricultural Recommendation:",
            listening: "🎙️ Listening... Please speak your question...",
            presets: [
                "What crop should I grow with soil pH 6.5 and high rainfall?",
                "How to control rice blast disease effectively?",
                "What are the recommended N-P-K fertilizer doses for wheat?",
                "Organic pest control for tomato leaf spot and fruit borer",
                "How does drip irrigation improve fertilizer use efficiency?"
            ]
        },
        crops: {
            Rice: "Rice (Paddy)",
            Maize: "Maize (Corn)",
            Chickpea: "Chickpea (Gram)",
            Kidneybeans: "Kidney Beans (Rajma)",
            Pigeonpeas: "Pigeon Peas (Arhar/Tur)",
            Mothbeans: "Moth Beans",
            Mungbean: "Mung Bean",
            Blackgram: "Black Gram (Urad)",
            Lentil: "Lentil (Masoor)",
            Pomegranate: "Pomegranate",
            Banana: "Banana",
            Mango: "Mango",
            Grapes: "Grapes",
            Watermelon: "Watermelon",
            Muskmelon: "Muskmelon",
            Apple: "Apple",
            Orange: "Orange",
            Papaya: "Papaya",
            Coconut: "Coconut",
            Cotton: "Cotton",
            Jute: "Jute",
            Coffee: "Coffee"
        }
    },

    hi: {
        code: "hi",
        speechCode: "hi-IN",
        name: "Hindi",
        native: "हिन्दी",
        nav: {
            title: "कृषि मित्र",
            badge: "एआई कृषि विस्तार एजेंट",
            subtitle: "स्मार्ट फसल बुद्धिमत्ता • कंप्यूटर विजन • पीक पैकेज ऑफ प्रैक्टिस परामर्श",
            btnCamera: "खेत कैमरा स्कैनर",
            btnLive: "लाइव",
            btnCopilot: "एआई कृषि साथी"
        },
        weather: {
            title: "सजीव कृषि-जलवायु बुद्धिमत्ता",
            tag: "ओपन-मेटियो द्वारा संचालित",
            subtitle: "स्थानीय तापमान, आर्द्रता, वर्षा और 5-दिवसीय कृषि परामर्श",
            placeholder: "जिला / शहर (उदा. पुणे, लुधियाना, पटना)",
            btnFetch: "मौसम प्राप्त करें",
            btnGPS: "📍 जीपीएस खोजें",
            quickSelect: "त्वरित चयन:",
            humidity: "सापेक्ष आर्द्रता",
            rainfall: "सक्रिय वर्षा",
            wind: "हवा की गति",
            sprayingTitle: "🧪 छिड़काव परामर्श",
            irrigationTitle: "💧 सिंचाई परामर्श",
            forecastTitle: "5-दिवसीय कृषि पूर्वानुमान",
            btnAutoFill: "⚡ यह जलवायु स्वतः फॉर्म में भरें",
            toastApplied: "✓ जलवायु विवरण फॉर्म में भर दिया गया!"
        },
        cropForm: {
            title: "स्मार्ट फसल अनुशंसा",
            subtitle: "रैंडम फॉरेस्ट मॉडल और कृषि-मौसम इनपुट द्वारा संचालित",
            soilSection: "🧪 मिट्टी पोषक तत्व प्रोफाइल (किग्रा/हेक्टेयर)",
            nitrogen: "नाइट्रोजन (N)",
            phosphorus: "फास्फोरस (P)",
            potassium: "पोटेशियम (K)",
            ph: "मृदा पीएच (pH)",
            climateSection: "🌦️ जलवायु और वायुमंडलीय स्थितियां",
            temperature: "तापमान",
            humidity: "आर्द्रता",
            rainfall: "वर्षा",
            btnPredict: "🌾 सर्वोत्तम फसल की भविष्यवाणी करें"
        },
        resultCard: {
            title: "अनुशंसा परिणाम",
            subtitle: "कृषि वैज्ञानिक परिणाम",
            badge: "वर्तमान परिस्थितियों के लिए सर्वोत्तम अनुशंसित",
            note: "यह फसल आपकी मिट्टी के N-P-K संतुलन, pH और स्थानीय तापमान/वर्षा के लिए गणितीय रूप से अनुकूलतम है।",
            btnAskCopilot: "💬 एआई कृषि साथी से कार्यप्रणाली पूछें",
            placeholder: "मिट्टी और मौसम के पैरामीटर भरें और परिणाम देखने के लिए 'सर्वोत्तम फसल की भविष्यवाणी करें' पर क्लिक करें।"
        },
        pillars: {
            title: "कृषि मित्र की क्षमताएं",
            p1Title: "स्तंभ 1: पत्ती रोग कंप्यूटर विजन",
            p1Desc: "पत्ती रोग पहचान और कवकनाशी उपचार के साथ रीयल-टाइम ऑप्टिकल स्कैनर।",
            p3Title: "स्तंभ 3: प्रामाणिक एआई परामर्शदाता",
            p3Desc: "भाकृअनुप (ICAR) पैकेज ऑफ प्रैक्टिस पर आधारित कृषि विस्तार एजेंट।",
            p2Title: "स्तंभ 2: क्षेत्रीय उपज मॉडल",
            p2Desc: "सटीक कृषि-मौसम आधारित उन्नत पूर्वानुमान इंजन।"
        },
        camera: {
            title: "खेत एवं पत्ती ऑप्टिकल नैदानिक स्कैनर",
            subtitle: "यूनिट: CAM-AGRI-01 • सेंसर: CMOS ऑप्टिकल और क्लोरोफिल IR",
            tabWebcam: "लाइव कैमरा",
            tabSim: "खेत नमूना मोड",
            btnFilter: "🎨 फिल्टर बदलें: पौध तनाव IR",
            btnUpload: "📁 पत्ती की फोटो अपलोड करें",
            btnCapture: "📸 पत्ती स्कैन करें और रोग पहचानें",
            btnDone: "पूर्ण",
            symptomsTitle: "दिखने वाले लक्षण:",
            treatmentTitle: "सुझाया गया रासायनिक / जैविक उपचार:",
            btnListen: "🔊 आवाज़ में सुनें",
            btnStopVoice: "⏹ आवाज़ रोकें",
            scanning: "स्कैनिंग और निदान जारी है...",
            ready: "स्कैन के लिए तैयार",
            analyzingUpload: "अपलोड की गई फोटो का विश्लेषण..."
        },
        copilot: {
            title: "कृषि मित्र एआई साथी (Copilot)",
            subtitle: "ICAR और राज्य कृषि विश्वविद्यालयों के पैकेज-ऑफ-प्रैक्टिस पर आधारित",
            welcome: "नमस्ते! मैं आपका एआई कृषि विस्तार एजेंट हूं। फसलों, मिट्टी की सेहत, खाद की मात्रा और कीट नियंत्रण में आपकी क्या मदद कर सकता हूँ?",
            placeholder: "फसल, खाद या कीट के बारे में पूछें (बोलने के लिए 🎙️ दबाएं)...",
            btnSend: "भेजें",
            actionTitle: "🌿 अनुशंसित कृषि कदम:",
            listening: "🎙️ सुन रहा हूँ... कृपया अपना सवाल बोलें...",
            presets: [
                "पीएच 6.5 और अधिक वर्षा वाली मिट्टी में कौन सी फसल उगाएं?",
                "धान के झुलसा (ब्लास्ट) रोग का प्रभावी नियंत्रण कैसे करें?",
                "गेहूं के लिए N-P-K उर्वरक की अनुशंसित खुराक क्या है?",
                "टमाटर के पत्ती धब्बा रोग का जैविक उपचार बताएं",
                "ड्रिप सिंचाई से खाद की बचत कैसे होती है?"
            ]
        },
        crops: {
            Rice: "चावल / धान",
            Maize: "मक्का (भुट्टा)",
            Chickpea: "चना",
            Kidneybeans: "राजमा",
            Pigeonpeas: "अरहर (तूर)",
            Mothbeans: "मोठ दाल",
            Mungbean: "मूंग दाल",
            Blackgram: "उड़द दाल",
            Lentil: "मसूर दाल",
            Pomegranate: "अनार",
            Banana: "केला",
            Mango: "आम",
            Grapes: "अंगूर",
            Watermelon: "तरबूज",
            Muskmelon: "खरबूजा",
            Apple: "सेब",
            Orange: "संतरा",
            Papaya: "पपीता",
            Coconut: "नारियल",
            Cotton: "कपास",
            Jute: "जूट (पटसन)",
            Coffee: "कॉफी"
        }
    },

    bn: {
        code: "bn",
        speechCode: "bn-IN",
        name: "Bengali",
        native: "বাংলা",
        nav: {
            title: "কৃষি মিত্র",
            badge: "এআই কৃষি সম্প্রসারণ এজেন্ট",
            subtitle: "স্মার্ট ফসল বুদ্ধিমত্তা • কম্পিউটার ভিশন • প্যাকেজ অফ প্র্যাকটিস পরামর্শ",
            btnCamera: "মাঠের ক্যামেরা স্ক্যানার",
            btnLive: "লাইভ",
            btnCopilot: "এআই কৃষি সহায়ক"
        },
        weather: {
            title: "সরাসরি কৃষি-আবহাওয়া তথ্য",
            tag: "ওপেন-মেটিও দ্বারা পরিচালিত",
            subtitle: "রিয়েল-টাইম স্থানীয় তাপমাত্রা, আর্দ্রতা, বৃষ্টিপাত এবং ৫ দিনের কৃষি পরামর্শ",
            placeholder: "জেলা / শহর (যেমন: বর্ধমান, কলকাতা, বাঁকুড়া)",
            btnFetch: "আবহাওয়া আনুন",
            btnGPS: "📍 জিপিএস সনাক্তকরণ",
            quickSelect: "দ্রুত নির্বাচন:",
            humidity: "আপেক্ষিক আর্দ্রতা",
            rainfall: "বৃষ্টিপাত",
            wind: "বাতাসের গতি",
            sprayingTitle: "🧪 স্প্রে সংক্রান্ত পরামর্শ",
            irrigationTitle: "💧 সেচ সংক্রান্ত পরামর্শ",
            forecastTitle: "৫ দিনের কৃষি আবহাওয়ার পূর্বাভাস",
            btnAutoFill: "⚡ এই আবহাওয়া ফর্মে যুক্ত করুন",
            toastApplied: "✓ আবহাওয়ার মান ফর্মে যুক্ত হয়েছে!"
        },
        cropForm: {
            title: "স্মার্ট ফসল সুপারিশ",
            subtitle: "র‍্যান্ডম ফরেস্ট মডেল ও কৃষি-আবহাওয়া বিশ্লেষণের মাধ্যমে পরিচালিত",
            soilSection: "🧪 মাটির পুষ্টিগুণ পরিমাপ (কেজি/হেক্টর)",
            nitrogen: "নাইট্রোজেন (N)",
            phosphorus: "ফসফরাস (P)",
            potassium: "পটাশিয়াম (K)",
            ph: "মাটির পিএইচ (pH)",
            climateSection: "🌦️ জলবায়ু ও পরিবেশগত অবস্থা",
            temperature: "তাপমাত্রা",
            humidity: "আর্দ্রতা",
            rainfall: "বৃষ্টিপাত",
            btnPredict: "🌾 উপযুক্ত ফসল নির্ণয় করুন"
        },
        resultCard: {
            title: "সুপারিশের ফলাফল",
            subtitle: "কৃষি বৈজ্ঞানিক মূল্যায়ন",
            badge: "বর্তমান পরিস্থিতির জন্য সর্বোত্তম প্রস্তাবিত",
            note: "আপনার মাটির N-P-K অনুপাত, পিএইচ এবং স্থানীয় বৃষ্টিপাতের সাথে এই ফসলটি বৈজ্ঞানিকভাবে সবচেয়ে মানানসই।",
            btnAskCopilot: "💬 এআই সহায়ককে চাষের পদ্ধতি জিজ্ঞাসা করুন",
            placeholder: "মাটি ও আবহাওয়ার মান পূরণ করে 'উপযুক্ত ফসল নির্ণয় করুন' বাটনে চাপুন।"
        },
        pillars: {
            title: "কৃষি মিত্রের সক্ষমতা",
            p1Title: "স্তম্ভ ১: পাতার রোগ নির্ণয় ভিশন",
            p1Desc: "রোগ নির্ণয় ও ছত্রাকনাশক ওষুধ সুপারিশসহ রিয়েল-টাইম অপটিক্যাল স্ক্যানার।",
            p3Title: "স্তম্ভ ৩: নির্ভরযোগ্য এআই কৃষি পরামর্শ",
            p3Desc: "ICAR প্যাকেজ অফ প্র্যাকটিস ভিত্তিক নির্ভরযোগ্য এআই সম্প্রসারণ এজেন্ট।",
            p2Title: "স্তম্ভ ২: আঞ্চলিক ফলন মডেল",
            p2Desc: "কৃষি-আবহাওয়া ভিত্তিক উন্নত পূর্বাভাস ইঞ্জিন।"
        },
        camera: {
            title: "মাঠ ও পাতার রোগ নির্ণায়ক অপটিক্যাল স্ক্যানার",
            subtitle: "ইউনিট: CAM-AGRI-01 • সেন্সর: CMOS অপটিক্যাল ও ক্লোরোফিল IR",
            tabWebcam: "লাইভ ক্যামেরা",
            tabSim: "নমুনা পাতা মোড",
            btnFilter: "🎨 ফিল্টার পরিবর্তন: উদ্ভিদ স্ট্রেস IR",
            btnUpload: "📁 পাতার ছবি আপলোড করুন",
            btnCapture: "📸 পাতা স্ক্যান করুন ও রোগ জানুন",
            btnDone: "সম্পন্ন",
            symptomsTitle: "দৃশ্যমান লক্ষণসমূহ:",
            treatmentTitle: "প্রয়োজনীয় ছত্রাকনাশক / কীটনাশক প্রতিকার:",
            btnListen: "🔊 বাংলায় শুনুন",
            btnStopVoice: "⏹ কণ্ঠস্বর বন্ধ করুন",
            scanning: "স্ক্যান ও রোগ নির্ণয় করা হচ্ছে...",
            ready: "স্ক্যান করার জন্য প্রস্তুত",
            analyzingUpload: "আপলোড করা ছবির বিশ্লেষণ চলছে..."
        },
        copilot: {
            title: "কৃষি মিত্র এআই সহায়ক (Copilot)",
            subtitle: "ICAR ও কৃষি বিশ্ববিদ্যালয়ের প্যাকেজ অফ প্র্যাকটিসের ওপর প্রতিষ্ঠিত",
            welcome: "নমস্কার! আমি আপনার এআই কৃষি সহায়ক। সঠিক কৃষি পদ্ধতি, সার প্রয়োগ এবং রোগবালাই দমনে কীভাবে সাহায্য করতে পারি?",
            placeholder: "ফসল, সার বা রোগবালাই সম্পর্কে প্রশ্ন করুন (বলতে 🎙️ চাপুন)...",
            btnSend: "পাঠান",
            actionTitle: "🌿 কৃষকের জন্য প্রয়োজনীয় পদক্ষেপ:",
            listening: "🎙️ শুনছি... অনুগ্রহ করে আপনার প্রশ্নটি বলুন...",
            presets: [
                "পিএইচ ৬.৫ এবং বেশি বৃষ্টিপাতযুক্ত মাটিতে কোন ফসল ভালো হয়?",
                "ধানের ব্লাস্ট বা ঝলসা রোগ নিয়ন্ত্রণের সঠিক উপায় কী?",
                "গম চাষে N-P-K সারের অনুমোদিত মাত্রা কত?",
                "টমেটোর পাতা পোড়া রোগের জৈব প্রতিকার কী?",
                "ড্রিপ সেচের মাধ্যমে সারের সাশ্রয় কীভাবে করা যায়?"
            ]
        },
        crops: {
            Rice: "ধান / চাল",
            Maize: "ভুট্টা",
            Chickpea: "ছোলা",
            Kidneybeans: "রাজমা",
            Pigeonpeas: "অড়হর ডাল",
            Mothbeans: "মট কলাই",
            Mungbean: "মুগ ডাল",
            Blackgram: "মাষকলাই",
            Lentil: "মসুর ডাল",
            Pomegranate: "বেদানা / ডালিম",
            Banana: "কলা",
            Mango: "আম",
            Grapes: "আঙুর",
            Watermelon: "তরমুজ",
            Muskmelon: "খরমুজ",
            Apple: "আপেল",
            Orange: "কমলালেবু",
            Papaya: "পেঁপে",
            Coconut: "নারকেল",
            Cotton: "তুলা",
            Jute: "পাট",
            Coffee: "কফি"
        }
    },

    te: {
        code: "te",
        speechCode: "te-IN",
        name: "Telugu",
        native: "తెలుగు",
        nav: {
            title: "కృషి మిత్ర",
            badge: "ఏఐ వ్యవసాయ విస్తరణ ఏజెంట్",
            subtitle: "స్మార్ట్ పంట విజ్ఞానం • కంప్యూటర్ విజన్ • వ్యవసాయ సలహా మండలి",
            btnCamera: "ఫీల్డ్ కెమెరా స్కానర్",
            btnLive: "లైవ్",
            btnCopilot: "ఏఐ వ్యవసాయ కోపైలట్"
        },
        weather: {
            title: "ప్రత్యక్ష వ్యవసాయ-వాతావరణ సమాచారం",
            tag: "ఓపెన్-మెటియో ఆధారితం",
            subtitle: "రియల్-టైమ్ ఉష్ణోగ్రత, తేమ, వర్షపాతం మరియు 5 రోజుల వ్యవసాయ సలహాలు",
            placeholder: "జిల్లా / నగరం (ఉదా. గుంటూరు, విజయవాడ, వరంగల్)",
            btnFetch: "వాతావరణం పొందండి",
            btnGPS: "📍 జీపీఎస్ గుర్తించండి",
            quickSelect: "త్వరిత ఎంపిక:",
            humidity: "సాపేక్ష తేమ",
            rainfall: "వర్షపాతం",
            wind: "గాలి వేగం",
            sprayingTitle: "🧪 పిచికారీ సలహా",
            irrigationTitle: "💧 నీటిపారుదల సలహా",
            forecastTitle: "5 రోజుల వ్యవసాయ వాతావరణ సూచన",
            btnAutoFill: "⚡ ఈ వాతావరణాన్ని ఫారమ్‌లో నింపండి",
            toastApplied: "✓ వివరాలు ఫారమ్‌లో చేర్చబడ్డాయి!"
        },
        cropForm: {
            title: "స్మార్ట్ పంట సిఫార్సు",
            subtitle: "రాండమ్ ఫారెస్ట్ మోడల్ మరియు వాతావరణ గణాంకాల ఆధారంగా",
            soilSection: "🧪 నేల పోషకాల వివరాలు (కిలోలు/హెక్టారు)",
            nitrogen: "నత్రజని (N)",
            phosphorus: "భాస్వరం (P)",
            potassium: "పొటాష్ (K)",
            ph: "నేల పి.హెచ్ (pH)",
            climateSection: "🌦️ వాతావరణ పరిస్థితులు",
            temperature: "ఉష్ణోగ్రత",
            humidity: "తేమ శాతం",
            rainfall: "వర్షపాతం",
            btnPredict: "🌾 అనువైన పంటను అంచనా వేయండి"
        },
        resultCard: {
            title: "ఫలితం",
            subtitle: "వ్యవసాయ శాస్త్ర ఫలితం",
            badge: "ప్రస్తుత పరిస్థితులకు ఉత్తమమైనది",
            note: "మీ నేల N-P-K పోషకాలు, pH మరియు వాతావరణానికి ఈ పంట అత్యంత అనుకూలమైనది.",
            btnAskCopilot: "💬 సాగు పద్ధతుల గురించి ఏఐని అడగండి",
            placeholder: "నేల మరియు వాతావరణ వివరాలను నమోదు చేసి పంటను అంచనా వేయండి."
        },
        pillars: {
            title: "కృషి మిత్ర సామర్థ్యాలు",
            p1Title: "స్తంభం 1: ఆకు తెగుళ్ళ స్కానర్",
            p1Desc: "ఆకు తెగుళ్ళను గుర్తించి మందులను సూచించే కెమెరా స్కానర్.",
            p3Title: "స్తంభం 3: ఆధారిత ఏఐ సలహాదారు",
            p3Desc: "ICAR ప్యాకేజ్ ఆఫ్ ప్రాక్టీసెస్ ఆధారంగా వ్యవసాయ విస్తరణ.",
            p2Title: "స్తంభం 2: ప్రాంతీయ దిగుబడి నమూనాలు",
            p2Desc: "ఖచ్చితమైన వ్యవసాయ-వాతావరణ అంచనా ఇంజిన్."
        },
        camera: {
            title: "ఫీల్డ్ & లీఫ్ ఆప్టికల్ డయాగ్నస్టిక్ స్కానర్",
            subtitle: "యూనిట్: CAM-AGRI-01 • సెన్సార్: CMOS ఆప్టికల్ & క్లోరోఫిల్ IR",
            tabWebcam: "లైవ్ కెమెరా",
            tabSim: "నమూనా ఆకు మోడ్",
            btnFilter: "🎨 ఫిల్టర్ మార్చండి: ప్లాంట్ స్ట్రెస్ IR",
            btnUpload: "📁 ఆకు ఫోటో అప్‌లోడ్ చేయండి",
            btnCapture: "📸 ఆకును స్కాన్ చేసి తెగులును గుర్తించండి",
            btnDone: "పూర్తయింది",
            symptomsTitle: "కనిపించే లక్షణాలు:",
            treatmentTitle: "నివారణ చర్యలు / పురుగుమందులు:",
            btnListen: "🔊 గొంతుతో వినండి",
            btnStopVoice: "⏹ ఆపండి",
            scanning: "స్కాన్ చేసి విశ్లేషిస్తోంది...",
            ready: "స్కాన్ చేయడానికి సిద్ధంగా ఉంది",
            analyzingUpload: "అప్‌లోడ్ చేసిన చిత్రాన్ని పరిశీలిస్తోంది..."
        },
        copilot: {
            title: "కృషి మిత్ర ఏఐ కోపైలట్ (Copilot)",
            subtitle: "ICAR మరియు వ్యవసాయ విశ్వవిద్యాలయాల సిఫార్సుల ఆధారంగా",
            welcome: "నమస్కారం! నేను మీ ఏఐ వ్యవసాయ సహాయకుడిని. పంటలు, ఎరువులు మరియు తెగుళ్ళ నివారణలో మీకు ఏ విధంగా సహాయపడగలను?",
            placeholder: "పంటలు, ఎరువులు లేదా తెగుళ్ళ గురించి అడగండి (మాట్లాడటానికి 🎙️ నొక్కండి)...",
            btnSend: "పంపు",
            actionTitle: "🌿 ఆచరణీయ వ్యవసాయ సలహా:",
            listening: "🎙️ వింటున్నాను... దయచేసి మీ ప్రశ్నను మాట్లాడండి...",
            presets: [
                "pH 6.5 మరియు భారీ వర్షపాతంలో ఏ పంట వేయాలి?",
                "వరి అగ్గితెగులును ఎలా అరికట్టాలి?",
                "గోధుమ పంటకు సిఫార్సు చేసిన N-P-K ఎరువుల మోతాదు ఎంత?",
                "టమోటా ఆకుమచ్చ తెగులుకు సేంద్రీయ నివారణ ఏమిటి?",
                "బిందు సేద్యం ద్వారా ఎరువుల సామర్థ్యం ఎలా పెరుగుతుంది?"
            ]
        },
        crops: {
            Rice: "వరి (వరి ధాన్యం)",
            Maize: "మొక్కజొన్న",
            Chickpea: "శనగలు",
            Kidneybeans: "రాజ్మా",
            Pigeonpeas: "కందులు",
            Mothbeans: "బొబ్బర్లు",
            Mungbean: "పెసలు",
            Blackgram: "మినుములు",
            Lentil: "ఎర్ర కందులు",
            Pomegranate: "దానిమ్మ",
            Banana: "అరటి",
            Mango: "మామిడి",
            Grapes: "ద్రాక్ష",
            Watermelon: "పుచ్చకాయ",
            Muskmelon: "కర్బూజా",
            Apple: "ఆపిల్",
            Orange: "నారింజ",
            Papaya: "బొప్పాయి",
            Coconut: "కొబ్బరి",
            Cotton: "పత్తి",
            Jute: "జనపనార",
            Coffee: "కాఫీ"
        }
    },

    mr: {
        code: "mr",
        speechCode: "mr-IN",
        name: "Marathi",
        native: "मराठी",
        nav: {
            title: "कृषी मित्र",
            badge: "एआय कृषी विस्तार सल्लागार",
            subtitle: "स्मार्ट पीक बुद्धिमत्ता • संगणक दृष्टी • पीक व्यवस्थापन सल्ला",
            btnCamera: "शेत कॅमेरा स्कॅनर",
            btnLive: "थेट",
            btnCopilot: "एआय कृषी मार्गदर्शक"
        },
        weather: {
            title: "थेट कृषी-हवामान बुद्धिमत्ता",
            tag: "ओपन-मेटिओ द्वारे समर्थित",
            subtitle: "स्थानिक तापमान, आर्द्रता, पर्जन्यमान आणि ५ दिवसांचा शेती सल्ला",
            placeholder: "जिल्हा / शहर (उदा. पुणे, नाशिक, नागपूर)",
            btnFetch: "हवामान मिळवा",
            btnGPS: "📍 जीपीएस शोधा",
            quickSelect: "जलद निवड:",
            humidity: "सापेक्ष आर्द्रता",
            rainfall: "पर्जन्यमान",
            wind: "वाऱ्याचा वेग",
            sprayingTitle: "🧪 फवारणी सल्ला",
            irrigationTitle: "💧 पाणी व्यवस्थापन सल्ला",
            forecastTitle: "५ दिवसांचा कृषी हवामान अंदाज",
            btnAutoFill: "⚡ हे हवामान फॉर्ममध्ये भरा",
            toastApplied: "✓ हवामान माहिती फॉर्ममध्ये भरली गेली!"
        },
        cropForm: {
            title: "स्मार्ट पीक शिफारस",
            subtitle: "रँडम फॉरेस्ट मॉडेल आणि कृषी-हवामान माहितीवर आधारित",
            soilSection: "🧪 मातीचे पोषण मूल्य (किलो/हेक्टर)",
            nitrogen: "नायट्रोजन (N)",
            phosphorus: "फॉस्फरस (P)",
            potassium: "पोटॅश (K)",
            ph: "सामू (pH)",
            climateSection: "🌦️ हवामान आणि वातावरणीय परिस्थिती",
            temperature: "तापमान",
            humidity: "आर्द्रता",
            rainfall: "पाऊस",
            btnPredict: "🌾 योग्य पिकाचा अंदाज घ्या"
        },
        resultCard: {
            title: "शिफारस निकाल",
            subtitle: "कृषी वैज्ञानिक निकाल",
            badge: "सध्याच्या परिस्थितीसाठी सर्वोत्तम शिफारस",
            note: "हे पीक तुमच्या जमिनीतील N-P-K, pH आणि हवामानासाठी गणितीयदृष्ट्या सर्वोत्तम आहे.",
            btnAskCopilot: "💬 लागवड तंत्राविषयी एआयला विचारा",
            placeholder: "जमीन आणि हवामानाचे तपशील भरून योग्य पिकाचा अंदाज घ्या."
        },
        pillars: {
            title: "कृषी मित्राची वैशिष्ट्ये",
            p1Title: "स्तंभ १: पान रोग ओळख स्कॅनर",
            p1Desc: "रोगांचे निदान आणि बुरशीनाशक उपायांसह रिअल-टाइम कॅमेरा स्कॅनर.",
            p3Title: "स्तंभ ३: खात्रीशीर एआय सल्लागार",
            p3Desc: "ICAR पॅकेज ऑफ प्रॅक्टिसवर आधारित कृषी विस्तार सेवा.",
            p2Title: "स्तंभ २: प्रादेशिक उत्पादन मॉडेल",
            p2Desc: "अचूक कृषी-हवामान अंदाज यंत्रणा."
        },
        camera: {
            title: "शेत व पान ऑप्टिकल निदान स्कॅनर",
            subtitle: "युनिट: CAM-AGRI-01 • सेन्सर: CMOS ऑप्टिकल आणि क्लोरोफिल IR",
            tabWebcam: "थेट कॅमेरा",
            tabSim: "नमुना पान मोड",
            btnFilter: "🎨 फिल्टर बदला: प्लांट स्ट्रेस IR",
            btnUpload: "📁 पानाचा फोटो अपलोड करा",
            btnCapture: "📸 पान स्कॅन करा आणि रोग ओळखा",
            btnDone: "झाले",
            symptomsTitle: "दिसणारी लक्षणे:",
            treatmentTitle: "रासायनिक / सेंद्रिय उपाययोजना:",
            btnListen: "🔊 आवाजात ऐका",
            btnStopVoice: "⏹ आवाज थांबवा",
            scanning: "स्कॅनिंग आणि रोग निदान सुरू आहे...",
            ready: "स्कॅनसाठी तयार",
            analyzingUpload: "अपलोड केलेल्या फोटोचे विश्लेषण सुरू..."
        },
        copilot: {
            title: "कृषी मित्र एआय मार्गदर्शक (Copilot)",
            subtitle: "ICAR आणि कृषी विद्यापीठांच्या शिफारसींवर आधारित",
            welcome: "नमस्कार शेतकरी बंधूंनो! मी तुमचा एआय कृषी विस्तार सहाय्यक आहे. पिके, खते, रोग आणि किडींच्या व्यवस्थापनात मी कशी मदत करू?",
            placeholder: "पिके, खते किंवा रोगांविषयी विचारा (बोलण्यासाठी 🎙️ दाबा)...",
            btnSend: "पाठवा",
            actionTitle: "🌿 कृषी कृती शिफारस:",
            listening: "🎙️ ऐकत आहे... कृपया आपला प्रश्न बोला...",
            presets: [
                "सामू ६.५ आणि जास्त पावसात कोणते पीक घ्यावे?",
                "भातावरील करपा रोगाचे प्रभावी नियंत्रण कसे करावे?",
                "गहू पिकासाठी शिफारशीत N-P-K खत मात्रा काय आहे?",
                "टोमॅटोवरील करपा रोगावर सेंद्रिय उपाय सांगा",
                "ठिबक सिंचनाने खतांची बचत कशी होते?"
            ]
        },
        crops: {
            Rice: "भात (तांदूळ)",
            Maize: "मका",
            Chickpea: "हरभरा (चना)",
            Kidneybeans: "राजमा",
            Pigeonpeas: "तूर",
            Mothbeans: "मठ",
            Mungbean: "मूग",
            Blackgram: "उडीद",
            Lentil: "मसूर",
            Pomegranate: "डाळिंब",
            Banana: "केळी",
            Mango: "आंबा",
            Grapes: "द्राक्षे",
            Watermelon: "कलिंगड",
            Muskmelon: "खरबूज",
            Apple: "सफरचंद",
            Orange: "संत्रे",
            Papaya: "पपई",
            Coconut: "नारळ",
            Cotton: "कापूस",
            Jute: "ताग",
            Coffee: "कॉफी"
        }
    },

    ta: {
        code: "ta",
        speechCode: "ta-IN",
        name: "Tamil",
        native: "தமிழ்",
        nav: {
            title: "கிருஷி மித்ரா",
            badge: "ஏஐ வேளாண் விரிவாக்க முகவர்",
            subtitle: "நுண்ணறிவு பயிர் தேர்வு • கணினி பார்வை • வேளாண் வழிகாட்டுதல்",
            btnCamera: "வயல் கேமரா ஸ்கேனர்",
            btnLive: "நேரலை",
            btnCopilot: "ஏஐ வேளாண் வழிகாட்டி"
        },
        weather: {
            title: "நேரலை வேளாண் காலநிலை நுண்ணறிவு",
            tag: "ஓபன்-மெட்டியோ இயங்குதளம்",
            subtitle: "உள்ளூர் வெப்பநிலை, ஈரப்பதம், மழைப்பொழிவு மற்றும் 5 நாள் விவசாய வழிகாட்டுதல்",
            placeholder: "மாவட்டம் / நகரம் (எ.கா. மதுரை, தஞ்சாவூர், கோவை)",
            btnFetch: "வானிலை பெறுக",
            btnGPS: "📍 ஜிபிஎஸ் கண்டறி",
            quickSelect: "விரைவு தேர்வு:",
            humidity: "சார்பு ஈரப்பதம்",
            rainfall: "மழைப்பொழிவு",
            wind: "காற்றின் வேகம்",
            sprayingTitle: "🧪 மருந்து தெளிப்பு ஆலோசனை",
            irrigationTitle: "💧 பாசன ஆலோசனை",
            forecastTitle: "5 நாள் வேளாண் வானிலை முன்னறிவிப்பு",
            btnAutoFill: "⚡ இக்காலநிலையை படிவத்தில் சேர்க்கவும்",
            toastApplied: "✓ வானிலை விவரங்கள் படிவத்தில் சேர்க்கப்பட்டன!"
        },
        cropForm: {
            title: "சிறந்த பயிர் பரிந்துரை",
            subtitle: "ரேண்டம் பாரஸ்ட் மாடல் மற்றும் காலநிலை உள்ளீடுகளின் அடிப்படையில்",
            soilSection: "🧪 மண் ஊட்டச்சத்து விபரம் (கிலோ/ஹெக்டேர்)",
            nitrogen: "தழைச்சத்து (N)",
            phosphorus: "மணிச்சத்து (P)",
            potassium: "சாம்பல் சத்து (K)",
            ph: "மண் கார அமிலத்தன்மை (pH)",
            climateSection: "🌦️ காலநிலை மற்றும் வானிலை சூழல்",
            temperature: "வெப்பநிலை",
            humidity: "ஈரப்பதம்",
            rainfall: "மழைப்பொழிவு",
            btnPredict: "🌾 உகந்த பயிரை கணிக்கவும்"
        },
        resultCard: {
            title: "பரிந்துரை முடிவு",
            subtitle: "வேளாண் அறிவியல் தேர்வு",
            badge: "தற்போதைய சூழலுக்கு பரிந்துரைக்கப்பட்டது",
            note: "உங்கள் மண்ணின் N-P-K ஊட்டச்சத்து, pH மற்றும் மழைப்பொழிவுக்கு இந்த பயிர் மிகவும் உகந்தது.",
            btnAskCopilot: "💬 சாகுபடி முறைகள் பற்றி ஏஐயிடம் கேட்கவும்",
            placeholder: "மண் மற்றும் வானிலை விவரங்களை உள்ளிட்டு 'உகந்த பயிரை கணிக்கவும்' பொத்தானை அழுத்தவும்."
        },
        pillars: {
            title: "கிருஷி மித்ரா திறன்கள்",
            p1Title: "தூண் 1: இலை நோய் கேமரா ஸ்கேனர்",
            p1Desc: "நோய் கண்டறிதல் மற்றும் பூஞ்சைக்கொல்லி மருந்து பரிந்துரையுடன் கூடிய ஸ்கேனர்.",
            p3Title: "தூண் 3: நம்பகமான ஏஐ வேளாண்மை ஆலோசகர்",
            p3Desc: "ICAR வழிகாட்டுதல்களின் அடிப்படையிலான வேளாண் விரிவாக்க முகவர்.",
            p2Title: "தூண் 2: பிராந்திய மகசூல் மாதிரிகள்",
            p2Desc: "துல்லியமான வேளாண்-காலநிலை முன்னறிவிப்பு இயந்திரம்."
        },
        camera: {
            title: "வயல் மற்றும் இலை நோய் கண்டறியும் ஸ்கேனர்",
            subtitle: "அலகு: CAM-AGRI-01 • சென்சார்: CMOS ஆப்டிகல் & குளோரோபில் IR",
            tabWebcam: "நேரலை கேமரா",
            tabSim: "மாதிரி இலை முறை",
            btnFilter: "🎨 வடிகட்டி மாற்று: தாவர அழுத்தம் IR",
            btnUpload: "📁 இலை படத்தை பதிவேற்றவும்",
            btnCapture: "📸 இலையை ஸ்கேன் செய்து நோய் கண்டறி",
            btnDone: "முடிந்தது",
            symptomsTitle: "தெரியும் அறிகுறிகள்:",
            treatmentTitle: "பரிந்துரைக்கப்படும் மருந்துகள் / மேலாண்மை:",
            btnListen: "🔊 குரலில் கேட்கவும்",
            btnStopVoice: "⏹ குரலை நிறுத்தவும்",
            scanning: "ஸ்கேன் செய்து நோய் கண்டறியப்படுகிறது...",
            ready: "ஸ்கேன் செய்ய தயார்",
            analyzingUpload: "பதிவேற்றிய படம் பகுப்பாய்வு செய்யப்படுகிறது..."
        },
        copilot: {
            title: "கிருஷி மித்ரா ஏஐ வழிகாட்டி (Copilot)",
            subtitle: "ICAR மற்றும் தமிழ்நாடு வேளாண் பல்கலை பரிந்துரைகளின் அடிப்படையில்",
            welcome: "வணக்கம்! நான் உங்கள் ஏஐ வேளாண் விரிவாக்க முகவர். பயிர்கள், உரங்கள் மற்றும் பூச்சி மேலாண்மையில் உங்களுக்கு எவ்வாறு உதவ முடியும்?",
            placeholder: "பயிர்கள், உரங்கள் பற்றி கேட்கவும் (பேச 🎙️ பொத்தானை அழுத்தவும்)...",
            btnSend: "அனுப்பு",
            actionTitle: "🌿 விவசாயிகள் செய்ய வேண்டிய முக்கிய படிகள்:",
            listening: "🎙️ கேட்கிறது... உங்கள் கேள்வியை பேசவும்...",
            presets: [
                "pH 6.5 மற்றும் அதிக மழை உள்ள நிலத்தில் என்ன பயிரிடலாம்?",
                "நெல் குலை நோயை எவ்வாறு கட்டுப்படுத்துவது?",
                "கோதுமைக்கு பரிந்துரைக்கப்பட்ட N-P-K உர அளவு என்ன?",
                "தக்காளி இலைப்புள்ளி நோய்க்கான இயற்கை தீர்வு என்ன?",
                "சொட்டுநீர்ப் பாசனம் மூலம் உர பயன்பாட்டு திறன் எவ்வாறு கூடுகிறது?"
            ]
        },
        crops: {
            Rice: "நெல் (அரிசி)",
            Maize: "மக்காச்சோளம்",
            Chickpea: "கொண்டைக்கடலை",
            Kidneybeans: "ராஜ்மா",
            Pigeonpeas: "துவரை",
            Mothbeans: "தட்டப்பயறு",
            Mungbean: "பாசிப்பயறு",
            Blackgram: "உளுந்து",
            Lentil: "மசூர் பருப்பு",
            Pomegranate: "மாதுளை",
            Banana: "வாழை",
            Mango: "மாம்பழம்",
            Grapes: "திராட்சை",
            Watermelon: "தர்பூசணி",
            Muskmelon: "முலாம் பழம்",
            Apple: "ஆப்பிள்",
            Orange: "ஆரஞ்சு",
            Papaya: "பப்பாளி",
            Coconut: "தேங்காய்",
            Cotton: "பருத்தி",
            Jute: "சணல்",
            Coffee: "காபி"
        }
    }
};

/**
 * Global Speech Engine for Vernacular Voice Recognition & Readout
 */
class KrishiVoiceEngine {
    constructor() {
        this.currentLang = 'en';
        this.recognition = null;
        this.isListening = false;
        this.synth = window.speechSynthesis || null;
        this.activeUtterance = null;
        this._initSpeechRecognition();
    }

    _initSpeechRecognition() {
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRec) {
            this.recognition = new SpeechRec();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;

            this.recognition.onstart = () => {
                this.isListening = true;
                this._updateMicUI(true);
            };

            this.recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                const input = document.getElementById('chatInput');
                if (input) {
                    input.value = transcript;
                    input.focus();
                }
            };

            this.recognition.onerror = (event) => {
                console.warn("Speech recognition error:", event.error);
                this.stopListening();
            };

            this.recognition.onend = () => {
                this.isListening = false;
                this._updateMicUI(false);
            };
        }
    }

    setLanguage(langCode) {
        this.currentLang = langCode || 'en';
        if (this.recognition) {
            const langData = KRISHI_TRANSLATIONS[this.currentLang] || KRISHI_TRANSLATIONS.en;
            this.recognition.lang = langData.speechCode;
        }
        this.stopSpeaking();
    }

    toggleListening() {
        if (!this.recognition) {
            alert("Speech Recognition is not supported on this browser. Please use Google Chrome or Microsoft Edge.");
            return;
        }
        if (this.isListening) {
            this.stopListening();
        } else {
            this.startListening();
        }
    }

    startListening() {
        if (!this.recognition) return;
        const langData = KRISHI_TRANSLATIONS[this.currentLang] || KRISHI_TRANSLATIONS.en;
        this.recognition.lang = langData.speechCode;
        try {
            this.recognition.start();
        } catch (e) {
            console.warn("Recognition already started", e);
        }
    }

    stopListening() {
        if (this.recognition && this.isListening) {
            this.recognition.stop();
        }
        this.isListening = false;
        this._updateMicUI(false);
    }

    _updateMicUI(listening) {
        const btn = document.getElementById('btnVoiceMic');
        const input = document.getElementById('chatInput');
        if (!btn) return;

        const langData = KRISHI_TRANSLATIONS[this.currentLang] || KRISHI_TRANSLATIONS.en;
        if (listening) {
            btn.classList.add('mic-active');
            btn.innerHTML = '🔴';
            btn.title = "Listening... बोलिए / বলুন...";
            if (input && !input.value) {
                input.placeholder = langData.copilot.listening;
            }
        } else {
            btn.classList.remove('mic-active');
            btn.innerHTML = '🎙️';
            btn.title = "Speak in " + langData.native;
            if (input) {
                input.placeholder = langData.copilot.placeholder;
            }
        }
    }

    speakText(text, onEndCallback) {
        if (!this.synth) {
            console.warn("Text-to-Speech not supported.");
            return;
        }
        this.stopSpeaking();

        if (!text || !text.trim()) return;

        // Clean markdown tags for natural speech
        const cleanText = text.replace(/[*#_`]/g, '').trim();
        const utterance = new SpeechSynthesisUtterance(cleanText);
        const langData = KRISHI_TRANSLATIONS[this.currentLang] || KRISHI_TRANSLATIONS.en;
        utterance.lang = langData.speechCode;
        utterance.rate = 0.95; // Slightly slower for clear regional speech

        // Pick best matching voice if available
        const voices = this.synth.getVoices();
        const matchedVoice = voices.find(v => v.lang.startsWith(this.currentLang) || v.lang === langData.speechCode);
        if (matchedVoice) {
            utterance.voice = matchedVoice;
        }

        utterance.onend = () => {
            this.activeUtterance = null;
            if (onEndCallback) onEndCallback();
        };

        utterance.onerror = () => {
            this.activeUtterance = null;
            if (onEndCallback) onEndCallback();
        };

        this.activeUtterance = utterance;
        this.synth.speak(utterance);
    }

    stopSpeaking() {
        if (this.synth) {
            this.synth.cancel();
            this.activeUtterance = null;
        }
    }

    isSpeaking() {
        return this.synth && this.synth.speaking;
    }
}

// Global instance
window.krishiVoice = new KrishiVoiceEngine();
