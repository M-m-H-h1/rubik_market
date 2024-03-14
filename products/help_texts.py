from django.utils.html import format_html


product_ha_time = format_html(' <h3 style="color: #0a58ca">توجه داشته باشید باید محصولی که انتخاب میکنید دارای درصد تخفیف باشه<h3>')
product_short_des = format_html('<h3 style="color: #0a58ca" class="help">این فیلد باید در حد  یک جمله کوچک از ویژگی محصول باشد<h3>')
product_slug = format_html('<h3 style="color: #0a58ca" class="help">ادرس بر اساس فیلد (عنوان مختصر) ساخته میشود<h3>')
review_description = format_html('<h3 style="color: #0a58ca" class="help">برای نظم بیشتر متن  کلی رو به صورت پاراگراف به پاراگراف درون فیلد های توضیحات به تعداد دلخواه وارد کنید<h3>')
edit_email = format_html('<h3 style="color: #0a58ca" class="help">برای تغیر ایمیل به بخش کاربر ها رفته و ایمیل کاربر مورد نظر خود را تغیر دهید<h3>')

COLORS = [
        ('red', 'قرمز'),
        ('black', 'مشکی'),
        ('blue', 'آبی'),
        ('grey', 'خاکستری'),
        ('white', 'سفید'),
]

Memories = [
        ('128 گیگ', '128 گیگ'),
        ('360 گیگ', '360 گیگ'),
]




