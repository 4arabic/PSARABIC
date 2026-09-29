import os
import re

BRAND = '''<div style="margin-top:43px;text-align:center;font-family:Arial,sans-serif;font-size:22px;font-weight:bold;color:white;">
تطوير وبرمجة:
<span style="color:#00d9ff;">محمد السوري</span>
|
<a href="https://t.me/PS4SY" target="_blank" rel="noopener" style="color:#ff3030;text-decoration:none;">
قناة التليجرام @PS4SY
</a>
</div>'''

for root, dirs, files in os.walk("."):
    for file in files:
        if not file.lower().endswith(".html"):
            continue

        path = os.path.join(root, file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = f.read()

            original = data

            # استبدال أي سطر Special Thanks بالكامل
            data = re.sub(
                r'<h1[^>]*>\s*Special Thanks to:.*?</h1>',
                BRAND,
                data,
                flags=re.IGNORECASE | re.DOTALL
            )

            # استبدال أي سطر Designed by القديم
            data = re.sub(
                r'<h1[^>]*>\s*Designed by:.*?</h1>',
                BRAND,
                data,
                flags=re.IGNORECASE | re.DOTALL
            )

            if data != original:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(data)

                print("تم التعديل:", path)

        except Exception as e:
            print("خطأ:", path, e)

print("\nتم الانتهاء.")
