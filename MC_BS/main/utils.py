def upload_image_to_news_item(self, filename):
    return f"newsItem/{filename}"

def upload_user_profile_image(self, filename):
    return f"{self.pk}/{filename}"

def upload_albom_element_image(self, filename):
    return f"albumImages/{filename}"

def str_to_int(limit : str):
    res = 0
    for pointer, chr in enumerate(limit[::-1], 0):
        if not chr.isdigit():
            return 9
        res += int(chr) * 10**pointer
    return res 