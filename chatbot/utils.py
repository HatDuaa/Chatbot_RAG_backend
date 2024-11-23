from langchain.schema import BaseChatMessageHistory, ChatMessage
from .models import ChatSession, ChatMessage as DjangoChatMessage

def save_chat_history_to_db(session_id: str, chat_history: BaseChatMessageHistory):
    # Lấy hoặc tạo một phiên chat mới
    session, created = ChatSession.objects.get_or_create(session_id=session_id)

    # Lưu từng tin nhắn trong lịch sử chat vào cơ sở dữ liệu
    for message in chat_history.messages:
        sender = 'user' if message.sender == 'User' else 'bot'
        DjangoChatMessage.objects.create(
            session=session,
            sender=sender,
            content=message.content
        )

def get_chat_history_from_db(session_id: str) -> BaseChatMessageHistory:
    # Lấy phiên chat từ cơ sở dữ liệu
    try:
        session = ChatSession.objects.get(session_id=session_id)
    except ChatSession.DoesNotExist:
        return BaseChatMessageHistory()

    # Lấy tất cả các tin nhắn liên quan đến phiên chat
    messages = session.messages.all().order_by('timestamp')
    chat_history = BaseChatMessageHistory()

    # Chuyển đổi các tin nhắn Django thành các tin nhắn LangChain
    for message in messages:
        chat_message = ChatMessage(
            sender='User' if message.sender == 'user' else 'Bot',
            content=message.content
        )
        chat_history.add_message(chat_message)

    return chat_history