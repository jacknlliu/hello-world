m = int(input('please input the orginal number system'))
n = int(input('please input the objective number system'))
m_str = input('the orginal integer ')

if(float(m_str)==int(float(m_str))):
        m_number = int(m_str,m)#get the numeric value of m
        symbol = ''

        if(m_number<0):#figure out the final symbol
                m_number = abs(m_number)#get positive value
                symbol = '-'

        if(n == 10):# m convert to 10
                print(symbol+str(m_number))
        else:#10 convert to n
                ans = ''
                while(m_number):
                        ans = str(m_number%n) + ans#doing the mod
                        m_number = m_number//n#warning!!: using // not /
                print(symbol+ans)#print the answer
else:
        print('input is not integer')
