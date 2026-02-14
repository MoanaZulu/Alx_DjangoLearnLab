from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or len(content.strip()) == 0:
            raise forms.ValidationError("Comment cannot be empty.")
        return content






from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tags_str = self.cleaned_data.get("tags", "")
        if tags_str:
            tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag)
        return instance
