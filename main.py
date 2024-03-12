# Case #3
# Developers: Khramchikhina A., Peshkov Y., Sanzhanova A., Yurshenaite A.
#

import ru_local as ru


def income():
    '''
    The function determines the annual income amount.
    :return: amount of income
    '''
    amount = 0
    for month in range(0, 12):
        value = float(input(f'{ru.INCOME} {ru.MONTH[month]} [USD]: '))
        amount += value
    return amount


def free_tax():
    '''
    The function determines the annual tax-free amount.
    :return: amount of tax-free amount
    '''
    amount = 0
    for month in range(0, 12):
        value = float(input(f'{ru.FREE_TAX} {ru.MONTH[month]} [USD]: '))
        amount += value
    return amount


def subject(income_for_tax):
    '''
    The function calculates the amount of the annual tax for single subject.
    :param income_for_tax: amount of taxable income
    :return: amount of tax
    '''
    if income_for_tax < 9_076:
        tax = 0.1 * income_for_tax
        return tax
    elif income_for_tax < 36_901:
        tax = 0.1*9_075 + 0.15*(income_for_tax - 9_075)
        return tax
    elif income_for_tax < 89_351:
        tax = 0.1*9_075 + 0.15*27_825 + 0.25*(income_for_tax - 36_900)
        return tax
    elif income_for_tax < 186_351:
        tax = 0.1*9_075 + 0.15*27_825 + 0.25*52_450 + 0.28*(income_for_tax - 89_350)
        return tax
    elif income_for_tax < 405_101:
        tax = 0.1*9_075 + 0.15*27_825 + 0.25*52_450 + 0.28*97_000 + 0.33*(income_for_tax - 186_350)
        return tax
    elif income_for_tax < 406_751:
        tax = 0.1*9_075 + 0.15*27_825 + 0.25*52_450 + 0.28*97_000 + 0.33*218_750 + 0.35*(income_for_tax - 405_100)
        return tax
    else:
        tax = 0.1*9_075 + 0.15*27_825 + 0.25*52_450 + 0.28*97_000 + 0.33*218_750 + 0.35*1_650 + \
              0.396*(income_for_tax - 406_750)
        return tax


def couple(income_for_tax):
    '''
    The function calculates the amount of the annual tax for married couple.
    :param income_for_tax: amount of taxable income
    :return: amount of tax
    '''
    if income_for_tax < 18_151:
        tax = 0.1 * income_for_tax
        return tax
    elif income_for_tax < 73_801:
        tax = 0.1*18_150 + 0.15*(income_for_tax - 18_150)
        return tax
    elif income_for_tax < 148_851:
        tax = 0.1*18_150 + 0.15*55_650 + 0.25*(income_for_tax - 73_800)
        return tax
    elif income_for_tax < 226_851:
        tax = 0.1*18_150 + 0.15*55_650 + 0.25*75_050 + 0.28*(income_for_tax - 148_850)
        return tax
    elif income_for_tax < 405_101:
        tax = 0.1*18_150 + 0.15*55_650 + 0.25*75_050 + 0.28*78_000 + 0.33*(income_for_tax - 226_850)
        return tax
    elif income_for_tax < 457_601:
        tax = 0.1*18_150 + 0.15*55_650 + 0.25*75_050 + 0.28*78_000 + 0.33*178_250 + 0.35*(income_for_tax - 405_100)
        return tax
    else:
        tax = 0.1*18_150 + 0.15*55_650 + 0.25*75_050 + 0.28*78_000 + 0.33*178_250 + 0.35*52_500 + \
              0.396*(income_for_tax - 457_600)
        return tax


def parent(income_for_tax):
    '''
    The function calculates the amount of the annual tax for one parent.
    :param income_for_tax: amount of taxable income
    :return: amount of tax
    '''
    if income_for_tax < 12_951:
        tax = 0.1 * income_for_tax
        return tax
    elif income_for_tax < 49_401:
        tax = 0.1*12_950 + 0.15*(income_for_tax - 12_950)
        return tax
    elif income_for_tax < 127_551:
        tax = 0.1*12_950 + 0.15*36_450 + 0.25*(income_for_tax - 49_400)
        return tax
    elif income_for_tax < 206_601:
        tax = 0.1*12_950 + 0.15*36_450 + 0.25*78_150 + 0.28*(income_for_tax - 127_550)
        return tax
    elif income_for_tax < 405_101:
        tax = 0.1*12_950 + 0.15*36_450 + 0.25*78_150 + 0.28*79_050 + 0.33*(income_for_tax - 206_600)
        return tax
    elif income_for_tax < 432_201:
        tax = 0.1*12_950 + 0.15*36_450 + 0.25*78_150 + 0.28*79_050 + 0.33*198_500 + 0.35*(income_for_tax - 405_100)
        return tax
    else:
        tax = 0.1*12_950 + 0.15*36_450 + 0.25*78_150 + 0.28*79_050 + 0.33*198_500 + 0.35*27_100 + \
              0.396*(income_for_tax - 432_200)
        return tax


def main():
    '''
    Main function.
    :return: None
    '''
    print(ru.CATEGORY, ru.SUBJECT, ru.COUPLE, ru.PARENT, sep='\n')
    category = int(input(ru.VALUE))
    print(ru.YEAR_INCOME)
    total_income = income()
    print(ru.TOTAL_INCOME, total_income)
    print(ru.YEAR_FREE_TAX)
    total_free_tax = free_tax()
    print(ru.TOTAL_FREE_TAX, total_free_tax)
    income_for_tax = total_income - total_free_tax
    print(ru.INCOME_FOR_TAX, income_for_tax)
    if category == 1:
        print(ru.YEAR_TAX, format(subject(income_for_tax), '.2f'))
        print(ru.MONTH_PAYMENT, format(subject(income_for_tax) / 12, '.2f'))
    elif category == 2:
        print(ru.YEAR_TAX, format(couple(income_for_tax), '.2f'))
        print(ru.MONTH_PAYMENT, format(couple(income_for_tax) / 12, '.2f'))
    else:
        print(ru.YEAR_TAX, format(parent(income_for_tax), '.2f'))
        print(ru.MONTH_PAYMENT, format(parent(income_for_tax) / 12, '.2f'))


if __name__ == '__main__':
    main()
