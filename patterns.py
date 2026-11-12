EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

URL_PATTERN = r'https?://(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?'

PHONE_PATTERN = r'(?<!\w)(?:\+\d{1,3}[\s.-]?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3,4}[\s.-]?\d{3,4}(?!\w)'

CREDIT_CARD_PATTERN = r'\b(?:\d{4}[- ]?){3}\d{4}\b'

TIME_PATTERN = (
    r'\b(?:[01]\d|2[0-3]):[0-5]\d\b'
    r'|'
    r'\b(?:1[0-2]|[1-9]):[0-5]\d\s?(?:AM|PM|am|pm)\b'
)

HTML_TAG_PATTERN = r'<[^>]+>'

HASHTAG_PATTERN = r'#[A-Za-z0-9_]+'

CURRENCY_PATTERN = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
