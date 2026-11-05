"""Check the dated publication's local identity and catalogue structure, not PDE accuracy."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
catalogue = json.loads((ROOT / "catalogue.json").read_text())
chats = json.loads((ROOT / "chat-review.json").read_text())
records = catalogue["records"]
assert len(records) == len({r["id"] for r in records}) == 42
assert len(chats["records"]) == len({r["id"] for r in chats["records"]}) == 12
assert all(r["coverage"]["all_pages_read"] for r in chats["records"])
assert not any(r["coverage"]["selected_message_truncation_detected"] for r in chats["records"])
manifest = json.loads((ROOT / "documents/manifest.json").read_text())
for record in manifest["files"]:
    path = ROOT / "documents" / record["target"]
    assert path.is_file(), path
    data = path.read_bytes()
    assert len(data) == record["bytes"], path
    assert hashlib.sha256(data).hexdigest() == record["sha256"], path
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    assert path.stat().st_size <= 5_000_000, path
    assert path.suffix.lower() not in {".npz", ".npy", ".pt", ".pth", ".h5", ".hdf5"}, path
    if path.suffix == ".json":
        json.loads(path.read_text())
print(f"Verified {len(records)} dated records, {len(chats['records'])} chat reviews and {len(manifest['files'])} preserved documents.")
print("This does not rerun historical experiments or certify their scientific conclusions.")
