def validate_card(card_number:str):
    card_number = list(str(card_number).strip())

    # Remove the last digit from the card number
    check_digit = card_number.pop()

    # Reverse the order of the remaining numbers
    card_number.reverse()

    processed_digits = []

    for index, digit in enumerate(card_number):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2

            # Subtract 9 from any results that are greater than 9       
            if doubled_digit > 9:
                doubled_digit = doubled_digit - 9

            processed_digits.append(doubled_digit)
        else:
            processed_digits.append(int(digit))

    total = int(check_digit) + sum(processed_digits)

    # Verify that the sum of the digits is divisible by 10
    if total % 10 == 0:
        print( "Valid!")
        return "Valid"
    else:
        print( "Invalid!")