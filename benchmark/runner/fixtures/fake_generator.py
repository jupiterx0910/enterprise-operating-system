class FakeGenerator:
    def __init__(self, fail_after: int | None = None):
        self.fail_after = fail_after
        self.calls = []

    def generate(self, messages, config):
        if self.fail_after is not None and len(self.calls) >= self.fail_after:
            raise RuntimeError("planned fake failure")
        self.calls.append({"messages": messages, "config": config})
        return f"FAKE OUTPUT {len(self.calls)}"
