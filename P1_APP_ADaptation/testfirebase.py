from firebase import firebase




firebase = firebase.FirebaseApplication(
    'https://masterapptestadaptation-default-rtdb.firebaseio.com/',None)



data = {
    'Email': 'miroubelk@gmail.com',
    'Password' :'adapt2022',
    
}

firebase.post(
    'https://masterapptestadaptation-default-rtdb.firebaseio.com/Users',data)

result = firebase.get('https://masterapptestadaptation-default-rtdb.firebaseio.com/Users','')
print(result)