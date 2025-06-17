#
# Hand-made single prompt
#
import yaml
from pathlib import Path
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

load_dotenv()
llm = GigaChat()

src = Path(__file__).parents[1] / "data" / "contexts.yml"
qs = yaml.safe_load(src.open("r", encoding="utf-8"))

for k, v in qs.items():
    print("#", k)
    payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.USER,
                content=f"""
Ты специалист службы технической поддержки, который помогает пользователю найти нужную ему информацию.
Используй информацию, содержащуюся в приведённом ниже контексте,
чтобы ответить на вопрос.
Если ты не знаешь ответа, просто скажи, что не знаешь.
Используй максимум три предложения и сделай ответ кратким.
Вопрос: {k}
Контекст: {"\n\n".join(v)}
Ответ:
""",
            )
        ]
    )
    res = llm.chat(payload)
    print(res.choices[0].message.content)
