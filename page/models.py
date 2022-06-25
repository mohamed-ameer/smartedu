from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import os


# Create your models here.


def user_directory_path(instance, filename):
	#THis file will be uploaded to MEDIA_ROOT /the user_(id)/the file
	return 'user_{0}/{1}'.format(instance.user.id, filename)

class PostFileContent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField(upload_to=user_directory_path)
	posted = models.DateTimeField(auto_now_add=True)

	def get_file_name(self):
		return os.path.basename(self.file.name)


# def save_lesson_files(instance, filename):
#     upload_to = 'Images/'
#     ext = filename.split('.')[-1]
#     # get filename
#     if instance.id:
#         filename = 'lesson_files/{}/{}.{}'.format(instance.id,instance.id, ext)
#         if os.path.exists(filename):
#             new_name = str(instance.id) + str('1')
#             filename =  'lesson_images/{}/{}.{}'.format(instance.id,new_name, ext)
#     return os.path.join(upload_to, filename)

class Page(models.Model):
	title = models.CharField(max_length=150)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_owner')
	created_at = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(null=True, blank=True)
	video_url=models.URLField(max_length=200)
	# video = models.FileField(upload_to=user_directory_path,verbose_name="Video", blank=True, null=True)
	files = models.ManyToManyField(PostFileContent)
	# lecture = models.FileField(upload_to=user_directory_path,verbose_name="Presentations", blank=True)
	# sheet = models.FileField(upload_to=user_directory_path,verbose_name="Notes", blank=True)
	# Note = models.FileField(upload_to=user_directory_path,verbose_name="Notes", blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)


class Comment(models.Model):
    lesson_name = models.ForeignKey(Page,null=True, on_delete=models.CASCADE,related_name='comments')
    comm_name = models.CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
    reply_body = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)
