from django import template

register = template.Library()

arabic_numbers = {
    '0': '٠',
    '1': '١',
    '2': '٢',
    '3': '٣',
    '4': '٤',
    '5': '٥',
    '6': '٦',
    '7': '٧',
    '8': '٨',
    '9': '٩',
}

@register.filter
def to_arabic(value):
    return ''.join(arabic_numbers.get(digit, digit) for digit in str(value))
