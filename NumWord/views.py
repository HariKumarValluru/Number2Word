from django.shortcuts import render
from .forms import NumWordForm
from num2words import num2words

def convert(request):
    form = NumWordForm(request.POST or None)
    in_words = None
    if form.is_valid():
        in_words =num2words(form.cleaned_data.get('number'), lang='en_IN')
    else:
        form.errors
    context = {
        'form': form,
        'in_words': in_words
    }

    return render(request, 'NumWord/form.html', context)
