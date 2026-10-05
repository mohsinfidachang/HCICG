def create_pixel_views(image_path: str, output_dir: str) -> dict:
    """Create the labeled channel, grayscale, and downsampled views."""
    os.makedirs(output_dir, exist_ok=True)

    img = Image.open(image_path).convert("RGB")
    original_size = [img.width, img.height]
    img_np = np.array(img)

    r = img_np[:, :, 0]
    g = img_np[:, :, 1]
    b = img_np[:, :, 2]
    gray = np.dot(img_np[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

    downsampled = img.resize((img.width // 4, img.height // 4), Image.LANCZOS)
    downsampled_size = [downsampled.width, downsampled.height]

    # Create montage 2x3
    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    axes = axes.flatten()

    axes[0].imshow(img_np); axes[0].set_title(f"Original {original_size}")
    axes[1].imshow(r, cmap='Reds'); axes[1].set_title("R Channel")
    axes[2].imshow(g, cmap='Greens'); axes[2].set_title("G Channel")
    axes[3].imshow(b, cmap='Blues'); axes[3].set_title("B Channel")
    axes[4].imshow(gray, cmap='gray'); axes[4].set_title("Grayscale")
    axes[5].imshow(downsampled); axes[5].set_title(f"Downsampled {downsampled_size}")

    for ax in axes: ax.axis('off')
    plt.tight_layout()

    output_path = os.path.join(output_dir, "pixel_views.png")
    plt.savefig(output_path, dpi=200)
    plt.close()

    return {
        "original_size": original_size,
        "downsampled_size": downsampled_size,
        "output_path": output_path
    }