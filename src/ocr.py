from paddleocr import PaddleOCR
import os

ocr_engine = PaddleOCR(
    lang="ch",
    use_angle_cls=True
)

def ocr_image(image_path: str) -> str:
    result = ocr_engine.ocr(image_path)

    texts = []

    for page in result:
        # PaddleOCR 3.x：识别结果在 rec_texts 里
        if "rec_texts" in page:
            texts.extend(page["rec_texts"])

    return "\n".join(texts)


def batch_ocr(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(input_dir):
        if not fname.lower().endswith(".png"):
            continue

        path = os.path.join(input_dir, fname)
        text = ocr_image(path)

        with open(os.path.join(output_dir, fname + ".txt"), "w", encoding="utf-8") as f:
            f.write(text)
