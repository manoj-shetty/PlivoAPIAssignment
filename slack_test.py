from slack_api import *

channel_name = {
        "name": "manojtest12"
    }
new_chanel_name = {
        "name": channel_name['name'] + "_updated"
    }
channel_id = None


def test_create_a_new_channel():
    global channel_id
    slack_obj = SlackApi()
    resp = slack_obj.post("https://slack.com/api/channels.create", **channel_name)
    resp_json = resp.json()
    logging.info("Stats code " + str(resp.status_code))
    logging.info("Stats code " + str(resp.json()))
    channel_id = resp_json['channel']['id']
    assert resp_json['ok'], "Failed to create slack channel"


def test_join_channel():
    slack_obj = SlackApi()
    resp = slack_obj.post("https://slack.com/api/channels.join", **channel_name)
    resp_json = resp.json()
    logging.info("Stats code " + str(resp.status_code))
    logging.info("Stats code " + str(resp.json()))
    assert resp_json['ok'], "Failed to create slack channel"


def test_rename_channel():
    global channel_id
    new_chanel_name["channel"] = channel_id
    slack_obj = SlackApi()
    resp = slack_obj.put("https://slack.com/api/channels.rename", **new_chanel_name)
    resp_json = resp.json()
    logging.info("Stats code " + str(resp.status_code))
    logging.info("Stats code " + str(resp.json()))
    assert resp_json['ok'], "Failed to create slack channel"


def test_validate_rename():
    global channel_id
    slack_obj = SlackApi()
    resp = slack_obj.get("https://slack.com/api/channels.list")
    resp_json = resp.json()
    logging.info("Stats code " + str(resp.status_code))
    logging.info("Stats code " + str(resp_json))
    assert resp_json['ok'], "Failed to create slack channel"
    for channel in resp_json['channels']:
        if channel['id'] == channel_id:
            assert channel['name'] == new_chanel_name['name']


def test_archive_channel():
    global channel_id
    channel = {
        "channel": channel_id,
    }
    slack_obj = SlackApi()
    resp = slack_obj.post("https://slack.com/api/channels.archive", **channel)
    resp_json = resp.json()
    logging.info("Stats code " + str(resp.status_code))
    logging.info("Stats code " + str(resp.json()))
    assert resp_json['ok'], "Failed to create slack channel"


def test_validate_archive():
    global channel_id
    slack_obj = SlackApi()
    resp = slack_obj.get("https://slack.com/api/channels.list")
    resp_json = resp.json()
    logging.info("Stats code " + str(resp.status_code))
    logging.info("Stats code " + str(resp_json))
    assert resp_json['ok'], "Failed to create slack channel"
    for channel in resp_json['channels']:
        if channel['id'] == channel_id:
            assert channel['name'] == new_chanel_name['name']
            assert channel['is_archived']


