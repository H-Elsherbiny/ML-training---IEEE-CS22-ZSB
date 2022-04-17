import pandas as pd
import numpy as np


n = ["ones", "gender", "age", "hypertension","heart_disease", "ever_married", 
     "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status"]


def cleaning_data():
    df = pd.read_csv("healthcare-dataset-stroke-data.csv")
    
    rescaling_data = ["age", "avg_glucose_level", "bmi"]
    df[rescaling_data] = (df[rescaling_data] - df[rescaling_data].mean()) / df[rescaling_data].std()
    
    temp = (df["stroke"] == 1) & (df["smoking_status"] == "Unknown")
    df.loc[temp, "smoking_status"] = "formerly smoked"
    
    temp = (df["stroke"] == 0) & (df["smoking_status"] == "Unknown")
    df.loc[temp, "smoking_status"] = "never smoked"
    
    df["bmi"].fillna(df["bmi"].mean(), inplace=True)
    
    df.drop("id", axis=1, inplace=True)
    df.insert(0, "ones", 1)
    
    
    df["gender"].replace("Male", 0, inplace=True)
    df["gender"].replace("Female", 1, inplace=True)
    df["gender"].replace("Other", 1, inplace=True)
    
    
    df["ever_married"].replace("Yes", 1, inplace=True)
    df["ever_married"].replace("No", 0, inplace=True)
    
    
    df["work_type"].replace("Private", 0, inplace=True)
    df["work_type"].replace("Self-employed", 1, inplace=True)
    df["work_type"].replace("Govt_job", 2, inplace=True)
    df["work_type"].replace("children", 3, inplace=True)
    df["work_type"].replace("Never_worked", 4, inplace=True)
    
    
    df["Residence_type"].replace("Rural", 0, inplace=True)
    df["Residence_type"].replace("Urban", 1, inplace=True)


    df["smoking_status"].replace("formerly smoked", 0, inplace=True)
    df["smoking_status"].replace("never smoked", 1, inplace=True)
    df["smoking_status"].replace("smokes", 2, inplace=True)
    
    df = df.sample(frac = 1)
        
    return df


def split(df):
    k = 2
    size = len(df.index) // 2
    df_mat = [0, 0]
    for i in range(k):
        df_mat[i] = df[size * i: size * (i + 1)]
        
    return df_mat[0], df_mat[1]
    

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def hypothesis(x, thetas):
    z = np.dot(x, thetas.T)
    a = sigmoid(z)
    return a


def cost(thetas, x, y):
    J = 0
    for i in range(len(x)):
        J += (-np.log(hypothesis(x[i], thetas))) * y[i]
        J += (-np.log(1 - hypothesis(x[i], thetas))) * (1 - y[i])
    return J / len(x)


def gradient_descent(x, y, thetas, alpha):
    m = len(x)
    num = len(thetas)
    segma = [0] * num
    for t in range(20):
        
        for i in range(m):
            for j in range(num):
                segma[j] += (hypothesis(x[i], thetas) - y[i]) * x[i][j]
                
        for j in range(num):
            thetas[j] -= alpha * segma[j] / m
            
    return thetas
            


def training(df):
    X = df[n].values
    y = np.matrix(df['stroke'].values).T
    thetas = np.zeros(X[1].shape)
    
    grads = gradient_descent(X, y, thetas, 0.01)
    J = cost(grads, X, y)
    
    return grads ,J


def check(df, thetas):
    counter = 0
    X = df[n].values
    y = np.matrix(df['stroke'].values).T
    
    for i in range(len(df.index)):
        predict = hypothesis(X[i], thetas)
        
        if round(predict) == y[i]:
            counter += 1
    
    return counter / i * 100


def main():
    df_training, df_check = split(cleaning_data())

    thetas, J = training(df_training)
    J = J.tolist()
    accuracy = check(df_check, thetas)
    
    print("Cost = ", round(J[0][0], 2))
    print("Accuracy = ", round(accuracy, 2), "%")
    
     
    
main()