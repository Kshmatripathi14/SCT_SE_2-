# SCT_SE_2 - Image Encryption Tool

This repository contains a Python tool for **basic image encryption and decryption** using various pixel manipulation techniques.  
It was created for **SkillCraft Task 02** following the SkillCraft repository naming rules.

---

## 📌 Features
- **Encryption & Decryption** of images using:
  1. **XOR** (bitwise exclusive OR with key)
  2. **Addition** (pixel value shift modulo 256)
  3. **Swap** (pixel position swapping based on key)
  4. **Shuffle Channels** (permutes RGB channels)

- Works with **PNG, JPG, JPEG, BMP** formats.
- **Deterministic** operations based on user-provided key.
- Uses `Pillow` for image processing and `numpy` for pixel manipulation.

---
