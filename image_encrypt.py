
---

## 🖥 `image_encrypt.py`

```python
import argparse
import numpy as np
from PIL import Image
import sys

def xor_encrypt_decrypt(img_array, key):
    return np.bitwise_xor(img_array, key)

def add_encrypt(img_array, key):
    return (img_array + key) % 256

def add_decrypt(img_array, key):
    return (img_array - key) % 256

def swap_encrypt(img_array, key):
    np.random.seed(key)
    flat = img_array.reshape(-1, img_array.shape[-1])
    idx = np.arange(len(flat))
    np.random.shuffle(idx)
    return flat[idx].reshape(img_array.shape), idx

def swap_decrypt(img_array, key):
    np.random.seed(key)
    flat = img_array.reshape(-1, img_array.shape[-1])
    idx = np.arange(len(flat))
    np.random.shuffle(idx)
    result = np.zeros_like(flat)
    result[idx] = flat
    return result.reshape(img_array.shape)

def shuffle_channels(img_array, key):
    np.random.seed(key)
    perm = np.arange(3)
    np.random.shuffle(perm)
    return img_array[:, :, perm], perm

def unshuffle_channels(img_array, key):
    np.random.seed(key)
    perm = np.arange(3)
    np.random.shuffle(perm)
    inv_perm = np.argsort(perm)
    return img_array[:, :, inv_perm]

def main():
    parser = argparse.ArgumentParser(description="Image Pixel Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("--input", required=True, help="Input image file")
    parser.add_argument("--output", required=True, help="Output image file")
    parser.add_argument("--key", type=int, required=True, help="Numeric key")
    parser.add_argument("--method", choices=["xor", "add", "swap", "shuffle_channels"], required=True, help="Encryption method")

    args = parser.parse_args()

    try:
        img = Image.open(args.input).convert("RGB")
        img_array = np.array(img)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

    if args.mode == "encrypt":
        if args.method == "xor":
            result = xor_encrypt_decrypt(img_array, args.key)
        elif args.method == "add":
            result = add_encrypt(img_array, args.key)
        elif args.method == "swap":
            result, _ = swap_encrypt(img_array, args.key)
        elif args.method == "shuffle_channels":
            result, _ = shuffle_channels(img_array, args.key)
        else:
            print("Invalid method")
            sys.exit(1)

    elif args.mode == "decrypt":
        if args.method == "xor":
            result = xor_encrypt_decrypt(img_array, args.key)
        elif args.method == "add":
            result = add_decrypt(img_array, args.key)
        elif args.method == "swap":
            result = swap_decrypt(img_array, args.key)
        elif args.method == "shuffle_channels":
            result = unshuffle_channels(img_array, args.key)
        else:
            print("Invalid method")
            sys.exit(1)

    try:
        Image.fromarray(result.astype(np.uint8)).save(args.output)
        print(f"Saved {args.mode}ed image to {args.output}")
    except Exception as e:
        print(f"Error saving image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
