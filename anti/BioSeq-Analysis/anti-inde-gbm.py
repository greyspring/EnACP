#-*- coding: UTF-8 -*-
from sklearn.metrics import accuracy_score
from sklearn import svm
import lightgbm as lgb
import sys
import glob
import pandas as pd
from imblearn.over_sampling import SMOTE
import numpy as np

def main(argv):

    file_predict=argv[0]
    feature_path ="Input_data/Input_data_feature/19-inde"
    feature_file = glob.glob(feature_path+'/*')
    print feature_file
    data_List = datadic(feature_file)
    data = trainmodel_GBM(data_List)
    from sklearn.externals import joblib
    SVM_path="model/SVM_model/"
    #joblib.dump(model,SVM_path+"SVM_model.pkl")
    model1 = joblib.load(SVM_path+"SVM_model.pkl")
    result = model1.predict(data)
    print result
    # print model1
    # print ("Done\n")
    # print file_predict


#合并编号对应阳阴训练集或测试集并保存
def datadic(feature_file):
    #11 features
#    method = ["kmer","feature-AC.csv","ACC.csv","feature-CC.csv","DP.csv","DR.csv","PC-PseAAC.csv","PC-PseAAC-General.csv","PDT.csv","SC-PseAAC.csv","SC-PseAAC-General.csv"]
#    method = ["feature-AC.csv","ACC.csv","feature-CC.csv","DP.csv","DR.csv","PC-PseAAC.csv","PC-PseAAC-General.csv","PDT.csv","SC-PseAAC.csv","SC-PseAAC-General.csv"]

#    method = ["ACC.csv","DP.csv","DR.csv","PC-PseAAC.csv","PC-PseAAC-General.csv","PDT.csv","SC-PseAAC.csv","SC-PseAAC-General.csv"]
#    method = ["feature-AC.csv","DP.csv"]
#    method = ["-PSSM-RT.csv","-PSSM-DT.csv","-CC-PSSM.csv","-AC-PSSM.csv","ACC-PSSM.csv","kmer","feature-AC.csv","ACC.csv","feature-CC.csv","DP.csv","DR.csv","PC-PseAAC.csv","PC-PseAAC-General.csv","PDT.csv","SC-PseAAC.csv","SC-PseAAC-General.csv"]
    method = ["txt-DT.csv","feature-CC.csv","-PDT-Profile.csv","-Top-n-gram.csv","-PSSM-RT.csv","-PSSM-DT.csv","-CC-PSSM.csv","-AC-PSSM.csv","ACC-PSSM.csv","kmer","feature-AC.csv","ACC.csv","DP.csv","DR.csv","PC-PseAAC.csv","PC-PseAAC-General.csv","PDT.csv","SC-PseAAC.csv","SC-PseAAC-General.csv"]
    method = ["feature-CC.csv","feature-DT.csv","-PDT-Profile.csv","-Top-n-gram.csv","-PSSM-RT.csv","-PSSM-DT.csv","-CC-PSSM.csv","-AC-PSSM.csv","ACC-PSSM.csv","kmer","feature-AC.csv","ACC.csv","DP.csv","DR.csv","PC-PseAAC.csv","PC-PseAAC-General.csv","PDT.csv","SC-PseAAC.csv","SC-PseAAC-General.csv"]

    #method = ['AC.csv']
    featureDic={}
    for methodname in method:
        for i in feature_file:
            if methodname in i:
                featureDic[methodname]=i
                break

    for feature_name in featureDic:
        feature_path=featureDic[feature_name]

        dataset = pd.read_csv(feature_path,header=None,low_memory=False)
        print feature_path
        print dataset.shape
        dataset = dataset.convert_objects(convert_numeric=True)
        dataset.dropna(inplace = True)
        featureDic[feature_name]=dataset


    return featureDic


def svm_best_parameters_cross_validation(train_x, train_y):
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC    
    model = SVC(probability=True)
    #param_grid = {'kernel':('linear', 'rbf'),'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.001, 0.0001]}    
    param_grid = {'C': [1e-7,1e-6,1e-5,1e-4,1e-3, 1e-2, 1e-1, 1, 10, 100, 1000,10000,100000], 'gamma':[1e-7,1e-6,1e-5,1e-4,1e-3, 1e-2, 1e-1, 1, 10, 100, 1000,10000]}
    grid_search = GridSearchCV(model, param_grid, n_jobs = -1, verbose=1,cv=10)    
    grid_search.fit(train_x, train_y)    
    best_parameters = grid_search.best_estimator_.get_params()    
    for para, val in list(best_parameters.items()):    
        print(para, val)    
    model = SVC(C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)    
    model.fit(train_x, train_y)    
    return model

#多重子模型分类



def trainmodel_mutipleModel(datadic):
    train_feature = {}
    test_feature  = {}
    metrics = {}
    index=[]
    for i in datadic:
        data = datadic[i]



        (y_pred_train, y_pred_test) = trainmodel_multipleTags(data[0], data[1], data[2], data[3])
        # y_pred_train_和y_pred_test 是多个预测结果的列表

        feature_SVM = i+"_"+"SVM"
        feature_DT = i+"_"+"DT"
        feature_NB = i+"_"+"NB"
        feature_Knn = i+"_"+"Knn"

        train_feature[feature_Knn] = y_pred_train[0]
        train_feature[feature_NB] = y_pred_train[1]
        train_feature[feature_SVM] = y_pred_train[2]
        train_feature[feature_DT] = y_pred_train[3]

        test_feature[feature_Knn] = y_pred_test[0]
        test_feature[feature_NB] = y_pred_test[1]
        test_feature[feature_SVM] = y_pred_test[2]
        test_feature[feature_DT] = y_pred_test[3]

    train_feature_vector = pd.DataFrame(train_feature)
    test_feature_vector  = pd.DataFrame(test_feature)
    data[0] = train_feature_vector.values
    data[2] = test_feature_vector.values
    return data

#子模型分类
def trainmodel_GBM(datadic):
    train_feature = {}
    test_feature  = {}
    metrics = {}
    count_model=0
    for feature_name in datadic:
        y_pred = lightgbmTrainStag(datadic[feature_name],feature_name)
        test_feature[feature_name]=y_pred
    test_feature_vector  = pd.DataFrame(test_feature)
    new_Feature= test_feature_vector.values

    return new_Feature
	# return model

#训练11个模型
def lightgbmTrainStag(data,featurename):
    model_path="model/lightgbm_model/"
    clf = lgb.Booster(model_file=model_path+'lightgbm_model'+featurename+'.txt')
    print model_path+'lightgbm_model'+featurename+'.txt'
    y_pred=clf.predict(data,num_iteration=clf.best_iteration)
    # y_raw =clf.predict(data,raw_score=True,num_iteration=clf.best_iteration)
    return y_pred

if __name__ == '__main__':
	main(sys.argv)