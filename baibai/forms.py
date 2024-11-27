from django.forms import ModelForm
from .models import BaibaiPost

class BaibaiPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = BaibaiPost
        fields = ['category', 'title', 'comment', 'money', 'image1', 'image2']
