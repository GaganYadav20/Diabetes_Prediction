import numpy as np
import pickle

loaded_model = pickle.load(open('diabetes_prediction_model.sav', 'rb'))
input_data=(8,183,64,0,0,23.3,0.672,32)
input_data_as_np_arr=np.array(input_data)
input_data_reshape=input_data_as_np_arr.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshape)

if prediction[0]==0:
    print("The person is not diabetic")
else:
    print("The person is diabetic")