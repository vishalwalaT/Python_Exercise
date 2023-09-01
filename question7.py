import re

emails = [
    "abc@gmail.com",
    "123$tt*@xyz.com",
    "good@bad@uk.in",
    "nasa@usa12.space",
    "no-reply@domain.in",
    "ramhanuman@saketa.lok",
    "ruhi.mohan@exter123.123",
    "fake@fake123.fakercom",
]
exp = r"[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{2,5}"
valid_emails = []
for i in emails:
    match = re.fullmatch(exp, i)
    if match is not None:
        valid_emails.append(i)
print(valid_emails)
