# Zusammenfassung
---
## Array Indizierung und Slicing
### Bsp. Array Indizierung
```python
1D
array1d = np.array([0,1,2,3,4,5,6,7,8,9])
array1d[element]

2D
array2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
array2d[row,element]
```
### Bsp. Array Slicing ohne Step

array1d[startpunkt:endpunkt]        Array von Startpunkt bis Endpunkt
array1d[:endpunkt]                  Array von Anfang bis Endpunkt
array1d[startpunkt:]                Array von Startpunkt bis Ende
array1d[:]                          ganzes Array

array2d[startzeile:endzeile,startelement:endelement]

### Bsp. Array Slicing mit Step

array1d[startpunkt:endpunkt:step]   Step ist die Schrittweite default = 1 jeder Wert  Bsp. 2 = jeder 2. Wert 

## Neuordnen von Matritzen mit "reshape"
test
