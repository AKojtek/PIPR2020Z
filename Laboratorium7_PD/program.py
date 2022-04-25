"""
Program is built from class Polymonial. It enables a bunch of operations on it
- setting and getting polymonial of created object set_collection(), get_collection()
- finding the coefficient next to the argument of a given degree
"""


class Polynomial:
    def __init__(self,collection=None):
        self.set_collection(collection)
        degree = self.get_collection()[0][0]
        self.set_degree(degree)


    def check_if_correct(self,collection):
        if not collection:
            raise ValueError("Kolekcja nie może być pusta!")
        for element in collection:
            if int(element[0]) < 0 or isinstance(element[0], float):
                raise ValueError("Błędna wartość potęgi!")
            if [i[0] for i in collection].count(element[0])>1:
                raise ValueError("Powtórzona potęga!")
            if int(element[1]) == 0:
                raise ValueError("Błędna wartośc współczynnika!")


    def get_collection(self):
        return self._collection


    def set_collection(self,collection):
        self.check_if_correct(collection)
        new_collection = sorted(collection, key=lambda parametr: parametr[0], reverse=True)
        self._collection = new_collection

    def __str__(self):
        first = True
        string = ""
        for entity in self._collection:
            if not first and entity[1]>0:
                string += "+"
            else:
                first = False
            if(entity[0]>1):
                string += str(entity[1])+"x^"+str(entity[0])
            elif(entity[0]==1):
                string += str(entity[1])+"x"
            else:
                string += str(entity[1])
        return string



    def set_degree(self,degree):
        self._degree = degree


    def degree(self):
        return self._degree


    def coefficient(self,degree):
        # Przeszukaj kolekcje, jezeli ktora z wartosci ma stopien rowny przekazanemu argumentowi
        # zwrac ten wspolczynnik, w przeciwnym wypadku zwroc None
        for entity in self._collection:
            if entity[0] == degree:
                return entity[1]
        return None


    def value(self,x):
        """
        This method finds value of saved polymonial for given argument
        For this task it uses Horner Schema
        """
        first = True
        degree = self._degree
        my_collection = self.get_collection()
        for element in my_collection:
            if first:
                # First element doesn't require any calculations,
                # setting its value to be eual to its coefficient is enough
                value = element[1]
                first = False
                degree -= 1
            else:
                # It is necessary to multiply value by x as long as polynomial degree
                # is higher than degree of next element
                if degree > element[0]:
                    while degree > element[0]:
                        value = value * x
                        degree -= 1
                value = value * x + element[1]
                degree -= 1
        while degree>=0:
            value = value*x
            degree -= 1
        return value


    def add_to_collection(self,collection,degree,value):
        """
        Method adds element of given degree and coefficient into given collection
        """
        new_collection = []
        for elems in collection:
            if elems[0]==degree:
                if elems[1]+value != 0:
                    new_collection.append((elems[0],elems[1]+value))
            else:
                new_collection.append(elems)
        return new_collection


    def substract_from_collection(self,collection,degree,value):
        """
        Method substracts element of given degree and coefficient from given collection
        """
        new_collection = []
        for elems in collection:
            if elems[0]==degree:
                if elems[1]-value != 0:
                    new_collection.append((elems[0],elems[1]-value))
            else:
                new_collection.append(elems)
        return new_collection

    def add(self, second_polynomial):
        """
        Method realizes process of polynomials additions
        """
        main_collection = self.get_collection()
        second_collection = second_polynomial.get_collection()
        for element in second_collection:
            if self.coefficient(element[0]) == None:
                main_collection.append(element)
            else:
                main_collection = self.add_to_collection(main_collection,element[0],element[1])
        self.set_collection(main_collection)



    def substract(self, second_polynomial):
        """
        Method realizes process of polynomials substraction
        """
        main_collection = self.get_collection()
        second_collection = second_polynomial.get_collection()
        for element in second_collection:
            if self.coefficient(element[0]) == None:
                main_collection.append((element[0],-element[1]))
            else:
                main_collection = self.substract_from_collection(main_collection,element[0],element[1])
        self.set_collection(main_collection)