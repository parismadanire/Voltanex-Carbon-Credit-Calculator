import hashlib

def get_generator(name="Balbina"):
    ceg = f"CEG-{name}"
    device_id = hashlib.sha256(ceg.encode()).hexdigest()

    return {
        "ceg": ceg,
        "device_id": device_id,
        "capacity_kw": 14000000,
        "category": "utility"
    }
