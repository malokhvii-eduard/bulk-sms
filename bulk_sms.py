#!/usr/bin/env python3

import sys
from enum import IntEnum
from typing import List, Optional

import click
import phonenumbers
from com.dtmilano.android.viewclient import ViewClient
from tqdm import tqdm

MESSAGES_PACKAGE = "com.google.android.apps.messaging"
CONFIRM_ID = "android:id/button1"
DELETE_CHAT_ID = f"{MESSAGES_PACKAGE}:id/action_delete"
LAST_CHAT_ID = f"{MESSAGES_PACKAGE}:id/swipeableContainer"
MESSAGE_ID = f"{MESSAGES_PACKAGE}:id/compose_message_text"
RECIPIENT_ID = f"{MESSAGES_PACKAGE}:id/recipient_text_view"
SEND_MESSAGE_ID = f"{MESSAGES_PACKAGE}:id/send_message_button_icon"
START_CHAT_ID = f"{MESSAGES_PACKAGE}:id/start_chat_fab"


class Key(IntEnum):
    Back = 4
    Enter = 66
    Paste = 279


def get_phone_numbers() -> List[str]:
    if sys.stdin.isatty():
        click.echo("Oops, input is a terminal, not a pipe!", err=True)
        sys.exit(1)

    phone_numbers = set()
    for line in map(lambda p: p.strip(), sys.stdin):
        try:
            phone_numbers.add(
                phonenumbers.format_number(
                    phonenumbers.parse(line, None),
                    phonenumbers.PhoneNumberFormat.E164,
                )
            )
        except phonenumbers.NumberParseException:
            pass

    if not phone_numbers:
        click.echo("Oops, no phone numbers in E.164 format!", err=True)
        sys.exit(2)

    return list(sorted(phone_numbers))


def open_messages(view: ViewClient):
    view.device.shell(f"monkey -p {MESSAGES_PACKAGE} 1")


def send_sms(view: ViewClient, phone_number: str, draft: bool = False):
    view.dump()
    view.findViewById(START_CHAT_ID).touch()

    view.dump()
    view.findViewById(RECIPIENT_ID).touch()
    view.device.type(phone_number)
    view.device.press(Key.Enter.value)

    view.dump()
    view.findViewById(MESSAGE_ID).touch()
    view.device.press(Key.Paste.value)

    if not draft:
        view.dump()
        view.findViewById(SEND_MESSAGE_ID).touch()

    view.dump()
    view.device.press(Key.Back.value, repeat=2)


def delete_last_sms(view: ViewClient):
    view.dump()
    coords = view.findViewById(LAST_CHAT_ID).getXY()
    view.device.drag(coords, coords, duration=1000, steps=1)

    view.dump()
    view.findViewById(DELETE_CHAT_ID).touch()

    view.dump()
    view.findViewById(CONFIRM_ID).touch()


@click.command()
@click.option("--serialno", "-s", help="The device or emulator serial number.")
@click.option("--draft", "-d", is_flag=True, help="Save SMS as Draft.")
@click.option("--delete", "-x", is_flag=True, help="Delete SMS after sending.")
def main(serialno: Optional[str], draft: bool, delete: bool):
    """
    A simple tool to send SMS messages over the carrier's network from an
    Android phone using the Android Debug Bridge. Firstly you will need to
    install Android Debug Bridge and Messages application from Google Play.
    Next, you will need to turn on Developer Options on your Android phone.
    After the Developer Options are enabled, turn on Stay Awake and USB
    Debugging. Finally, plug your phone into your computer using a USB cable,
    copy a message to the clipboard on your phone and check that you have
    enough credit to send SMS. Enjoy!
    """

    phone_numbers = get_phone_numbers()

    view = ViewClient(*ViewClient.connectToDeviceOrExit(serialno=serialno))
    open_messages(view)

    phone_numbers = tqdm(phone_numbers)
    for phone_number in phone_numbers:
        phone_numbers.set_description(phone_number)

        send_sms(view, phone_number, draft)

        if delete:
            delete_last_sms(view)


if __name__ == "__main__":
    main()
