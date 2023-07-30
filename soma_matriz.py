def soma_matrizes(m1,m2):
    line_m1 = len(m1)
    line_m2 = len(m2)
    column_m1 = len(m1[0])
    column_m2 = len(m2[0])

    if line_m1 == line_m2 and column_m1 == column_m2:
        i = 0
        while i < line_m1:
            j = 0
            while j < column_m1:
                m1[i][j] = m1[i][j] + m2[i][j]
                j += 1
            i += 1
        return m1
                
                
    else:
        return False
