import re

def ID_patient(input_file, output_file):
    file = open(input_file)
    pattern = re.compile(r"([A-Z]){2,3}-\d{12}|([A-Z]){2,3}-\d{4}-\d{4}-\d{4}")
    text = file.read()
    redacted = re.sub(pattern,"redacted", text)


    output = open(output_file, "w")
    output.write(redacted)
    output.close()

ID_patient("file.txt", "whatever.txt" )



