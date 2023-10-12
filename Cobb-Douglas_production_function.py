
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns; sns.set_theme(color_codes=True)
from scipy.stats import pearsonr
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols


data = pd.read_stata("/Users/martinfranco/Desktop/Universität/Mikroökonomik/Applied Microeconometrics/Exercises/dta/production.dta")
data.to_csv("/Users/martinfranco/Desktop/Universität/Mikroökonomik/Applied Microeconometrics/Exercises/dta/production.dta")
print(data)


####focus on only year 1958.
year1958 = data[data["year"] == 58]
year1958.head()

#### Let´s transform the Cobb-Douglas production function to a linear equation by taking logs.
#### Cobb- Douglas production function being Y_i = A * K_i^α * L_I^β where Y_i is a measure of output, K_i is the capital stock, and Li is employment.
#### A is a ratio of output to total input, and reflects the overall efficiency of the production process. 
#### Transformation to a linear equation by taking logs = ln(Y_i) = ln(A) + αln(K_i) + βln(L_i)

log_emp = np.log(year1958["emp"]) 
log_cap = np.log(year1958["cap"]) 
log_vadd = np.log(year1958["vadd"])

#### OLS regression of log_vadd on log_emp and log_cap

x = pd.concat([log_cap, log_emp], 1) 
y = log_vadd
model_1 = sm.OLS(y, sm.add_constant(x)) 
print(model_1.fit().get_robustcov_results(cov_type = "HC1").summary())

#### Our α is 0.2761 and our β is 0.6975. 
#### This means that a 1% increase in capital usage would lead to a 0.28% increase in output, and a 1% increase in employment would lead to a 0.70% increase in output.

#### Now let´s test whether the estimates are consistent with the production function exhibitingconstant returns to scale, i.e.
#### H0: α + β = 1 vs H1: α + β != 1

results = ols("np.log(vadd) ~ np.log(cap) + np.log(emp)", year1958).fit().get_robustcov_results(cov_type="HC1") 
hypothesis = "np.log(cap) + np.log(emp) = 1"
t_test = results.t_test(hypothesis)
print(t_test)

#### 1 is within the 95% confidence interval so we cannot firmly reject the null hypothesis that the production function exhibits constant returns to scale at the 5% level.

#### Now the F-test

f_test = results.f_test(hypothesis) 
print(f_test)

#### p-value of 0.0497 in the F-test so we cannot firmly reject the null hypothesis at the 5% level.

#### An alternative way of specifying the production function is to define Yi as the total value of shipments and to add materials as a factor of production.
#### We can transform the equation as following by substituting the parameter β with α + β − 1 = θ <=> β = θ + 1 − α
#### This leads us to ln(Y_i) = ln(A) + αln(K_i) + βln(L_i) + e_i <=> ln(Y_i /L_i) = ln(A) + αln(K_i /L_i) + θln(L_i) + e_i

#### Let´s test the hypothesis that the parameter θ equals 0.

results_1 = ols("np.log(vadd/emp) ~ np.log(cap/emp) + np.log(emp)", year1958).fit().get_robustcov_results(cov_type = "HC1") 
hypothesis_1 = "np.log(emp) = 0"
t_test_1 = results_1.t_test(hypothesis_1)
print(t_test_1)

f_test_1 = results_1.f_test(hypothesis_1)
print(f_test_1)

#### The parameter θ is too close to zero. On 5% and 1% levels, we cannot firmly reject the null hypothesis that α + β = 1.

#### Let´s add matcost as a factor of production to the model and use Y_i as the total value of shipments vship.


results_2 = ols("np.log(vship) ~ np.log(cap) + np.log(emp) + np.log(matcost)", year1958).fit().get_robustcov_results(cov_type = "HC1") 
print(results_2.summary())

####  α, β and γ are 0.11, 0.26 and 0.62 respectively.

t_test_2 = results_2.t_test("np.log(cap) + np.log(emp) + np.log(matcost) = 1")
print(t_test_2)

f_test_2 = results_2.f_test("np.log(cap) + np.log(emp) + np.log(matcost) = 1")
print(f_test_2)

#### Not statistically significant.

#### Now add energy as a fourth factor of production.

results_3 = ols("np.log(vship) ~ np.log(cap) + np.log(emp) + np.log(matcost) + np.log(energy)", year1958).fit().get_robustcov_results(cov_type = "HC1")
print(results_3.summary())

t_test_3 = results_3.t_test("np.log(cap) + np.log(emp) + np.log(matcost) + np.log(energy) = 1")
print(t_test_3)

#### Energy does not seem to be a significant factor of production. 
#### Energy is considered mainly as fixed costs and is not freely doubled or reduced as other factors such as labour, capital or materials.




















