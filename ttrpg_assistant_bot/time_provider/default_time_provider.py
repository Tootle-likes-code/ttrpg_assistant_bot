from datetime import datetime

from ttrpg_assistant_bot.time_provider.time_provider import TimeProvider


class DefaultTimeProvider(TimeProvider):
    instance: "DefaultTimeProvider" = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = DefaultTimeProvider()

        return cls.instance

    def get_time(self) -> datetime:
        return datetime.now()
