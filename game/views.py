from django.shortcuts import render
import random

def home(request):
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        context = {'message': ''}
        if 1 <= guess <= 100:
            number_to_guess = request.session['number_to_guess']
            if guess < number_to_guess:
                context['message'] = 'Too low!'
            elif guess > number_to_guess:
                context['message'] = 'Too high!'
            else:
                context['message'] = f'Congratulations! You guessed the number {number_to_guess}!'
                del request.session['number_to_guess']
        else:
            context['message'] = 'Please enter a number between 1 and 100.'
        return render(request, 'game/home.html', context)
    else:
        if 'number_to_guess' not in request.session:
            request.session['number_to_guess'] = random.randint(1, 100)
        return render(request, 'game/home.html')
