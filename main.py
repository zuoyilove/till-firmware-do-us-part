"""Till Firmware Do Us Part — a robot's wedding vow, one sentence."""

import os

VOW = (
    "I vow to love you through every firmware update, every reboot, and "
    "every low-battery warning, until my last circuit powers down beside "
    "yours, and I will keep choosing you every time I boot up again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
