# How to measure production? Cobb Douglas production function regression

One of the main interests in economics is to calculate efficiency in terms of production. Every country, firm, and individual wants to maximize production in an efficient way since it leads to creation of wealth and later on it impacts other factors like innovation and technological advancement. We can think of production as managing inputs in order to generate an output. A Cobb-Douglas production function is a mathematical tool that helps us understand how the output produced depends on the quantity of capital and labor.

Cobb-Douglas production function is definded as Y_i = A * K_i^α L_i^β where Y_i is a measure of output, K_i is the capital stock, and L_i is employment. A is the total factor productivity which is the ratio of aggregate output to aggregate inputs.
α is the output elasticity of capital and β is the output elasticity of labor.
This formula is useful for figuring out the best combination of inputs to make production efficient and for estimating how technology affects the way we produce things.

In this project, I used data on output (value added) and inputs at the industry level for 459 industries in 1958. 
The production function was transformed to a linear equation by taking logs and the parameters α and β by an OLS regression using total value added asa measure of output was estimated. Hypothesis test was also applied.
Later on, materials and energy were added as a factor of production.
