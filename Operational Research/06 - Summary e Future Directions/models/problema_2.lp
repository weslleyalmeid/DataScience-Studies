\* Source Pyomo model name=unknown *\

min 
objetivo:
-4174 a
-206366 b
+ [
+26 a ^ 2
+2556 a * b
+65594 b ^ 2
] / 2
+365387 ONE_VAR_CONSTANT

s.t.

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
    -inf <= a <= +inf
    -inf <= b <= +inf
end
