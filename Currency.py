import requests
base_url="https://open.er-api.com/v6/latest/"

class CurrencyConverter:
    def __init__(self,base_currency:str,target_currency:str,amount:float =0):
        self.base_currency=base_currency
        self.target_currency=target_currency
        self.amount=amount

    def get_info(self):

        url=f"{base_url}{self.base_currency}"
        old=self.amount
        try:
            response=requests.get(url=url)
            if response.status_code==200:
                data=response.json()
                self.amount=self.amount * data['rates'][self.target_currency]
                print(f"{old}{self.base_currency} is equivalent to {self.amount}{self.target_currency}")
            else:
                print("fail to retreive data")
                return None

        except requests.exceptions.JSONDecodeError:
                print("Error: Could not parse response as JSON.")
                return None
        except requests.exceptions.RequestException as e:
                print(f"Network error: {e}")
                return None

def get_input(prompt:str):
     while True:
          raw=input(prompt)
          if raw.upper() and len(raw)==3:
               return raw
          else:
               print("Enter a valid currency eg USD,XAF,CAD")


def get_amount(prompt:str):
     while True:
          raw=input(prompt)
          if raw.isdigit():
               return float(raw)
          else:
               print("enter a valid amount")
def main():
     print("**********Welcome to our currency program********")
     base_cur=get_input("Enter the base  currency:")
     amt=get_amount("Enter the amount to convert:")
     target_cur=get_input("enter the target currency:")

     Converter=CurrencyConverter(base_currency=base_cur,target_currency=target_cur,amount=amt)
     Converter.get_info()

if __name__=="__main__":
     main()
