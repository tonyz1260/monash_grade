def single_unit_wam_sum(mark, credit_point, year_level):
    if year_level == 1:
        return mark*credit_point*0.5
    else:
        return mark*credit_point*1


def single_unit_hwa_sum(mark, credit_point, year_level):
    return mark*credit_point*year_level


def single_unit_wam_divide(credit_point, year_level):
    if year_level == 1:
        return credit_point*0.5
    else:
        return credit_point*1


def single_unit_hwa_divide(credit_point, year_level):
    return credit_point*year_level


def wam(results):
    sum = 0
    divisor = 0
    for i in range(0,len(results)):
        sum += single_unit_wam_sum(results[i][0],results[i][1],results[i][2])
    for j in range(0,len(results)):
        divisor += single_unit_wam_divide(results[j][1],results[j][2])
    return sum/divisor

def hwa(results):
    sum = 0
    divisor = 0
    for i in range(0,len(results)):
        sum += single_unit_hwa_sum(results[i][0],results[i][1],results[i][2])
    for j in range(0,len(results)):
        divisor += single_unit_hwa_divide(results[j][1],results[j][2])
    return sum/divisor
