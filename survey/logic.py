
from survey.models import ANSWERS, QUESTIONS, RESULTS, WEIGHT

def getResults(answer_list):
    
    #dictionary to store result ID key, weight value
    result_weights = {}
        
    for answerID in answer_list:
        # q is the answer ID
        # weight table must be queries by question ID for weight
        # most applicable results will be populated by descending weight
        answerID.encode('ASCII')#this might not be necessary
        
        optionWeights = WEIGHT.objects.filter(answer=answerID)
        
        for option in optionWeights:
            
            if option.result in result_weights:
                result_weights[option.result] = result_weights[option.result] + option.weight
            else:
                result_weights[option.result]=option.weight

    result_weights = sorted(result_weights.items(), key=lambda indx:indx[1], reverse=True)

    return result_weights

