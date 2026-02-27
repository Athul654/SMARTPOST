from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import base64
import json
from openai import OpenAI

def chatbot(request):
    return render(request, 'chatinterface.html')

client = OpenAI(api_key="")

@csrf_exempt
def image_to_caption(request):
    if request.method == "POST":
        image_file = request.FILES.get("image")

        if not image_file:
            return JsonResponse({"error": "No image provided"}, status=400)

        image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        prompt = """
        You are a social media expert. 
        Analyze the given image and generate:
        1. One engaging Instagram caption
        2. 8-12 relevant hashtags
        
        Format your response exactly like this:
        [Your caption text here]
        

        #hashtag1 #hashtag2 #hashtag3
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}},
                    ],
                }
            ],
            max_tokens=300,
        )

        ai_text = response.choices[0].message.content

        return JsonResponse({"result": ai_text})

    return JsonResponse({"error": "Invalid request"}, status=400)