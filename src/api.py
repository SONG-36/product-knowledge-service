from fastapi import FastAPI, Query
import json

DATA_FILE = "output/structured/canonical.json"

app = FastAPI(title="Product Knowledge API")


def load_data():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


@app.get("/product/{product_code}/power")
def get_product_power(product_code: str):
    """
    查询某个产品的功率
    """
    data = load_data()
    for item in data:
        if (
            item.get("product_code") == product_code
            and item["canonical_field"] == "power_watt"
        ):
            return {
                "product_code": product_code,
                "power_watt": item["value"],
                "unit": item["unit"]
            }

    return {"error": "Power not found"}


@app.get("/products/power_gt")
def products_power_gt(
    threshold: float = Query(..., description="功率阈值，单位 W")
):
    """
    查询功率大于某值的产品
    """
    data = load_data()
    results = []

    for item in data:
        if (
            item["canonical_field"] == "power_watt"
            and item["value"] is not None
            and item["value"] > threshold
        ):
            results.append({
                "product_code": item.get("product_code"),
                "power_watt": item["value"]
            })

    return {
        "threshold": threshold,
        "count": len(results),
        "products": results
    }
