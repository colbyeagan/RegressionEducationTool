# Linear and Higher Order Regression Dashboard

I created this project to practice my computational math skills. This is a web app which can be ran and used to show how regression fits models data and is effected by noise. By generating X data points in either a normal or uniform distribution and then making the Y coordinates of those points a transformation of the X values, one can create their desired coorelation. Then, by adding noise through the form of a normal or uniform random distribution to the y coordinates, one can visualize the effect of noise on coorelation in data. The final step requires an oI walk through my steps for calculating regression below. 

# Linear regression walkthrough
There are many ways to calculate regression, however using matrices is one of my favorite ways because of how scalable it is to higher orders as well as how quick it is when the A matrix is invertible upon projection to the nearest subspace.  
  
$$Ax = b$$
Let matrix A be a matrix with height of the number of data points. A has a column of ones, a column of the x values, and an extra column for every higher order desired in our line of best fit where the column will be the x values to that order. For instance, for a line of best fit with order to the power of 2, the A matrix will have a column of ones, of x values, and of each of the x values squared. For a line of best fit with order of 3, just add another column of each of the x values to the power of 3. Let x be of height of the number of columns in A. x is unknown. We are trying to solve for x. The solution for x will be called x with a hat on top, or x hat. x hat will be the coefficients of each x in our line of best fit. Finally, be is simply a matrix with one column that contains all of the y coordinates. 
$$Ax = b$$
Solve by multiplying both sides by A transpose -----------------------------------------------------------------------------------
$$A^TA\hat{x} = A^Tb$$
Simplify -------------------------------------------------------------
$$\hat{x} = ((A^TA)^{-1})(A^Tb)$$
When ATA is not invertible, take the pseudoinverse to approximate the closest inverse. In all cases, one is safest to simply take the pseudoinverse becasuse if the matrix is invertible then the pseudoinverse will just be the inverse. It is more computationally intensive, but not much more.

Then to calculate Error for metrics like R squared or MAE etc, you can use the fact that the error matrix equals
$$e = b - p$$
Where -------------------------------------------------------------
$$p = A\hat{x}$$  
  
Next to calculate R², we use the following equation ---------------------------------------------------------
$$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
$$=$$
$$R^2 = 1 - \frac{SSR}{SST}$$
The numerator of this equation is called the sum squared regression (SSR). It is the sum of the squared differences between all of the actual y data points and their predicted values on the lne of best fit.  
The denominator is called the total sum of squares (SST). It is the sum of the squared differences between all of the actual y data points and the mean of all of the y data points.