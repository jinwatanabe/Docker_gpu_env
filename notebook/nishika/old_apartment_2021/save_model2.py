import pickle
import datetime

def save_model_params(model):
    dt_now = datetime.datetime.now()
    
    file = './models/' + str(dt_now.month) + str(dt_now.day) + '_trained_model.pkl'
    pickle.dump(model, open(file, 'wb'))