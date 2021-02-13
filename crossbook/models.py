from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png', upload_to='profile_pics')
    text = models.TextField(blank=True, max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS = (
        (0, "選択してください"),
        (1, "新品、未使用"),
        (2, "未使用に近い"),
        (3, "目立った傷や汚れなし"),
        (4, "やや傷や汚れあり"),
        (5, "傷や汚れあり"),
        (6, "全体的に状態が悪い")
    )

    LOCATION = (
        (0, "選択してください"),
        (1, "北海道"),
        (2, "青森県"),
        (3, "岩手県"),
        (4, "宮城県"),
        (5, "秋田県"),
        (6, "山形県"),
        (7, "福島県"),
        (8, "茨城県"),
        (9, "栃木県"),
        (10, "群馬県"),
        (11, "埼玉県"),
        (12, "千葉県"),
        (13, "東京都"),
        (14, "神奈川県"),
        (15, "新潟県"),
        (16, "富山県"),
        (17, "石川県"),
        (18, "福井県"),
        (19, "山梨県"),
        (20, "長野県"),
        (21, "岐阜県"),
        (22, "静岡県"),
        (23, "愛知県"),
        (24, "三重県"),
        (25, "滋賀県"),
        (26, "京都府"),
        (27, "大阪府"),
        (28, "兵庫県"),
        (29, "奈良県"),
        (30, "和歌山県"),
        (31, "鳥取県"),
        (32, "島根県"),
        (33, "岡山県"),
        (34, "広島県"),
        (35, "山口県"),
        (36, "徳島県"),
        (37, "香川県"),
        (38, "愛媛県"),
        (39, "高知県"),
        (40, "福岡県"),
        (41, "佐賀県"),
        (42, "長崎県"),
        (43, "熊本県"),
        (44, "大分県"),
        (45, "宮崎県"),
        (46, "鹿児島県"),
        (47, "沖縄県"),
        (48, "未定")
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', verbose_name="画像")
    title = models.CharField(max_length=50, verbose_name="タイトル")
    content = models.TextField(max_length=100, verbose_name="一言")
    category = models.ManyToManyField(Category)
    state = models.PositiveSmallIntegerField(choices=STATUS, default=0, verbose_name="商品の状態")
    shipping_area = models.PositiveSmallIntegerField(choices=LOCATION, default=0)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="出品日")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return self.title




