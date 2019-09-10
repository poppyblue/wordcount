from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def count(request):
	user_text = request.GET['text']
	total_count = len(request.GET['text'])

	word_dict = {}
	for word in user_text:
		# 一开始不在字典里面
		if word not in word_dict:
			# 键是word 值是1
			word_dict[word] = 1
		else:
			word_dict[word] += 1

	#reverse=True从大到小
	sorted_dict = \
		sorted(word_dict.items(), key = lambda w:w[1], reverse = True)

	return render(request, 'count.html', 
			{'count': total_count, 
			'text': user_text, 'word': word_dict, 
			'sorted': sorted_dict})

def about(request):
	return render(request, 'about.html')