def create_blur_and_edges(image_path: str, output_dir: str) -> dict:
    """Blur and detect edges - for outputs/blur_and_edges.png"""
    os.makedirs(output_dir, exist_ok=True)

    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    blurred = cv2.blur(gray, (5, 5))

    # Sobel edges
    sobel_orig_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_orig_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_orig = cv2.magnitude(sobel_orig_x, sobel_orig_y)
    sobel_orig = np.uint8(np.clip(sobel_orig, 0, 255))

    sobel_blur_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobel_blur_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    sobel_blur = cv2.magnitude(sobel_blur_x, sobel_blur_y)
    sobel_blur = np.uint8(np.clip(sobel_blur, 0, 255))

    fig, axes = plt.subplots(1, 4, figsize=(12, 4))
    axes[0].imshow(gray, cmap='gray'); axes[0].set_title("Grayscale")
    axes[1].imshow(blurred, cmap='gray'); axes[1].set_title("Mean Blur 5x5")
    axes[2].imshow(sobel_orig, cmap='gray'); axes[2].set_title("Sobel Original")
    axes[3].imshow(sobel_blur, cmap='gray'); axes[3].set_title("Sobel Blurred")

    for ax in axes: ax.axis('off')
    plt.tight_layout()

    output_path = os.path.join(output_dir, "blur_and_edges.png")
    plt.savefig(output_path, dpi=200)
    plt.close()

    return {"output_path": output_path}

if _name_ == "_main_":
    IMG = "input/image.jpg" # change this
    OUT = "outputs"