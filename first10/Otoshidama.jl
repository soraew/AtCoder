using Printf

line = readline()
N, Y = split(line, " ")
N = parse(Int64, N)
Y = parse(Int64, Y)


function otoshi(N, Y)
    flag = false
    for ten = 0:N
        for fiv = 0:(N - ten)
            one = N - ten - fiv
            if ten*10000 + fiv*5000 + one*1000 == Y
                @printf "%d %d %d" ten fiv one
                flag = !flag
                return 0
            end
        end
    end

    if !flag
        println("-1 -1 -1")
    end
        
end

otoshi(N, Y)