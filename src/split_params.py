def split_parameters(text: str):
    """
    把 OCR 文本拆成参数级 key-value
    """
    params = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        # 统一处理中英文冒号
        if "：" in line:
            key, value = line.split("：", 1)
        elif ":" in line:
            key, value = line.split(":", 1)
        else:
            continue

        params.append({
            "field": key.strip(),
            "value": value.strip()
        })

    return params
