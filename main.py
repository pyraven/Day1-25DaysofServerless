import random
def spin_dreidel(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        dreidel_options = ['נ (Nun)', 'ג (Gimmel)', 'ה (Hay)', 'ש (Shin)']
        choice = random.choice(dreidel_options)
        message = f"{choice}\n#25daysofserverless2019"
        return message