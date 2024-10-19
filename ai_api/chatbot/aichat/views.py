from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import requests
from .AI_Model_v2 import main as ai
from .AI_Model_v2 import agents

# Create your views here.
def home(request):
    print("HOME!")
    return HttpResponse("HOME!")


def test(request):
    print("test_crew!")
    pass


@csrf_exempt
@require_POST
def chat(request):
    try:
        body = json.loads(request.body)
        mensajes = body.get("message", "")
        
        last_message = mensajes[-1]["content"]
        # print("Last message: ", last_message)
        
        # * Check information/rules on the message
        # Checking products
        # db_require = ai.merge_instructions(agents.DataRetriver.goal, agents.DataRetriver.task_identify_db_use, mensajes[-7])
        

        llm_response = ai.ollama_llm(mensajes)
        response = {"reply": llm_response}

        return HttpResponse(json.dumps(response), content_type="application/json")
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON", status=400)

