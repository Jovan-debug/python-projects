import requests

base_url="https://wttr.in"



class WeatherCondition:
    def __init__(self,city:str=None,temp_c:int=0,humidity:int=0,pressure:int=0):
        self.city=city
        self.temp_c=temp_c
        self.humidity=humidity
        self.pressure=pressure

    def get_info(self,name:str):
        self.city=name
        url=f"{base_url}/{self.city}?format=j1"
        try:
            response=requests.get(url=url)
            if response.status_code==200:
                data=response.json()
                self.temp_c=data['current_condition'][0]['temp_C']
                self.humidity=data['current_condition'][0]['humidity']
                self.pressure=data['current_condition'][0]['pressure']
            else :
                print(f"Error to retreive data")
                return None
        except requests.exceptions.JSONDecodeError:
            print("Error: Could not parse response as JSON.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None

    def info_display(self):
        print(f"weather condition of {self.city}:")
        print(f"Temperature:{self.temp_c}c")
        print(f"Humidity:{self.humidity}%")
        print(f"Pressure:{self.pressure}atm")


def main():
    print("***Welcome to our Weather app***")
    weather=WeatherCondition()
    while True:

        name=input("Enter the name f the city to get it's weather condition or q to exit:")
        if name.lower() =="q":
            print("Thank you for using our program")
            break
        else:
            weather.get_info(name=name)
            weather.info_display()


if __name__=="__main__":
    main()


