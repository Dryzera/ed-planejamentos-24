from apis.models import PromptIa
from datetime import datetime

def verify_inferences(user):
    if user.is_authenticated:
        if user.groups.filter(name='Free').exists():
            prompts = PromptIa.objects.get(user=user)

            timestamp_of_last_inference = prompts.updated_at.timestamp()
            timestamp_of_one_day = 86400.000
            if datetime.now().timestamp() >= (timestamp_of_one_day + timestamp_of_last_inference):
                prompts.inference_counts = 0
                prompts.save()
            
            if prompts.inference_counts < 5:
                return True
            else:
                return False
        return True

    return False