# Security Measures Implemented

## Settings
- DEBUG = False
- SECURE_BROWSER_XSS_FILTER = True
- X_FRAME_OPTIONS = "DENY"
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True

## Templates
- All forms include `{% csrf_token %}` to prevent CSRF attacks.

## Views
- ORM queries used instead of raw SQL to prevent SQL injection.
- User input validated via Django forms.

## CSP
- django-csp middleware configured to restrict scripts and styles to trusted sources.

## Testing
- Manual tests performed for CSRF and XSS vulnerabilities.
