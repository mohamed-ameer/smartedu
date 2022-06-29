from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from page.models import Page, PostFileContent,Comment, Reply
from classroom.models import Course
from module.models import Module
from completion.models import Completion

from page.forms import NewPageForm

# Create your views here.

@login_required
def NewPageModule(request, course_id, module_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	module = get_object_or_404(Module, id=module_id)
	files_objs = []

	if user != course.user:
		return HttpResponseForbidden()

	else:
		if request.method == 'POST':
			form = NewPageForm(request.POST, request.FILES)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				video_url = form.cleaned_data.get('video_url')
				description = form.cleaned_data.get('description')
				files = request.FILES.getlist('files')

				for file in files:
					file_instance = PostFileContent(file=file, user=user)
					file_instance.save()
					files_objs.append(file_instance)

				p = Page.objects.create(title=title,video_url=video_url,description=description, user=user)
				p.files.set(files_objs)
				p.save()
				module.pages.add(p)
				return redirect('modules', course_id=course_id)
		else:
			form = NewPageForm()
	context = {
		'form': form,'course': course
	}

	return render(request, 'page/newpage.html', context)


def PageDetail(request, course_id, module_id, page_id):
	page = get_object_or_404(Page, id=page_id)
	course = get_object_or_404(Course, id=course_id)
	module = get_object_or_404(Module, id=module_id)
	completed = Completion.objects.filter(course_id=course_id, user=request.user, page_id=page_id).exists()

	comments =Comment.objects.filter(page=page)
	replies =Reply.objects.filter(page=page)

	if request.method == 'POST':
		if request.POST.get('form-type') == 'comment-post':
			comment = request.POST.get('comment')#name='comment' in input of form
			comment_info = Comment.objects.create(user_given=request.user,page=page,content=comment)
			comment_info.save()
		else:
			reply = request.POST.get('reply')#name='reply' in input of form
			comment_id= request.POST.get('comment_id')
			current_comment=Comment.objects.get(id=comment_id)
			reply_info = Reply.objects.create(user_given=request.user,reply_content=reply,comment_on=current_comment)
			reply_info.save()



	context = {
		'page': page,
		'course': course,
		'module': module,
		'completed': completed,
		'course_id': course_id,
		'module_id': module_id,
		'comments': comments,
		'replies': replies,
	}
	return render(request, 'page/page.html', context)


def MarkPageAsDone(request, course_id, module_id, page_id):
	user = request.user
	page = get_object_or_404(Page, id=page_id)
	course = get_object_or_404(Course, id=course_id) 
	Completion.objects.create(user=user, course=course, page=page)
	return redirect('modules', course_id=course_id)

