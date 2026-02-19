#!/usr/bin/env python3
"""Interactive TP90x demo with model selection, scan target, and action menu."""

from __future__ import annotations

from typing import Optional, Type

from tp90x import AlarmMode, SearchMode, TP902, TP904, TP90xBase, TemperatureBroadcast


class BroadcastCollector:
    def __init__(self) -> None:
        self.active = False
        self.remaining = 0
        self.target = 0

    def callback(self, broadcast: TemperatureBroadcast) -> None:
        if not self.active:
            return
        index = self.target - self.remaining + 1
        print(f"[broadcast {index}/{self.target}] {broadcast}")
        self.remaining -= 1

    def reset(self, count: int) -> None:
        self.active = True
        self.target = count
        self.remaining = count

    def stop(self) -> int:
        got = self.target - self.remaining
        self.active = False
        self.target = 0
        self.remaining = 0
        return got


def prompt_choice(prompt: str, options: dict[str, str]) -> str:
    while True:
        print(prompt)
        for key, label in options.items():
            print(f"  {key}) {label}")
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice.\n")


def prompt_int(prompt: str, default: Optional[int] = None) -> int:
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"{prompt}{suffix}: ").strip()
        if raw == "" and default is not None:
            return default
        try:
            return int(raw)
        except ValueError:
            print("Please enter an integer.")


def connect_selected_model(
    model_cls: Type[TP90xBase],
    search_mode: str,
    identifier: str,
    collector: BroadcastCollector,
) -> TP90xBase:
    by = SearchMode.ADDRESS if search_mode == "a" else SearchMode.NAME
    return model_cls.connect(
        identifier,
        by=by,
        on_temperature=collector.callback,
    )


def do_set_alarm(tp: TP90xBase) -> None:
    channel = prompt_int("Channel", 1)
    mode_choice = prompt_choice(
        "Alarm mode:",
        {"0": "Off", "1": "Target", "2": "Range"},
    )
    mode_map = {"0": AlarmMode.Off, "1": AlarmMode.Target, "2": AlarmMode.Range}
    mode = mode_map[mode_choice]

    value1 = None
    value2 = None
    if mode == AlarmMode.Target:
        value1 = float(input("Target temperature (C): ").strip())
    elif mode == AlarmMode.Range:
        value2 = float(input("Low temperature (C): ").strip())
        value1 = float(input("High temperature (C): ").strip())

    tp.set_alarm(channel=channel, mode=mode, value1=value1, value2=value2)
    print("Alarm updated.")


def receive_five_broadcasts(tp: TP90xBase, collector: BroadcastCollector) -> None:
    collector.reset(5)
    print("Waiting for 5 broadcasts...")
    timeout_count = 0
    while collector.remaining > 0:
        result = tp.process(timeout_ms=2000)
        if result is None:
            timeout_count += 1
            if timeout_count >= 8:
                break
    got = collector.stop()
    print(f"Broadcast capture complete ({got}/5).")


def run_menu(tp: TP90xBase, collector: BroadcastCollector) -> None:
    while True:
        action = prompt_choice(
            "\nChoose an action:",
            {
                "1": "Backlight on",
                "2": "Get firmware version",
                "3": "Get status",
                "4": "Get alarm (channel)",
                "5": "Set units",
                "6": "Set sound alarm",
                "7": "Set alarm",
                "8": "Snooze alarm",
                "9": "Sync time",
                "10": "Receive 5 broadcasts",
                "q": "Quit",
            },
        )

        if action == "1":
            tp.backlight_on()
            print("Backlight command sent.")
        elif action == "2":
            fw = tp.get_firmware_version()
            if fw is None:
                print("Firmware: no response (timeout)")
            else:
                print(f"Firmware: {fw}")
        elif action == "3":
            status = tp.get_status()
            if status is None:
                print("Status: no response (timeout)")
            else:
                print(f"Status: {status}")
        elif action == "4":
            channel = prompt_int("Channel", 1)
            alarm = tp.get_alarm(channel)
            if alarm is None:
                print("Alarm: no response (timeout)")
            else:
                print(f"Alarm: {alarm}")
        elif action == "5":
            units = prompt_choice("Units:", {"c": "Celsius", "f": "Fahrenheit"})
            tp.set_units(celsius=(units == "c"))
            print("Units updated.")
        elif action == "6":
            enabled = prompt_choice("Sound alarm:", {"on": "Enabled", "off": "Disabled"})
            tp.set_sound_alarm(enabled=(enabled == "on"))
            print("Sound alarm updated.")
        elif action == "7":
            do_set_alarm(tp)
        elif action == "8":
            tp.snooze_alarm()
            print("Snooze command sent.")
        elif action == "9":
            tp.sync_time()
            print("Time sync sent.")
        elif action == "10":
            receive_five_broadcasts(tp, collector)
        elif action == "q":
            return


def main() -> int:
    model_choice = prompt_choice("Select model:", {"1": "TP902", "2": "TP904"})
    model_cls: Type[TP90xBase] = TP902 if model_choice == "1" else TP904

    search_mode = prompt_choice(
        "Search by:",
        {"a": "Address", "n": "Name"},
    )
    prompt = "Enter BLE address" if search_mode == "a" else "Enter advertised name"
    identifier = input(f"{prompt}: ").strip()
    if not identifier:
        print("No identifier provided.")
        return 1

    collector = BroadcastCollector()
    print("Scanning and connecting...")
    try:
        tp = connect_selected_model(model_cls, search_mode, identifier, collector)
    except Exception as exc:
        print(f"Failed to connect: {exc}")
        return 2

    print(f"Connected to {model_cls.model_name()}.")
    try:
        auth = tp.authenticate()
        if auth is None:
            print("Authentication failed (timeout).")
            return 3
        print(f"Authenticated: {auth}")
        run_menu(tp, collector)
    finally:
        tp.disconnect()
        print("Disconnected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
