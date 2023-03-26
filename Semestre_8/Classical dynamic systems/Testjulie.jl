using LinearAlgebra, Random
using ProgressBars, Plots
using DelimitedFiles


# function

function com(x,y)
    mat = x*y - y*x
    n, m = size(mat)
    # for i = 1:n
    #     for j = 1:n
    #         if abs(imag(mat[i, j])) < 1e-10
    #             mat[i, j] = real(mat[i, j])
    #         end
    #     end
    # end
    return mat
end

function A(x)
    return com(X1, com(x, X1)) + com(X2, com(x, X2)) + com(X3, com(x, X3))
end

function Er(line, column)
    mat = randn(ComplexF64, line, column) .* (0.1 + 0.1im) .+ 0.5im
    mat = (mat + dague(mat)) / 2
    for i = 1:n
        mat[i, i] = real(mat[i, i])
    end
    return mat
end

function J(sgn)
    J = zeros(ComplexF64, mj, mj)
    for i = 1:mj
        for k = 1:mj
            if sgn == "+"
                if m[k] + 1 == m[i]
                    J[i, k] = sqrt(j*(j+1) - m[k]*(m[k]+1))
                end
            elseif sgn == "z"
                if m[i] == m[k]
                    J[i, k] = m[k]
                end
            else
                if m[k] - 1 == m[i]
                    J[i, k] = sqrt(j*(j+1) - m[k]*(m[k]-1))
                end
            end
        end
    end
    return J
end

function dague(x)
    return x'
end

function NormMat(a, b, c)
    return sqrt(norm(a) + norm(b) + norm(c))
end

# Constants
const j = 1
const std = 0.01
const mj = Int(2*j+1)
const m = [j-i for i = 0:mj-1]
const n = Int(2*j+2)
const t = 1000
const t0 = 0
const tf = 200
const h = (tf - t0) / t
const XT = [i*h for i = 0:t-1]
const X1 = zeros(ComplexF64, n, n)
const X2 = zeros(ComplexF64, n, n)
const X3 = zeros(ComplexF64, n, n)

J1 = (J("+") + J("-")) / 2
J2=(J("+")-J("-"))/(2im)
J3=J("z")


println(com(J1,J2) == im*J3)
println(com(J1,J2))
println(im*J3)
writedlm(stdout, J3)
printl(com(J2,J3) == 1j*J1)
printl(com(J2,J3))
printl(1j*J1)

printl(com(J3,J1) == 1j*J2)
printl(com(J3,J1))
printl(1j*J2)

X1[1:end-1,1:end-1] = J1/j
X1[1:end-1,end] = rand(Normal(0, std), mj).*exp.(1im*rand(Uniform(0,2*pi), mj))
X1[end,1:end-1] = conj(X1[1:end-1,end])
X1[end,end] = 5

X2[1:end-1,1:end-1] = J2/j
X2[1:end-1,end] = rand(Normal(0, std), mj).*exp.(1im*rand(Uniform(0,2*pi), mj))
X2[end,1:end-1] = conj(X2[1:end-1,end])
X2[end,end] = 0

X3[1:end-1,1:end-1] = J3/j
X3[1:end-1,end] = rand(Normal(0, std), mj).*exp.(1im*rand(Uniform(0,2*pi), mj))
X3[end,1:end-1] = conj(X3[1:end-1,end])
X3[end,end] = 0

# v = zeros(ComplexF64, n, n)
# v[end,end] = 0
# V1 = v + A(X1)*h/2
# V2 = v + A(X2)*h/2
# V3 = v + A(X3)*h/2

# Vacum = zeros(ComplexF64, 3, t)
# Prob = zeros(ComplexF64, 3, t)
# Det = zeros(ComplexF64, 3, t)
# Dia = []
# Vacum[1,1] = sqrt(dot(X1[1:end-1,end], X1[end,1:end-1]))
# Vacum[2,1] = sqrt(dot(X2[1:end-1,end], X2[end,1:end-1]))
# Vacum[3,1] = sqrt(dot(X3[1:end-1,end], X3[end,1:end-1]))
# #read the pos of prob
# Prob[1,1] = X1[end,end]
# Prob[2,1] = X2[end,end]
# Prob[3,1] = X3[end,end]

# push!(Dia, NormMat(X1,X2,X3))

# # Det[1,1] = det(X1)
# # Det[2,1] = det(X2)
# # Det[3,1] = det(X3)
