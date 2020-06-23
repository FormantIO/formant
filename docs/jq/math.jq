def avg: reduce .[] as $n (0; . + $n) / length;
def pow2: . * .;
def variance: . | avg as $avg | map_values(. - $avg | pow2) | avg;
def stdev: . | variance | sqrt;

map(.value|tonumber)  |
stdev as $stdev |
avg as $avg |
variance as $variance |
{avg: $avg, stdev:$stdev, variance: $variance}
