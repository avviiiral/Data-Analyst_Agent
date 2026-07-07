from datetime import datetime


class HealthService:
    def status(self):
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
        }