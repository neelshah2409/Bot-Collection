print("Title of program: Encouragement bot")
print()
while True:
    description = input("Could you describe how you feel in a sentence?")

    list_of_words = description.split()

    feelings_list = []
    encouragement_list = []
    counter = 0

    for each_word in list_of_words:

        if each_word == "miserable":
            feelings_list.append("miserable")
            encouragement_list.append("tomorrow will be a better day")
            counter += 1
        if each_word == "happy":
            feelings_list.append("happy")
            encouragement_list.append("to keep smiling")
            counter += 1
        if each_word == "tired":
            feelings_list.append("tired")
            encouragement_list.append(
                "you will make it through ! remember to take a break when you need to"
            )
            counter += 1
        if each_word == "exhausted":
            feelings_list.append("exhausted")
            encouragement_list.append("you are stronger than you think")
            counter += 1
        if each_word == "angry":
            feelings_list.append("angry")
            encouragement_list.append("calm down, things will turn better.")
            counter += 1
        if each_word == "scared":
            feelings_list.append("scared")
            encouragement_list.append("you are not alone")
            counter += 1
        if each_word == "lonely":
            feelings_list.append("lonely")
            encouragement_list.append(
                "your friends are always ther for you!hou 'bout talking to them?"
            )
            counter += 1
        if each_word == "confused":
            feelings_list.append("confused")
            encouragement_list.append(
                "everything will work out eventually, stay positive!"
            )
            counter += 1
        if each_word == "devastated":
            feelings_list.append("devastated")
            encouragement_list.append("bad times would pass")
            counter += 1
        if each_word == "troubled":
            feelings_list.append("troubled")
            encouragement_list.append(
                "that your troubles will end! there is always light at the end of the tunnel! i'm sure you will somehow overcome it all"
            )
            counter += 1
    if counter == "sad":
        if each_word == "stressed":
            feelings_list.append("stressed")
            encouragement_list.append("take a deep breath")
            counter += 1

            output = "dont be sad every cloud has a silver lining"

    elif counter == 1:

        output = (
            "It seems that you are feeling quite "
            + feelings_list[0]
            + ". However, do remember that "
            + encouragement_list[0]
            + "! Hope you feel better :)"
        )

    else:

        feelings = ""
        for i in range(len(feelings_list) - 1):
            feelings += feelings_list[i] + ", "
        feelings += "and " + feelings_list[-1]

        encouragement = ""
        for j in range(len(encouragement_list) - 1):
            encouragement += encouragement_list[i] + ", "
        encouragement += "and " + encouragement_list[-1]

        output = (
            "It seems that you are feeling quite "
            + feelings
            + ". Please always remember "
            + encouragement
            + "! Hope you feel better :)"
        )

    print()
    print(output)
    print()
