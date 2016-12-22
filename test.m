
%{
Find u_0, u_1 ... u_T such that ||x_T||^2 is minimum
Where:
    x_t = A * x_t-1 + B * u_t-1
    x_0 = [0, 0, 0]';
    A =   [[0.7500,   -0.1500,   -0.3500];
          [-1.9000,   -0.0000,    0.1000];
           [1.7500,    0.7500,    0.8500]];
    B = [1, 1, 1]'
    T = 5
    u_0, u_1 ... u_T-1 are scalars and in the set {-1,1}.
%}
in.h = [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]';
in.J = [[ -1.65585035e-01  -3.36029250e-01  -4.11874975e-01  -1.23657500e-02 ...
   -3.32676600e-01  -4.50512150e-01   2.72506500e-01  -2.44275000e-01 ...
   -3.89067500e-01   5.55925000e-01  -1.21560000e-01  -2.14515000e-01 ...
    2.66650000e-01  -2.87500000e-01  -1.08750000e-01];
 [ -3.36029250e-01  -1.06307429e+00  -1.36899600e+00   4.20221400e-01 ...
   -8.85386250e-01  -1.33338810e+00   1.63057500e+00  -3.64468500e-01 ...
   -8.54400000e-01   2.54499000e+00   1.67625000e-01   2.30400000e-02 ...
    4.38750000e-01  -8.79600000e-01   3.11250000e-01];
 [ -4.11874975e-01  -1.36899600e+00  -1.77029134e+00   5.92258250e-01 ...
   -1.12156050e+00  -1.70687635e+00   2.18555250e+00  -4.23750000e-01 ...
   -1.05830350e+00   3.36582500e+00   2.77950000e-01   1.08165000e-01 ...
    5.22750000e-01  -1.12750000e+00   4.75150000e-01];
 [ -1.23657500e-02   4.20221400e-01   5.92258250e-01  -5.22093500e-01 ...
    2.20305000e-01   4.55876500e-01  -1.24207500e+00  -1.73760000e-01 ...
    4.53250000e-02  -1.62335000e+00  -4.99500000e-01  -5.56350000e-01 ...
    1.17500000e-01   3.09000000e-01  -6.42500000e-01];
 [ -3.32676600e-01  -8.85386250e-01  -1.12156050e+00   2.20305000e-01 ...
   -7.84678500e-01  -1.13645400e+00   1.13994000e+00  -4.19625000e-01 ...
   -8.18250000e-01   1.89300000e+00  -1.93500000e-02  -1.80900000e-01 ...
    4.66500000e-01  -7.50000000e-01   6.75000000e-02];
 [ -4.50512150e-01  -1.33338810e+00  -1.70687635e+00   4.55876500e-01 ...
   -1.13645400e+00  -1.68667550e+00   1.92568500e+00  -5.20710000e-01 ...
   -1.13013500e+00   3.06865000e+00   1.23600000e-01  -8.05500000e-02 ...
    6.08500000e-01  -1.11100000e+00   2.86500000e-01];
 [  2.72506500e-01   1.63057500e+00   2.18555250e+00  -1.24207500e+00 ...
    1.13994000e+00   1.92568500e+00  -3.50835000e+00   2.25000000e-02 ...
    8.18250000e-01  -4.95750000e+00  -9.96000000e-01  -9.61500000e-01 ...
   -2.35000000e-01   1.25000000e+00  -1.37500000e+00];
 [ -2.44275000e-01  -3.64468500e-01  -4.23750000e-01  -1.73760000e-01 ...
   -4.19625000e-01  -5.20710000e-01   2.25000000e-02  -4.10850000e-01 ...
   -5.55000000e-01   3.09000000e-01  -3.37500000e-01  -4.86000000e-01 ...
    3.75000000e-01  -3.60000000e-01  -3.75000000e-01];
 [ -3.89067500e-01  -8.54400000e-01  -1.05830350e+00   4.53250000e-02 ...
   -8.18250000e-01  -1.13013500e+00   8.18250000e-01  -5.55000000e-01 ...
   -9.27350000e-01   1.53250000e+00  -2.25000000e-01  -4.33500000e-01 ...
    5.75000000e-01  -7.50000000e-01  -1.85000000e-01];
 [  5.55925000e-01   2.54499000e+00   3.36582500e+00  -1.62335000e+00 ...
    1.89300000e+00   3.06865000e+00  -4.95750000e+00   3.09000000e-01 ...
    1.53250000e+00  -7.23500000e+00  -1.20000000e+00  -1.03500000e+00 ...
   -7.50000000e-01   1.90000000e+00  -1.75000000e+00];
 [ -1.21560000e-01   1.67625000e-01   2.77950000e-01  -4.99500000e-01 ...
   -1.93500000e-02   1.23600000e-01  -9.96000000e-01  -3.37500000e-01 ...
   -2.25000000e-01  -1.20000000e+00  -5.85000000e-01  -6.90000000e-01 ...
    1.50000000e-01  -8.88178420e-16  -7.50000000e-01];
 [ -2.14515000e-01   2.30400000e-02   1.08165000e-01  -5.56350000e-01 ...
   -1.80900000e-01  -8.05500000e-02  -9.61500000e-01  -4.86000000e-01 ...
   -4.33500000e-01  -1.03500000e+00  -6.90000000e-01  -8.55000000e-01 ...
    3.50000000e-01  -1.00000000e-01  -8.50000000e-01];
 [  2.66650000e-01   4.38750000e-01   5.22750000e-01   1.17500000e-01 ...
    4.66500000e-01   6.08500000e-01  -2.35000000e-01   3.75000000e-01 ...
    5.75000000e-01  -7.50000000e-01   1.50000000e-01   3.50000000e-01 ...
   -1.00000000e+00  -0.00000000e+00  -0.00000000e+00];
 [ -2.87500000e-01  -8.79600000e-01  -1.12750000e+00   3.09000000e-01 ...
   -7.50000000e-01  -1.11100000e+00   1.25000000e+00  -3.60000000e-01 ...
   -7.50000000e-01   1.90000000e+00  -8.88178420e-16  -1.00000000e-01 ...
   -0.00000000e+00  -1.00000000e+00  -0.00000000e+00];
 [ -1.08750000e-01   3.11250000e-01   4.75150000e-01  -6.42500000e-01 ...
    6.75000000e-02   2.86500000e-01  -1.37500000e+00  -3.75000000e-01 ...
   -1.85000000e-01  -1.75000000e+00  -7.50000000e-01  -8.50000000e-01 ...
   -0.00000000e+00  -0.00000000e+00  -1.00000000e+00]];
