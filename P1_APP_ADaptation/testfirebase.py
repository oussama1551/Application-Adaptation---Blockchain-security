def verify_data_login():
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://masterapptestadaptation-default-rtdb.firebaseio.com/',None)
        result = firebase.get('https://masterapptestadaptation-default-rtdb.firebaseio.com/Users','')




verify_data_login()