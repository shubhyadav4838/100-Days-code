import requests
AMOUNT = 10
TYPE = "boolean"
parameter = {
    "type": TYPE,
    "amount": AMOUNT
}
question_data=[]

connect = requests.get(url="https://opentdb.com/api.php", params=parameter)
connect.raise_for_status()
question_data = connect.json()["results"]
