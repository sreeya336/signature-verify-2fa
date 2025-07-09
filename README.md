# SignatureVerify-2FA
![Python](https://img.shields.io/badge/Python-3.9-blue)
![TensorFlow](https://img.shields.io/badge/Model-TensorFlow-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Twilio](https://img.shields.io/badge/2FA-Twilio-red)
![MobileNetV2](https://img.shields.io/badge/FeatureExtractor-MobileNetV2-brightgreen)

**SignatureVerify-2FA** is a secure signature authentication system that detects handwritten forgery using deep learning and verifies user identity with two-factor authentication (2FA). This project is designed for applications like banking, legal services, and secure identity systems, where handwritten signature verification is essential.

Built using TensorFlow, Streamlit, and Twilio API, the system compares a user’s uploaded signature against pre-registered samples using MobileNetV2-based feature extraction and L1 distance similarity scoring. If the similarity passes a threshold, the user must then verify their identity via a one-time password (OTP) sent to their phone.

---
<p align="center">
  <img src="signature_detection_banner.png" width="600" alt="Signature Verification Banner">
</p>

## Why This Project?

Traditional signature verification is subjective and error-prone. This project:
- Automates verification using machine learning
- Improves accuracy and reliability
- Adds 2FA to prevent unauthorized access
- Provides a user-friendly interface via Streamlit

---

## How It Works

1. **Signature Upload**: The user uploads a query signature and 5 pre-registered genuine samples.
2. **Feature Extraction**: MobileNetV2 (pretrained on ImageNet) extracts 128-dimensional feature vectors.
3. **Similarity Scoring**: L1 distance is calculated between the uploaded signature and the registered samples.
4. **Thresholding**: If the average similarity score exceeds 0.75, it's considered genuine.
5. **OTP Verification**: An OTP is sent to the user’s phone using Twilio’s Verify API. The user must enter the OTP to complete verification.

---

## Features

- Deep feature extraction using MobileNetV2
- L1-based signature similarity computation
- Threshold-based decision logic
- OTP verification using Twilio API
- Real-time web interface using Streamlit
- Modular and extensible code structure

---

## Tech Stack

| Component        | Tool/Library             |
|------------------|--------------------------|
| Deep Learning    | TensorFlow, Keras        |
| Feature Model    | MobileNetV2              |
| Image Processing | OpenCV, NumPy            |
| Web Interface    | Streamlit                |
| OTP Integration  | Twilio Verify API        |
| Language         | Python                   |

---
### Clone the Repository

```bash
git clone https://github.com/sreeya336/signature-verify-2fa.git
cd signature-verify-2fa

