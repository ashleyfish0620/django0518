from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 時間函數
from datetime import datetime

import random

def students(request):
	std1 = {"name": "aka", "sid": "110913219", "age": 18}
	std2 = {"name": "熊瑩", "sid": "110913124", "age": 17}
	std3 = {"name": "ZOE哥", "sid": "110913131", "age": 16}
	stds = [std1, std2, std3]
	return render(request, "std.html", locals())

def hello(request):
	# return HttpResponse("Hello World")
	return render(request, 'hello.html')

def hello1(request, username):
	now = datetime.now()
	#                                     傳遞的資料
	return render(request, 'hello1.html', locals())

# global全域變數
times = 0

def hello2(request, username):
	global times
	times = times + 1
	local_times = times
	# local區域變數
	now = datetime.now()
	dicenum1 = random.randint(1,6)
	dicenum2 = random.randint(1,6)
	dicenum3 = random.randint(1,6)
	dict1 = {"dice1": dicenum1, "dice2": dicenum2, "dice3": dicenum3}

	score = random.randint(0,100)
	#                                     傳遞的資料
	return render(request, 'hello2.html', locals())
	# 字典型式 
	# {"username": username, "now": datetime.now(), "dicenum1": random.randint(1,6), 
	#  "dicenum2": random.randint(1,6), "dicenum3": random.randint(1,6), 
	#  "dict1": {"dice1": dicenum1, "dice2": dicenum2, "dice3": dicenum3}}