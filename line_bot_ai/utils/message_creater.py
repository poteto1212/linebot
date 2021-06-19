#送られてきたメッセージに対応するメソッド

from ..models import Message

def create_single_text_message(message):
    if Message.objects.filter(medicine=message):
        detail=Message.objects.filter(medicine=message)[0]
        message=detail.detail
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message