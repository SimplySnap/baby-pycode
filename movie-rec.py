import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#Data set of movies with rating at least 4
data = fetch_movielens(min_rating = 4.0)

#print rating
print(repr(data['train']))
print(repr(data['test']))

#create model - weighted approximate pairwise. Uses gradient descent
model = LightFM(loss='warp')

#train model
model.fit(data['train'], epochs = 30, num_threads = 2)

def sample_rec(model,data,user_ids):
    #no users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recs for each user
    for user_id in user_ids:

        #Movies they already like
        known_positives = data['item_labels'][data['train'].toscr()[user_id].indices]

        #Movies our model predicts they'll like
        scores = model.predict(user_id, np.arange(n_items))

        #Rank in order of liked to least
        
        top_items = data['item_labels'][np.argsort()]

        #Print results
        print("User %s" % user_id)
        print("   Known positives:")

        for x in known_positives[:3]:
            print("      %s" % x)

        print("      Recommended:")

        for x in top_items[:3]:
            print("       %s" % x)

    
#Test
sample_rec(model, data, [6,21,104])

