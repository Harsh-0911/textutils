from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Render homepage of the website.
    return render(request, 'index.html')

def analyze(request):
    """ Analyze the data """
    # Get all checkboxes values 
    # It is in form of 'on' or 'off'.
    removepunc = request.POST.get('removepunc', 'off')
    removeline = request.POST.get('removeline', 'off')
    removespace = request.POST.get('removespace', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    upper = request.POST.get('upper', 'off')
    lower = request.POST.get('lower', 'off')

    # Get the text data from the form.
    text = request.POST.get('data', 'default')
    
    # This variable is used to check whether user has selected any option or not.
    # If false then user has selected nothing.
    flag = False

    # Creating a dictonary of the variables that are used in the template.
    analyzed_text = ''
    params = {'data' : analyzed_text}

    # Defining the 'Lower' functionality.
    if lower == 'on':
        flag = True
        analyzed_text = ''
        analyzed_text = text.lower()
        params = {'data' : analyzed_text}
        text = analyzed_text

    # Defining the 'Upper' functionality.
    if upper == 'on':
        flag = True
        analyzed_text = ''
        analyzed_text = text.upper()
        params = {'data' : analyzed_text}
        text = analyzed_text

    # Defining the 'Capitlize' functionality.
    if capitalize == 'on':
        flag = True
        analyzed_text = ''
        analyzed_text = text.capitalize()
        params = {'data' : analyzed_text}
        text = analyzed_text

    # Defining the 'Remove new line' functionality.
    if removeline == 'on':
        flag = True
        analyzed_text = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_text += char
        params = {'data' : analyzed_text}
        text = analyzed_text

    # Defining the 'Remove extra spaces' functionality.
    if removespace == 'on':
        flag = True
        analyzed_text = ''
        # Using enumerate to get indexes. 
        for index, char in enumerate(text):
            # Used try-except block to overcome the "index out of the range error".
            try:
                if not(text[index] == " " and text[index+1] == " "):
                    analyzed_text += char
            except:
                pass
        params = {'data' : analyzed_text}
        text = analyzed_text

    # Defining the 'Remove punctuation' functionality.
    if removepunc == 'on':
        flag = True
        analyzed_text = ''
        # string of all possible punctuations.
        punc = '''"'/\[]{}(),.:;-_!~`^'''
        for char in text:
            if char not in punc:
                analyzed_text += char
        params = {'data' : analyzed_text}
        text = analyzed_text

    # If user selects nothing then original data will be sent back.   
    if flag == False:
        analyzed_text = ''
        analyzed_text = text
        params = {'data' : analyzed_text}

    # Rendering the final page
    return render(request, 'final.html', params)