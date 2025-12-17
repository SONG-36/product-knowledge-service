from docx import Document
from PIL import Image
import os
from io import BytesIO

def extract_images(docx_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    doc = Document(docx_path)

    image_index = 1

    # 遍历文档中的所有关系（按文档顺序）
    for rel in doc.part._rels.values():
        if "image" in rel.reltype:
            image_data = rel.target_part.blob

            image = Image.open(BytesIO(image_data))

            filename = f"image{image_index:03d}.png"
            image.save(os.path.join(output_dir, filename))

            image_index += 1

    print(f"Extracted {image_index - 1} images")


if __name__ == "__main__":
    extract_images(
        docx_path="input/manual.docx",     # 👈 你的 Word 文件
        output_dir="input/images"           # 👈 输出目录
    )
