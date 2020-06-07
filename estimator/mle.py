

from estimator import AEstimator


class MaxLikelihoodEstimator(AEstimator):
    """
    The estimator using maximum likelihood. We hide the pseudocount in here to be used with LaPlace smoothing.
    By default it is set to 0, which means no smoothing occurs.
    """

    def __init__(self, pseudocount=0):
        """
        Constructor for the class
        :param pseudocount: Sets the pseudocount value for the object. This enables Laplace smoothing at no extra
        cost.
        """
        self._model = dict()
        self._alpha = pseudocount
        self._N = 0
        self._V = 0

    def train(self, samples):
        """
        Train the estimator. We record N, the number of instances seen, and d, the number of different items.

        :param samples: The sample for training
        :return: None
        """    
        for i in samples:

            if i in self._model :
                self._model[i] += 1
                
            else:
                self._model[i] = 1
                
        self._N = self._model    
        
        
        self._V = len(set(item for key in self._N for item in key))
        
        
        return None
    
        raise NotImplementedError("The training method for the MLE model has not been implemented yet.")

    def p(self, evidence, history):
        """
        Return the value of v from the samples
        :param evidence: The provided evidence
        :param history: The history to take into account.
        :return: The probability of v
        """
        
        probability1 = self._N[history,evidence]
        key_data = [key[0] for key in self._N.keys()]
        key_data2 = [key[1] for key in self._N.keys()]
        count = 0
        count2 = 0
        
        def occurences (history):
            
            
            count = 0
            if (history in key_data):
                
                 count = 1
            else:
                 count = 0

            #Second part
            

            
           
            if (history in key_data2):
                count2 = 1
            else:
                count2 = 0

               

            return(count+count2)
        
        if (self._alpha == 0):
            Probability = probability1/occurences (history)
        else:
            Probability = (probability1+self._alpha)/(occurences (history)+self._V)
        
          
               
        return (occurences (history))
        raise NotImplementedError("The p method for the MLE model has not been implemented yet.")




