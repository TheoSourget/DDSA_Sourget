import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from ast import literal_eval

random.seed(1907)
np.random.seed(1907)

"""
data: training data (only x as it's one class classification)
nb_exemples : Number of training exemples taken randomly before training a DecisionTree (Bagging)
nb_outlier : Number of outlier generated before training a Tree
nb_classif: Number of tree in the forest
nb_features_RSM : Number of feature taken randomly before training a DecisionTree (Random Subspace Method)
nb_features_RFS : Number of feature taken randomly when growing a DecisionTree (Random Feature Selection)
"""
def OCRF(train_data,nb_exemples,nb_outlier,nb_classif=200,nb_features_RSM=10,nb_features_RFS="sqrt"):
    lstModel = []
    
    for _ in range(nb_classif):
        #Bagging
        selected_x = np.array(random.choices(train_data,k = nb_exemples))

        #Random Subspace Method
        selected_features = random.sample(range(selected_x.shape[1]),k = nb_features_RSM)
        x_true = np.array([x[selected_features] for x in selected_x])
        y_true = np.array(["Cardiac" for x in x_true])

        #Outlier generation
        #Compute H_target and H_outlier (1-H_target)
        H_target = np.sum(x_true,axis = 0)
        print(H_target)
        H_target = H_target/sum(H_target)
        H_outlier = 1 - H_target

        #Generate new data with H_outlier
        x_outlier = []
        for n in range(nb_exemples):
            x_outlier.append((np.random.rand(nb_features_RSM) < H_outlier).astype(int))

        x_outlier = np.array(x_outlier)  
        y_outlier = np.array(["Outlier" for x in x_outlier])
        
        #Create augmented dataset
        x_train = np.concatenate((x_true,x_outlier),axis=0)
        y_train = np.concatenate((y_true,y_outlier),axis=0)
        #Training of the model
        current_model = DecisionTreeClassifier(max_features=nb_features_RFS)
        current_model.fit(x_train,y_train)

        lstModel.append((current_model,selected_features))
    return lstModel

def decisionOCRF(test_data,lstModel):
    ensemblePrediction = []
    for model in lstModel:
        m = model[0]
        selected_features = model[1]
        x_subspace = np.array([x[selected_features] for x in test_data])
        ensemblePrediction.append(m.predict(x_subspace))
    ensemblePrediction = np.array(ensemblePrediction)

    pred = []
    for i in range(len(test_data)):
        preds = ensemblePrediction[:,i]
        print(preds)
        pred.append(max(preds,key=list(preds).count))
    #accuracy = sum(pred == "Cardiac")/len(pred)
    return pred

if __name__ == "__main__":
    with open('./data/keywordsHist_ACDC.csv','r') as f:
        df_hist = pd.read_csv(f)
        df_hist = df_hist[df_hist["hist"] != "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"]
        df_hist["hist"] = df_hist["hist"].apply(literal_eval)
    data = []
    for d in df_hist["hist"].to_numpy():
        data.append(d)
    data = np.array(data)
    
    X_train, X_test = train_test_split(data, test_size=0.1, random_state=1907)
    
    print(len(X_train),len(X_test))
    
    lstModel = OCRF(X_train,X_train.shape[0],100000)
    #print(decisionOCRF(X_test,lstModel))

    print(decisionOCRF(np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),lstModel))