def upload_image(self, filename):
    
    return f"{self.pk}_{filename}"

def upload_user_profile_image(self, filename):
    
    return f"{self.pk}/{filename}"