import datetime


from yui.util import (bold, bool2str, code, italics, preformatted, quote,
                      strike, tz_none_to_kst, tz_none_to_utc)


def test_datetime_utils():
    """Test utils for datetime."""

    now = datetime.datetime.utcnow()

    utcnow = tz_none_to_utc(now)

    assert utcnow.tzinfo.tzname(dt=None) == 'UTC'

    kstnow = tz_none_to_kst(now)

    assert kstnow.tzinfo.tzname(dt=None) == 'Asia/Seoul'


def test_bool2str():
    """True -> 'true', False -> 'false'"""

    assert bool2str(True) == 'true'
    assert bool2str(False) == 'false'


def text_slack_syntax():
    """Test slack syntax helpers."""

    assert bold('item4') == '*item4*'
    assert code('item4') == '`item4`'
    assert italics('item4') == '_item4_'
    assert preformatted('item4') == '```item4```'
    assert strike('item4') == '~item4~'
    assert quote('item4') == '>item4'
