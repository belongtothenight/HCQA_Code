from pyqubo import Binary, dimod

x1, x2, x3, x4, x5, x6, x7, x8 = Binary("x1"), Binary("x2"), Binary("x3"), Binary("x4"), Binary("x5"), Binary("x6"), Binary("x7"), Binary("x8")

a = 25*x1 + 7*x2 + 13*x3 + 31*x4 + 42*x5 + 17*x6 + 21*x7 + 10*x8
H = (166-2*a)**2

model = H.compile()
qubo, offset = model.to_qubo()
solution = dimod.SimulatedAnnealingSampler().sample_qubo(qubo, num_sweeps=10000)
print(solution.first, offset)
