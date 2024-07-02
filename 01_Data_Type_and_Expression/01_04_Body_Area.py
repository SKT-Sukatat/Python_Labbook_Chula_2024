import math

W, H = [float(x) for x in input().split()]

Mosteller = math.sqrt(W*H)/60
Haycock = 0.024265*(W**0.5378)*(H**0.3964)
Boyd = 0.0333 * (W**(0.6157 - 0.0188*math.log10(W))) * (H**0.3)

print(Mosteller)
print(Haycock)
print(Boyd)