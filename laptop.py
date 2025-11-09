class Laptop:
    def __init__(self, brand, model, country, year, driveType, memoryGB, cpuType, gpuModel, speedMHz, screenSize):
        self.brand = brand
        self.model = model
        self.country = country
        # store year as integer (YYYY)
        try:
            self.year = int(year) if year is not None else None
        except Exception:
            self.year = None
        self.driveType = driveType
        self.memoryGB = memoryGB
        self.cpuType = cpuType
        self.gpuModel = gpuModel
        self.speedMHz = speedMHz
        self.screenSize = screenSize

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "country": self.country,
            "year": self.year,
            "drive_type": self.driveType,
            "memory_GB": self.memoryGB,
            "cpu_type": self.cpuType,
            "gpu_model": self.gpuModel,
            "speed_mhz": self.speedMHz,
            "screen_size": self.screenSize,
        }

    @staticmethod
    def from_dict(data):
        if data is None:
            return None
        return Laptop(
            data.get("brand"),
            data.get("model"),
            data.get("country"),
            data.get("year"),
            data.get("drive_type"),
            data.get("memory_GB"),
            data.get("cpu_type"),
            data.get("gpu_model"),
            data.get("speed_mhz"),
            data.get("screen_size"),
        )