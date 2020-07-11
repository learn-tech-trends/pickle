import pickle

sample_dict = {
    "key" : "value",
    (0,1) : [1,2,3,4,5],
     1 : [2,34],
    }

with open("sample.txt","wb") as f:
    pickle.dump(sample_dict,f)


del sample_dict






