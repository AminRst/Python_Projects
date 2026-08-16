# Invoice Generator

اسکریپت Flask برای تولید فاکتور رسمی به‌صورت PDF از روی قالب HTML، با تاریخ شمسی.

## ویژگی‌ها

- دریافت اطلاعات مشتری (کد اقتصادی، شماره ثبت، کد ملی، آدرس و ...) از طریق ورودی خط فرمان
- رندر کردن قالب HTML فاکتور با Flask/Jinja2
- خروجی گرفتن فاکتور به‌صورت فایل PDF با `pdfkit` (بر پایه‌ی `wkhtmltopdf`)
- استفاده از تاریخ شمسی (`jdatetime`) برای مطابقت با فاکتورهای فارسی
- تشخیص خودکار مسیر `wkhtmltopdf` — روی لینوکس/مک/ویندوز کار می‌کنه، دیگه به مسیر هاردکد ویندوزی وابسته نیست

## تکنولوژی‌ها

- Flask
- pdfkit + wkhtmltopdf
- jdatetime

## راه‌اندازی محلی

```bash
git clone https://github.com/AminRst/Python_Projects.git
cd Python_Projects/Invoice
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# نصب wkhtmltopdf (نه به‌عنوان فایل داخل ریپو):
#   لینوکس (دبیان/اوبونتو): sudo apt install wkhtmltopdf
#   مک: brew install wkhtmltopdf
#   ویندوز: از wkhtmltopdf.org دانلود و نصب کن، یا مسیرش رو با متغیر
#            محیطی WKHTMLTOPDF_PATH به برنامه معرفی کن

python app.py
```

## کارهایی که برای حرفه‌ای‌سازی این ریپو انجام شد

- فایل نصب‌کننده‌ی ویندوز `wkhtmltox-...exe` (حدود ۲۷ مگابایت) و یک پوشه‌ی کامل `venv/` که قبلاً به‌اشتباه کامیت شده بودن، از ریپو و از تاریخچه‌ی گیت حذف شدن.
- مسیر `wkhtmltopdf` که هاردکد و مخصوص ویندوز بود (`C:\Program Files\...`) با تابع `find_wkhtmltopdf()` جایگزین شد که به ترتیب متغیر محیطی، `PATH` سیستم و در نهایت مسیر پیش‌فرض ویندوز رو چک می‌کنه — یعنی الان روی هر سیستم‌عاملی کار می‌کنه.
- فایل خروجی نمونه (`templates/output.pdf`) از ریپو حذف شد؛ این فایل نتیجه‌ی اجرای برنامه‌ست، نه بخشی از کد.
- `requirements.txt` اضافه شد.
