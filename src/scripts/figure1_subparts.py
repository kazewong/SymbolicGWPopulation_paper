import matplotlib.pyplot as plt
from pysr import *
import numpy as np
import sympy
import pandas as pd
from sympy import preorder_traversal, Float


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Raman'
plt.rcParams['text.usetex'] = True

GWTC = np.load('./src/data/GWTC3_posterior.npz')
m1 = GWTC['m1']
from scipy.stats import gaussian_kde
m1_axis = np.linspace(0,100,1000)
fig, ax = plt.subplots(1,1,figsize=(10,9))
for i in range(79):
    kde = gaussian_kde(m1[i,::10])
    ax.plot(m1_axis,kde(m1_axis),c='grey',alpha=0.5)
ax.set_yscale('log')
ax.set_ylim(1e-3,3)
ax.set_xlim(0,100)
ax.set_xlabel(r'$m_{1,i}\ [M_{\odot}]$',fontsize=20)
ax.set_ylabel(r'$p(m_{1,i})$',fontsize=20)
ax.tick_params(axis='x',labelsize=16)
ax.tick_params(axis='y',labelsize=16)
ax.set_title('Data',fontsize=24)
fig.savefig('./figure/GWTC3_m1_data.pdf',bbox_inches='tight')


def get_data():
    data = np.load("GWTC3_m1_spectrum.npz")
    X = data["axis"]

    X = np.concatenate(
        [
            X,
            np.array([1e-9, 1e9]),
        ]
    )

    # Samples: [5, 50, 95]
    y_med = np.log(data["pm1_med"])
    y_low = np.log(data["pm1_low"])
    y_high = np.log(data["pm1_high"])

    y_med = np.concatenate([y_med, np.array([-8, -8])])
    y_low = np.concatenate([y_low, np.array([-12, -12])])
    y_high = np.concatenate([y_high, np.array([-6, -6])])

    stdev = (y_high - y_low) / 4
    snr = 1 / stdev**2

    X = pd.DataFrame(
        {
            "logM": np.log(X),
            "M": X,
            "logP": y_med,
            "snr": snr,
            "stdev": stdev,
            "logP_med": y_med,
            "logP_low": y_low,
            "logP_high": y_high,
        }
    )
    return X

def round_expression(ex1):
    ex2 = ex1
    for a in preorder_traversal(ex1):
        if isinstance(a, Float):
            ex2 = ex2.subs(a, round(a, 2))
    return ex2

Gauss = lambda x: sympy.exp(-(x**2))
Cond = lambda x, y: sympy.Piecewise((0, x < 0), (y, True))
model = PySRRegressor(
        binary_operators=["+", "-", "*", "pow", "cond(x,y)= x >= 0 ? y : 0", "custompow(x,y) = x > 0 ? x^y : -100"],
    unary_operators=["square", "gauss(x)=exp(-x^2)"],
    equation_file="multinode_search_gwaves_with_nested_constraints4.txt",
    extra_sympy_mappings={
        "gauss": lambda x: sympy.exp(-(x**2)),
        "square": lambda x: x**2,
        "custompow": lambda x, y: sympy.Pow(x,y),
        "cond": lambda x, y: sympy.Piecewise((0, x < 0), (y, True)),
    },
    variable_names=["M"],
)
model.set_params(n_features=1)
model.refresh()
model.set_params(model_selection='accuracy')

X = get_data()
index = 10
f = model.equations.iloc[index]["lambda_format"]
y1 = f(X[["M"]])

index = 15
f = model.equations.iloc[index]["lambda_format"]
y2 = f(X[["M"]])

index = 30
f = model.equations.iloc[index]["lambda_format"]
y3 = f(X[["M"]])

model = PySRRegressor(
        binary_operators=["+", "-", "*", "pow", "cond(x,y)= x >= 0 ? y : 0", "custompow(x,y) = x > 0 ? x^y : -100"],
    unary_operators=["square", "gauss(x)=exp(-x^2)"],
    equation_file="multinode_search_gwaves_with_nested_constraints4.txt",
    extra_sympy_mappings={
        "gauss": lambda x: sympy.Function("Gauss")(x),#sympy.exp(-(x**2)),
        "square": lambda x: x**2,
        "custompow": lambda x, y: sympy.Pow(x,y),
        "cond": lambda x, y: sympy.Function("Cond")(x,y),#sympy.Piecewise((0, x < 0), (y, True)),
    },
    variable_names=["M"],
)
model.set_params(n_features=1)
model.refresh()
model.set_params(model_selection='accuracy')

index = 10
label1 = '$'+sympy.latex(round_expression(model.equations.iloc[index]["sympy_format"]))+'$'
label1 = label1.replace('operatorname','rm')
label1 = label1.replace('&','\&')

index = 15
label2 = '$'+sympy.latex(round_expression(model.equations.iloc[index]["sympy_format"]))+'$'
label2 = label2.replace('operatorname','rm')
label2 = label2.replace('&','\&')

index = 30
label3 = '$'+sympy.latex(round_expression(model.equations.iloc[index]["sympy_format"]))+'$'
label3 = label3.replace('operatorname','rm')
label3 = label3.replace('&','\&')




fig, ax = plt.subplots(1,1,figsize=(10,9))
ax.plot(X['M'].values[:-2],np.exp(X['logP'])[:-2],lw=5)
ax.fill_between(X['M'].values[:-2],np.exp(X['logP_low'][:-2]),np.exp(X['logP_high'][:-2]),alpha=0.14,color='C0')
ax.set_yscale('log')
ax.set_xlabel(r'$m_1\ [M_{\odot}]$',fontsize=20)
ax.set_ylabel(r'$d\mathcal{R}/dm_1\ [{\mathrm yr}^{-1}]$',fontsize=20)
ax.tick_params(axis='x',labelsize=16)
ax.tick_params(axis='y',labelsize=16)
ax.set_ylim(1e-6,2e1)
ax.set_xlim(0,100)
ax.set_title('Gaussian Mixture Model',fontsize=24)
fig.savefig('./figure/GWTC3_m1_GMM.pdf',bbox_inches='tight')


fig, ax = plt.subplots(1,1,figsize=(10,9))
ax.plot(X['M'].values[:-2],np.abs(y1[:-2]),label='Low complexity',lw=3)
ax.plot(X['M'].values[:-2],np.abs(y2[:-2]),label='Mid complexity',lw=3)
ax.plot(X['M'].values[:-2],np.abs(y3[:-2]),label='High complexity',lw=3)
ax.set_yscale('log')
ax.legend(loc='lower right',fontsize=16)
ax.set_xlabel(r'$m_1\ [M_{\odot}]$',fontsize=20)
ax.set_ylabel(r'$d\mathcal{R}/dm_1\ [{\mathrm yr}^{-1}]$',fontsize=20)
ax.tick_params(axis='x',labelsize=16)
ax.tick_params(axis='y',labelsize=16)
ax.set_ylim(1e-6,2e1)
ax.set_xlim(0,100)
ax.set_title('Symbolic Forms',fontsize=24)
fig.savefig('./figure/GWTC3_m1_PYSR.pdf',bbox_inches='tight')
