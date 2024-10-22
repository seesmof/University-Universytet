import scipy.optimize as optimize

def f(params):
    x,y=params
    return x**2+y**2-4*x-y-x*y

initial_guess = [3,3]
result = optimize.minimize(f, initial_guess)
if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)