from django.shortcuts import render
from .forms import BinaryTranslationForm
from .utils import binary_to_text

def translate_binary(request):
    translation_form = BinaryTranslationForm(request.POST or None)
    translated_text = None

    if translation_form.is_valid():
        binary_code = translation_form.cleaned_data['binary_code']
        translated_text = binary_to_text(binary_code)

    context = {
        'form': translation_form,
        'translated_text': translated_text,
    }
    return render(request, 'translator.html', context)


