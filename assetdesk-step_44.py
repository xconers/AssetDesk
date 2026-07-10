# === Stage 44: Add backup creation for the data file ===
# Project: AssetDesk
def create_backup():
    src = "assetdesk_data.csv"
    dst = f"{src}.bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    with open(src, 'r') as infile:
        shutil.copyfile(infile, dst)
    print(f"Backup created at {dst}")

if __name__ == "__main__":
    create_backup()
