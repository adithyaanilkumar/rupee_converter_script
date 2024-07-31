

words_list = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
    10 : "Ten",
    11 : "Eleven",
    12 : "Twelve",
    13 : "Thirteen",
    14 : "Fourteen",
    15 : "Fifteen",
    16 : "Sixteen",
    17 : "Seventeen",
    18 : "Eighteen",
    19 : "Nineteen",
    20 : "Twenty",
    30 : "Thirty",
    40 : "Fourty",
    50 : "Fifty",
    60 : "Sixty",
    70 : "Seventy",
    80 : "Eighty",
    90 : "Ninety",
    100: "Hundread",
    1000 : "Thousand",
    100000 : "Lakh",
    10000000 : "Crore"
}


def check_and_print_num() :
    num = 10000
    sliced_num = num
    count = 2
    num_string = ""
    
    # Less than 20, then print directly from list
    if(num<20) :
        
        print(" \n#######################################\n")
        print("  " + "Rs. " + str(num)  )
        print(" \n---------------------------------------\n")
        print("  "+words_list[num] + " Rupees Only")
        print(" \n#######################################\n")
        return
    while(sliced_num!=0) : 
        # If two digits
        if count == 2 :
            # Get the last digit
            current_digits = sliced_num % 100
            if current_digits!=0 :
                # In the case of 15,17 etc
                if current_digits<20 :
                    num_string = words_list[current_digits]
                # In the case of 45,87 etc
                else :
                    first_digit = current_digits % 10
                    second_digit = current_digits // 10
                    #print("first_digit is", first_digit)
                    #print("second_digit is", second_digit)
                    if(first_digit!=0) :
                        num_string =  words_list[first_digit]        
                    if(second_digit!=0) :
                        num_string = words_list[second_digit*10] + " " + num_string 
            count +=1
            sliced_num = abs(sliced_num//100)
            #print("sliced_num  is ", sliced_num)
            # If there is a digit still remaining, add "and" before the hundread
            if(sliced_num!=0 and current_digits!=0) :
                num_string = "and " + num_string
            #print("words string is ", num_string)
        # If Hundread
        elif count == 3 :
            #print("count is ", count)
            current_digits = sliced_num % 10
            #print("current_digits is ", current_digits)
            if current_digits!=0 :
                 # Since hundread doesnt have twelve hundread, we just need to look at till 9
                num_string = words_list[current_digits] + " Hundread " + num_string
                #print("num_string is ", num_string)
            sliced_num = abs(sliced_num//10)
            count +=1
            #print("sliced_num  is ", sliced_num)
            #print("words string is ", num_string)
        # If Thousand
        elif count == 4 :
            #print("count is ", count)
            current_digits = sliced_num % 100
            #print("current_digits  is ", current_digits)
            if current_digits!=0 :
                # Same logic as for 45,50 etc
                if current_digits<20 :
                    num_string = words_list[current_digits]+ " Thousand " + num_string
                else :
                    first_digit = current_digits % 10
                    second_digit =  current_digits // 10 
                    #print("first_digit  is ", first_digit)
                    #print("second_digit  is ", second_digit)
                    first_word =""
                    if(first_digit!=0) :
                        first_word =  words_list[first_digit] + " "
                    if(second_digit!=0) :
                        # To cover the case of differentiating between 50000 and 89000
                        num_string =  words_list[second_digit*10] + " " + first_word + "Thousand " + num_string 
            count +=1
            sliced_num = abs(sliced_num//100)
            #print("sliced_num  is ", sliced_num)
            #print("words string is ", num_string)
        # If Lakh
        elif count == 5 :
            #print("count is ", count)
            current_digits = sliced_num % 100
            #print("current_digits is ", current_digits)
            if current_digits!=0 :
                if current_digits<20 :
                    num_string = words_list[current_digits]+ " Lakh " + num_string
                else :
                    first_digit = current_digits % 10
                    second_digit = current_digits // 10
                    #print("first_digit is ", first_digit)
                    #print("second_digit is ", second_digit)
                    first_word =""
                    if(first_digit!=0) :
                        first_word =  words_list[first_digit] + " "
                    if(second_digit!=0) :
                        # To cover the case of differentiating between 5000000 and 8900000
                        num_string =  words_list[second_digit*10] + " " + first_word + " Lakh " + num_string 
            count +=1
            sliced_num = abs(sliced_num//100)
            #print("sliced_num is ", sliced_num)
            #print("words string is ", num_string)
        # If crore
        elif count == 6 :
            #print("count is ", count)
            current_digits = sliced_num % 100
            #print("current_digits is ", current_digits)
            if current_digits!=0 :
                if current_digits<20 :
                    num_string = words_list[current_digits]+ " Crore " + num_string
                else :
                    first_digit = current_digits % 10
                    second_digit = current_digits // 10
                    #print("first_digit is ", first_digit)
                    #print("second_digit is ", second_digit)
                    first_word =""
                    if(first_digit!=0) :
                        first_word =  words_list[first_digit] + " "
                    if(second_digit!=0) :
                        num_string =  words_list[second_digit*10] + " " + first_word + " Crore " + num_string 
            count +=1
            sliced_num = abs(sliced_num//100)
            #print("sliced_num is ", sliced_num)
            #print("words string is ", num_string)
    print(" \n#######################################\n")
    print("  " + "Rs. " + str(num)  )
    print(" \n---------------------------------------\n")
    print("  "+num_string + "Rupees Only")
    print(" \n#######################################\n")
check_and_print_num()           
            
