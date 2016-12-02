
"""Simple program that consumes open weather api and
    return conitons for particular cities"""

TOWNS = {1:"Nairobi", 2:"Mombasa", 3:"Kisumu", 4:"Kampala", 5:"Dodoma"}
def main():
    """main fxn"""
    #import
    import requests
    #cities GLOBAL VAR
    #function for requests to api
    def weather(arg):
        """function which send a request"""
        #request using get fxn from requests
        url = ('http://api.openweathermap.org/data'
        	      '/2.5/weather?q='+TOWNS[int(arg)]+'&APPID=b18ed1dc9ae803324cab0942f118d210')
        request = requests.get(url)
        response = request.json()
        return response
    #takes in argument
    city = str(raw_input('\n 1.Nairobi \n 2.Mombasa \n'
    	                    '3.kisumu \n 4.Kampala \n 5.Dodoma \n'
    	                    ' Enter Number of Your City of Choice From the list:'))

    #takes only number btwn 1 and 5
    if city in [str(i) for i in range(1, 6)]:
        condition = weather(city)
        print '\t------Weather Forecast For Today in '+ TOWNS[int(city)]+' -------:'
        #converted the temp to degree celcius -273
        print '\n \t Highs of '+ str(condition["main"]["temp_max"]-273.00)+' degrees'
        #converted the temp to degree celcius -273
        print '\n \t Lows of '+ str(condition["main"]["temp_min"]-273.00)+' degrees'
        print '\n \t humudity is '+ str(condition["main"]["humidity"])+ ' %s'
        print '\n \t Atmospheric pressure is '+str(condition["main"]["pressure"])+' pascals'
        print '\n \t Cloud Cover '+str(condition["clouds"]["all"])+' %'
    else:
        #raising error incase of number not 1-5
        print "Enter a valid Argument"
if __name__ == " __main__":
    main()
