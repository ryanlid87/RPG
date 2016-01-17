def promptUser(prompt, options):
    while True:
        userInput = raw_input(prompt+"\n>")

        if userInput in options:
            return userInput
        else:
            print "Invalid option. Available actions:"
            print options
