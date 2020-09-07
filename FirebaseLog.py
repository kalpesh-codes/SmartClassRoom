from firebase import firebase
firebase = firebase.FirebaseApplication('https://fingerprint-5e700.firebaseio.com', None)
new_user = 'Ozgur Vatansever'

result = firebase.post('/users', new_user,{'X_FANCY_HEADER': 'VERY FANCY'})
print result
