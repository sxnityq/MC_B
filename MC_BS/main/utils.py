def upload_image_to_news_item(self, filename):
    return f"newsItem/{filename}"

def upload_user_profile_image(self, filename):
    return f"{self.pk}/{filename}"

def upload_albom_element_image(self, filename):
    return f"albumImages/{filename}"