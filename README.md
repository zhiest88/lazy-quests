# 🦥 Ленивые квесты

Telegram Mini App: ежедневные дела в игровом режиме — XP, уровни, серия дней.

- `index.html` — мини-приложение (раздаётся через GitHub Pages)
- `bot.py` — бот на aiogram 3, открывает приложение
- `deploy/` — values для helm-чарта и пример конфига

## Локальный запуск бота

```bash
cp deploy/config.example.yaml config.yaml   # вписать токен
pip install -r requirements.txt
CONFIG_PATH=./config.yaml python bot.py
```


