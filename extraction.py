import re

from patterns import (
    EMAIL_PATTERN,
    URL_PATTERN,
    PHONE_PATTERN,
    CREDIT_CARD_PATTERN,
    TIME_PATTERN,
    HTML_TAG_PATTERN,
    HASHTAG_PATTERN,
    CURRENCY_PATTERN
)


def extract_emails(text):
    return re.findall(EMAIL_PATTERN, text)


def extract_urls(text):
    return re.findall(URL_PATTERN, text)


def extract_phone_numbers(text):
    return re.findall(PHONE_PATTERN, text)


def extract_credit_cards(text):
    return re.findall(CREDIT_CARD_PATTERN, text)


def extract_times(text):
    return re.findall(TIME_PATTERN, text)


def extract_html_tags(text):
    return re.findall(HTML_TAG_PATTERN, text)


def extract_hashtags(text):
    return re.findall(HASHTAG_PATTERN, text)


def extract_currency(text):
    return re.findall(CURRENCY_PATTERN, text)
