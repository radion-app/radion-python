from enum import Enum


class ApiKeyPlan(str, Enum):
    ENTERPRISE = "enterprise"
    FREE = "free"
    PRO = "pro"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
