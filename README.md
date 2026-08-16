# Invoice Generator

اسکریپت Flask برای تولید فاکتور رسمی به‌صورت PDF از روی قالب HTML، با تاریخ شمسی.

## ویژگی‌ها

- دریافت اطلاعات مشتری (کد اقتصادی، شماره ثبت، کد ملی، آدرس و ...) از طریق ورودی خط فرمان
- رندر کردن قالب HTML فاکتور با Flask/Jinja2
- خروجی گرفتن فاکتور به‌صورت فایل PDF با `pdfkit` (بر پایه‌ی `wkhtmltopdf`)
- استفاده از تاریخ شمسی (`jdatetime`) برای مطابقت با فاکتورهای فارسی

## تکنولوژی‌ها

- Flask
- pdfkit + wkhtmltopdf
- jdatetime

## راه‌اندازی محلی

```bash
git clone https://github.com/AminRst/invoice-generator.git
cd invoice-generator/Invoice
python -m venv venv && source venv/bin/activate
pip install flask pdfkit jdatetime
# نصب wkhtmltopdf روی سیستم (نه به‌عنوان فایل داخل ریپو!)
python app.py
```

## نکاتی که بهتره قبل از نمایش اصلاح بشه

- [ ] فایل نصب‌کننده‌ی ویندوز `wkhtmltox-0.12.6-1.msvc2015-win64.exe` (باینری حجیم) از ریپو حذف بشه — این نوع فایل‌ها هرگز نباید داخل گیت کامیت بشن؛ کاربر باید خودش نصبش کنه یا لینکش توی README بیاد
- [ ] مسیر `wkhtmltopdf` هاردکد شده برای ویندوز (`C:\Program Files\...`) — بهتره از متغیر محیطی یا تشخیص خودکار مسیر استفاده بشه تا روی لینوکس/مک هم کار کنه
- [ ] اضافه کردن `requirements.txt`
- [ ] حذف `templates/output.pdf` (فایل خروجی نمونه) از ریپو — این خروجی اجراست، نباید کامیت بشه
