import scipy.io
import os
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

class ARMA_fit(object):

    def __init__(self, TimeSeries):
    	self.TimeSeries = np.array(TimeSeries)

    def arma_mod(self, p_val, q_val):
        model = sm.tsa.ARMA(self.TimeSeries, (p_val,q_val)).fit()
        return model
        aic1=np.log(np.var(model.resid))*N+N+2*(p+q+1)
        aic2=np.log(np.var(model.resid))*N+N+2*(p+q+1)*N/(N-2-p-q)
        return {'AIC1':aic1, 'AIC2':aic2 ,'y2':y2 }
        

data = scipy.io.loadmat('ECMWF/N_temp.mat')
N_temp = np.asarray(data['N_temp'])

x = N_temp[20,]
model,aic1,aic2 = ARMA_fit(x).arma_mod(1,0,'nc')
coef_p = model.arparams

x = N_temp[20,]
modelp= ARMA_fit(x).ar_mod(2,'nc')
coef_p = modelp.params

tau_p = np.var(model.resid)/np.square((1-np.sum(coef_p)))/np.var(x)

x = modelp.resid
p=0;q=1
modelq,aic1,aic2 = ARMA_fit(x).arma_mod(p,q,'nc')

coef_p = modelq.arparams
coef_q = modelq.maparams
tmp = [np.square(num) for num in coef_q]
factor = 1+np.sum(tmp)

tau_pq = factor*tau_p


