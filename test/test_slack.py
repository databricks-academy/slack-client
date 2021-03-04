from slack_client.slack_thread import SlackThread
import datetime


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

    thread.update_first_msg("danger", f"This is the updated test at {current_time}")
    assert thread.thread_ts == first_ts
    assert thread.last_response is not None
    assert thread.last_response["ok"] is True

    thread.send_msg("This is the fourth message")
    assert thread.thread_ts == first_ts
    assert thread.last_response is not None
    assert thread.last_response["ok"] is True
