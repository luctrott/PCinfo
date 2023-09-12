import psutil # pip install psutil

def get_ram_info():
    ram_info = []
    try:
        for bank in psutil.virtual_memory()._asdict():
            ram_info.append({
                "Firm": bank,
                "Speed (MHz)": "N/A",
                "Size (MB)": psutil.virtual_memory()._asdict()[bank] // (1024 ** 2),
            })

        return ram_info

    except Exception as e:
        print("Error: Unable to retrieve RAM information.")
        print(e)
        return []

if __name__ == "__main__":
    ram_info = get_ram_info()

    if ram_info:
        print("RAM Information per Bank:")
        for i, bank in enumerate(ram_info):
            print(f"Bank {i + 1}:")
            print(f"  Firm: {bank['Firm']}")
            print(f"  Speed (MHz): {bank['Speed (MHz)']}")
            print(f"  Size (MB): {bank['Size (MB)']} MB")
    else:
        print("No RAM information found.")
