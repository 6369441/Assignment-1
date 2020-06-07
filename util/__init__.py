
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost
    def distance(self, source, target):
        """
        Calculates the distance between two strings.
        :param source: The source string
        :param target: The target string
        :return: The scalar distance between the source and target.
        """
        #Calculate the Lenth of the two Strings
                
        n = len(target)
        m = len(source)
        
        # Initialize Matrix
        distance = [[0 for i in range(n + 1)] for i in range(m + 1)] 

         
        for i in range(m + 1): 
        
            for j in range(n + 1): 

                # If first string is empty
                if i == 0: 
                
                    distance[i][j] = j 

                # If second string is empty
                
                elif j == 0: 
                
                    distance[i][j] = i 
                    

                #Reccurence
                else: 
                    distance[i][j] = min(distance[i][j-1]+self._insert_cost,   
                                        distance[i-1][j]+self._deletion_cost,
                                        distance[i-1][j-1]+self._subst_cost if source[i-1] != target[j-1] 
                                                                            else distance[i-1][j-1] )  
   

        return distance[m][n] 
       
        raise NotImplementedError('Distance calculation not implemented yet')
        
#Get input from User, create object and print the distance        
source = input('Enter first word: ')
target = input('Enter Second word: ')
print(" ")        
obj1 = DistanceCalculator()
print("The Minimum Edit-Distance between",source,"and",target,"is",obj1.distance(source,target))

 
