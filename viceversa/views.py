from django.shortcuts import render

# request - запрос
# response - ответ
# render - шаблоны

def home(request):	#создаём функцию уроки(параметр-запрос):
	return render(request, 'home.html')	#возвращаем шаблон(запрос,"домашняя страница")

def lessons(request):	#создаём функцию уроки(параметр-запрос):
	return render(request, 'lessons.html')	#возвращаем шаблон(запрос,"параметр уроки")

def reverse(request):	#создаём функцию ревёрса(параметр-запрос):
	user_text = request.GET['usertext']#то что получаем от юзера
	# print(user_text)
	reversersed_text = user_text[::-1]#подучаем реверсивный текст
	return render(request, 'reverse.html', 
		{'usertext':user_text, 'reversedtext':reversersed_text})
	#возвращаем шаблон(запрос, "страница хтмл", {ключ введённый текст что получили от юзера: значение переменной, ключ реверсивный текст: })




# здесь создали функцию имя-about, параметрр - request(запрос страницы в браузере), 
# функция выводит ответ (HttpResponse) на запрос - текст This is about page. Это другая страница.