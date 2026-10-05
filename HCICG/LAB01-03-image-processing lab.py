def run_lab(image_path: str, output_dir: str) -> dict:
    """Run Tasks 1-4 and return their results together."""
    os.makedirs(output_dir, exist_ok=True)
    t1 = inspect_image(image_path)
    t2 = create_pixel_views(image_path, output_dir)
    t3 = create_adjustments(image_path, output_dir)
    t4 = create_blur_and_edges(image_path, output_dir)
    return {"task1": t1, "task2": t2, "task3": t3, "task4": t4}

def main() -> None:
    """Run the lab using the required repository paths."""
    image_path = "images/original.jpg"
    output_dir = "outputs/"
    os.makedirs(output_dir, exist_ok=True)
    results = run_lab(image_path, output_dir)
    print("Lab completed:")
    print(results)

if _name_ == "_main_":
    main()