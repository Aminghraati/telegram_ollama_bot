# Telegram Ollama Bot 🤖

ربات تلگرام متصل به هوش مصنوعی محلی Ollama با مدل Gemma3:1b

این پروژه به شما اجازه می‌دهد از طریق تلگرام روی موبایل، به مدل هوش مصنوعی که روی کامپیوتر شخصی شما اجرا می‌شود متصل شوید.

## معماری پروژه

```
Mobile
   ↓
Telegram
   ↓
Telegram Bot
   ↓
Python
   ↓
Ollama
   ↓
Gemma3:1b
   ↓
Response
```


## امکانات

- اجرای هوش مصنوعی به صورت کاملاً محلی
- عدم نیاز به API خارجی هوش مصنوعی
- اتصال از طریق تلگرام
- ذخیره تاریخچه گفتگو در SQLite
- استفاده از مدل Gemma3:1b


## پیش‌نیازها

- Windows
- Python 3.13+
- Ollama
- Telegram Account


# نصب Ollama

ابتدا Ollama را نصب کنید.

بعد از نصب بررسی کنید:

```bash
ollama --version
```


# نصب مدل Gemma3:1b

دستور:

```bash
ollama pull gemma3:1b
```

تست مدل:

```bash
ollama run gemma3:1b
```


# ساخت ربات تلگرام

در تلگرام وارد BotFather شوید:

```
@BotFather
```

دستور ساخت ربات:

```bash
/newbot
```

نام ربات را انتخاب کنید.

بعد از ساخت ربات، BotFather یک Token به شما می‌دهد.


# گرفتن Telegram User ID

برای دریافت User ID از ربات‌های نمایش ID استفاده کنید.

این مقدار برای محدود کردن استفاده از ربات استفاده می‌شود.


# نصب پروژه

کلون کردن پروژه:

```bash
git clone https://github.com/Aminghraati/telegram_ollama_bot.git
```

ورود به پوشه پروژه:

```bash
cd telegram_ollama_bot
```


نصب کتابخانه‌ها:

```bash
pip install -r requirements.txt
```


# تنظیمات

فایل:

```
config.py
```

را باز کنید.

مقادیر زیر را وارد کنید:

```python
BOT_TOKEN="YOUR_TOKEN"

ALLOWED_USER_ID=YOUR_ID

OLLAMA_URL="http://127.0.0.1:11434/api/generate"

MODEL="gemma3:1b"
```


# اجرای پروژه

ابتدا Ollama باید فعال باشد.

بررسی Ollama:

```bash
curl http://127.0.0.1:11434
```

باید نمایش دهد:

```
Ollama is running
```


اجرای ربات:

```bash
python bot.py
```


حالا داخل تلگرام به ربات پیام بدهید.


# ساختار فایل‌ها

```
telegram_ollama_bot

├── bot.py
├── config.py
├── database.py
├── ollama_client.py
├── requirements.txt
├── README.md
```


# خطاهای رایج

## خطای اتصال Ollama

بررسی کنید Ollama در حال اجرا باشد:

```bash
curl http://127.0.0.1:11434
```

اگر خروجی زیر را دیدید:

```
Ollama is running
```

سرویس Ollama فعال است.


# License

Personal Project