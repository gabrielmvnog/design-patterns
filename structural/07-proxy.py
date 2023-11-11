from typing import Self


class Bridge:
    def cross(self: Self, name: str):
        print(f"You shall pass the bridge: {name}")


class GandalfProtectedBridge(Bridge):
    def __init__(self, bridge: Bridge) -> None:
        self.bridge = bridge

    def cross(self: Self, name: str):
        if name == "Balrog":
            print("You shall not pass")
        else:
            self.bridge.cross(name)


if __name__ == "__main__":
    bridge = Bridge()
    protected_bridge = GandalfProtectedBridge(bridge)

    protected_bridge.cross("Frodo")
    protected_bridge.cross("Balrog")
