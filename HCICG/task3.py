def create_adjustments(
    image_path: str,
    output_dir: str,
    brightness_delta: int = 40,
    contrast_factor: float = 1.5,
    threshold: int = 127,
) -> dict:
    """Create labeled brightness, contrast, and threshold results."""
    if not (0 <= threshold <= 255):
        raise ValueError("threshold must be in range 0-255")

    os.makedirs(output_dir, exist_ok=True)

    img = Image.open(image_path).convert("RGB")
    gray = np.array(img.convert("L"))

    # Brightness: add and clip
    bright = np.clip(gray.astype(int) + brightness_delta, 0, 255).astype(np.uint8)
    # Contrast: multiply and clip
    contrast = np.clip(gray.astype(float) * contrast_factor, 0, 255).astype(np.uint8)
    # Threshold
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    fig, axes = plt.subplots(1, 4, figsize=(12, 4))
    axes[0].imshow(gray, cmap='gray'); axes[0].set_title("Grayscale")
    axes[1].imshow(bright, cmap='gray'); axes[1].set_title(f"Brightness +{brightness_delta}")
    axes[2].imshow(contrast, cmap='gray'); axes[2].set_title(f"Contrast x{contrast_factor}")
    axes[3].imshow(thresh, cmap='gray'); axes[3].set_title(f"Threshold {threshold}")

    for ax in axes: ax.axis('off')
    plt.tight_layout()

    output_path = os.path.join(output_dir, "adjustments.png")
    plt.savefig(output_path, dpi=200)
    plt.close()

    return {"output_path": output_path}

