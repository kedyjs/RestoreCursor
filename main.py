import json
import os
import shutil
import uuid
from datetime import datetime
from pathlib import Path
import platform


def backup_file(file_path: str):
    """Her ihtimale karşılık olarak yedek dosyası oluşturuyoruz."""
    if os.path.exists(file_path):
        backup_path = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(file_path, backup_path)


def get_storage_file():
    """İşletim sistemine göre storage.json dosyasının yolunu buluyoruz."""
    system = platform.system()
    if system == "Windows":
        return Path(os.getenv("APPDATA")) / "Cursor" / "User" / "globalStorage" / "storage.json"
    elif system == "Darwin":  # macOS
        return Path(os.path.expanduser("~")) / "Library" / "Application Support" / "Cursor" / "User" / "globalStorage" / "storage.json"
    elif system == "Linux":
        return Path(os.path.expanduser("~")) / ".config" / "Cursor" / "User" / "globalStorage" / "storage.json"
    else:
        raise OSError(f"Unsupported operating system: {system}")


def reset_cursor_id():
    storage_file = get_storage_file()
    storage_file.parent.mkdir(parents=True, exist_ok=True)
    backup_file(storage_file)

    if not storage_file.exists():
        data = {}
    else:
        with open(storage_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

    machine_id = os.urandom(32).hex()
    mac_machine_id = os.urandom(32).hex()
    dev_device_id = str(uuid.uuid4())

    data["telemetry.machineId"] = machine_id
    data["telemetry.macMachineId"] = mac_machine_id
    data["telemetry.devDeviceId"] = dev_device_id

    with open(storage_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print("Cursor ID'leri başarıyla sıfırlandı. Yeni ID'ler: \n")
    print(
        json.dumps(
            {
                "machineId": machine_id,
                "macMachineId": mac_machine_id,
                "devDeviceId": dev_device_id,
            },
            indent=2))


if __name__ == "__main__":
    reset_cursor_id()