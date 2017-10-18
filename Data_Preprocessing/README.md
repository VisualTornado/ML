Decision tree regression uses a ID3 algorithm which follows a top down approach using a standard deviation reduction methodology for selection of decision nodes.

SDR(a, b) = sd(a) - sd(a, b)  -- Sd of target/dependent variable is calculated before data is split amongst the independent variables.

The variable with highest SDR is choosen as root and then the process is recursive for the following decision nodes till the leaf nodes.

Decision tree can be used for both numerical and categorical data.
