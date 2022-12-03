import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("happybase.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     'first': 'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })


users_ref = db.collection(u'users')  # reference to a collection
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


a_lovelace_ref = db.collection(u'users').document(u'alovelace')  # reference to a document
a_lovelace_ref_2 = db.document(u'users/alovelace')  # second method to refer the document


room_a_ref = db.collection(u'rooms').document(u'roomA')
message_ref = room_a_ref.collection(u'messages').document(u'message2')  # subcollection1 and subcollection2
message_ref.set({
     'first': 'Fedor',
     'middle': 'Dan',
     'last': 'Bulkin',
     'born': 2000
})


cities = db.collection(u'cities')

sf_landmarks = cities.document(u'SF').collection(u'landmarks')
sf_landmarks.document().set({
    u'name': u'Golden Gate Bridge',
    u'type': u'bridge'
})
sf_landmarks.document().set({
    u'name': u'Legion of Honor',
    u'type': u'museum'
})
la_landmarks = cities.document(u'LA').collection(u'landmarks')
la_landmarks.document().set({
    u'name': u'Griffith Park',
    u'type': u'park'
})
la_landmarks.document().set({
    u'name': u'The Getty',
    u'type': u'museum'
})
dc_landmarks = cities.document(u'DC').collection(u'landmarks')
dc_landmarks.document().set({
    u'name': u'Lincoln Memorial',
    u'type': u'memorial'
})
dc_landmarks.document().set({
    u'name': u'National Air and Space Museum',
    u'type': u'museum'
})
tok_landmarks = cities.document(u'TOK').collection(u'landmarks')
tok_landmarks.document().set({
    u'name': u'Ueno Park',
    u'type': u'park'
})
tok_landmarks.document().set({
    u'name': u'National Museum of Nature and Science',
    u'type': u'museum'
})
bj_landmarks = cities.document(u'BJ').collection(u'landmarks')
bj_landmarks.document().set({
    u'name': u'Jingshan Park',
    u'type': u'park'
})
bj_landmarks.document().set({
    u'name': u'Beijing Ancient Observatory',
    u'type': u'museum'
})
