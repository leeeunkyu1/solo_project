from django.db import models

# 장고의 모델은 클래스로 정의.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    # pip install pillow 해줘야함
    # null = True 텍스트에는 적용하지 않기를 권장. 해도 에러는없음
    
    
    
    
    
    
    
    
    
    # 매직 메소드 데이터베이스 문자열을 깔끔하게 보여줌!
    def __str__(self):
        return self.title   