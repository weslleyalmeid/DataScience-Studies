\* Source Pyomo model name=unknown *\

max 
objetivo:
+100 QTD_PRODUCT(1)
+120 QTD_PRODUCT(2)
+135 QTD_PRODUCT(3)
+90 QTD_PRODUCT(4)
+125 QTD_PRODUCT(5)
+110 QTD_PRODUCT(6)
+105 QTD_PRODUCT(7)

s.t.

c_u_limite_material_product(1)_:
+5 QTD_PRODUCT(2)
+5 QTD_PRODUCT(3)
+4 QTD_PRODUCT(4)
+8 QTD_PRODUCT(5)
+5 QTD_PRODUCT(6)
+3 QTD_PRODUCT(7)
<= 100

c_u_limite_material_product(2)_:
+3 QTD_PRODUCT(1)
+10 QTD_PRODUCT(2)
+3 QTD_PRODUCT(3)
+6 QTD_PRODUCT(4)
+2 QTD_PRODUCT(5)
+2 QTD_PRODUCT(6)
+2 QTD_PRODUCT(7)
<= 150

c_u_limite_material_product(3)_:
+10 QTD_PRODUCT(1)
+10 QTD_PRODUCT(2)
+9 QTD_PRODUCT(3)
+3 QTD_PRODUCT(4)
+8 QTD_PRODUCT(5)
+10 QTD_PRODUCT(6)
+7 QTD_PRODUCT(7)
<= 200

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
   0 <= QTD_PRODUCT(1) <= +inf
   0 <= QTD_PRODUCT(2) <= +inf
   0 <= QTD_PRODUCT(3) <= +inf
   0 <= QTD_PRODUCT(4) <= +inf
   0 <= QTD_PRODUCT(5) <= +inf
   0 <= QTD_PRODUCT(6) <= +inf
   0 <= QTD_PRODUCT(7) <= +inf
end
