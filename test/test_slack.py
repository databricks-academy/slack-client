from slack_client.slack_thread import SlackThread
import datetime
import pytest


def test_rebuild_first_message():

    thread = SlackThread("training-engine-test", "Slack Test")
    thread.send_msg("This is a test")

    thread.warnings = 3
    thread.errors = 0
    thread.exceptions = 0
    message, color = thread.rebuild_first_message()
    assert message == "3 Warnings | This is a test"
    assert color == "warning"

    thread.warnings = 0
    thread.errors = 5
    thread.exceptions = 0
    message, color =  thread.rebuild_first_message()
    assert message == "5 Errors | This is a test"
    assert color == "danger"

    thread.warnings = 0
    thread.errors = 0
    thread.exceptions = 7
    message, color = thread.rebuild_first_message()
    assert message == "7 Exceptions | This is a test"
    assert color == "danger"

    thread.warnings = 3
    thread.errors = 2
    thread.exceptions = 0
    message, color = thread.rebuild_first_message()
    assert message == "2 Errors | 3 Warnings | This is a test"
    assert color == "danger"

    thread.warnings = 0
    thread.errors = 5
    thread.exceptions = 3
    message, color = thread.rebuild_first_message()
    assert message == "3 Exceptions | 5 Errors | This is a test"
    assert color == "danger"

    thread.warnings = 1
    thread.errors = 0
    thread.exceptions = 7
    message, color = thread.rebuild_first_message()
    assert message == "7 Exceptions | 1 Warnings | This is a test"
    assert color == "danger"

    thread.warnings = 1
    thread.errors = 2
    thread.exceptions = 7
    message, color = thread.rebuild_first_message()
    assert message == "7 Exceptions | 2 Errors | 1 Warnings | This is a test"
    assert color == "danger"


def test_split():
    text = "7 Exceptions | 2 Errors | 1 Warnings | Some random comment"
    parts = text.split("|")
    assert parts[-1].strip() == "Some random comment"


def test_send_msg():

    current_time = datetime.datetime.now()
    first_message = f"This is a test at {current_time}"

    thread = SlackThread("training-engine-test", "Slack Test")
    assert thread.thread_ts is None
    assert thread.last_response is None

    thread.send_msg(first_message)
    first_ts = thread.thread_ts
    assert first_ts is not None
    assert thread.last_response is not None
    assert thread.last_response["ok"] is True

    thread.send_msg("This is the second message")
    assert thread.thread_ts == first_ts
    assert thread.last_response is not None
    assert thread.last_response["ok"] is True

    thread.update_first_msg("#0000ff", f"This is the updated test at {current_time}")
    assert thread.thread_ts == first_ts
    assert thread.last_response is not None
    assert thread.last_response["ok"] is True

    thread.send_msg("This is the fourth message")
    assert thread.thread_ts == first_ts
    assert thread.last_response is not None
    assert thread.last_response["ok"] is True

    thread.send_warning("This is a warning")
    thread.send_error("This is an error")

    thread.send_exception("This is an exception")
    thread.send_exception("This is an exception")

    thread.send_error("This is an error")

    thread.send_warning("This is a warning")
    thread.send_warning("This is a warning")

